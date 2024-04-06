import streamlit as st
import requests
import pandas as pd
from streamlit_image_select import image_select
from streamlit_agraph import agraph, Node, Edge, Config

from atlas_client import AtlasClient
from openai_client import OpenAIClient
from visualize_results import plot_umap

st.set_page_config(layout="wide")
st1, st2 = st.columns([2, 1])
with st1: st.title("What a movie poster tells about its story?")
with st2: st.image("logo.png", width=200)

def is_image_valid(image_url):
    try:
        response = requests.get(image_url, stream=True)
        if 'content-type' in response.headers and response.headers['content-type'].startswith('image/'):
            return True
        else:
            return False
    except requests.exceptions.RequestException:
        return False


def select_poster(df):

    # remove nan values from poster field
    df = df.dropna(subset=['poster'])

    # check if the image is valid (not broken link)
    df = df[df['poster'].apply(is_image_valid)]

    # -- in image selector
    img_idx = image_select(label="Matching movie posters, click on a poster to get its details", images=df['poster'], return_value='index', captions=df['title'])
    return img_idx
    

def visulaize_embedding(df):
    fig = plot_umap(df)
    st.plotly_chart(fig, use_container_width=True)


def agraph_network(df):
    # https://github.com/ChrisDelClea/streamlit-agraph?tab=readme-ov-file#basic-usage    

    # drop nan values from dataframe
    df = df.dropna(subset=['cast', 'title', 'poster'])

    nodes = []
    edges = []
    seen = set()
    for idx, movie in df.iterrows():
        if movie['title'] not in seen:
            nodes.append(Node(id=idx, 
                            label=movie['title'],
                            size=45,
                            shape="circularImage",
                            image=movie['poster'],
                            key=movie['title'],
                            ))
            seen.add(movie['title'])
        
        # -- edges for acted_in relation
        for actor in movie['cast']:
            if actor not in seen:
                nodes.append(Node(id=actor, label=actor, size=25))
                edges.append(Edge(source=idx, label="cast", target=actor))
                seen.add(actor)
    
    config = Config(width=900,
                height=450,
                directed=True, 
                physics=True, 
                hierarchical=True,
                # **kwargs
                )

    return agraph(nodes=nodes, edges=edges, config=config)


def main():
    
    db = AtlasClient()
    llm_client = OpenAIClient()

    st1, st2 = st.columns(2)
    query = st1.text_input("Describe the movie you are looking for", placeholder="e.g. love story in manhattan")
    max_results = st2.slider("Max results", 1, 50, 10)
    if query:
        
        # embed query
        query_embedding = llm_client.get_embedding(query)
        
        # vector search: https://github.com/sujee/mongodb-atlas-vector-search/blob/main/lab-2-vector-search-openai/vector-search-openai.ipynb
        results = db.vector_search(embedding_vector=query_embedding, limit=max_results)
        
        # -- convert results to a dataframe and display
        df = pd.DataFrame(results)
        

        # -- display all results
        with st.expander("Vector Search Results (MongoDB Atlas)"):
            st1, st2 = st.columns(2)
            if st1.toggle("Show all results", False): st.data_editor(df, use_container_width=True)
            # -- visulaize embedding
            if st2.toggle("3D Plot"): visulaize_embedding(df)

        # render images from the 'poster' field
        img_idx = select_poster(df)
        # if not img_idx: st.stop()
        row = df.iloc[img_idx]
        row_df = pd.DataFrame(row).T # flip index to columns
    

        # extract the full plot and poster from the selected movie
        full_plot = row_df['fullplot'].values[0]
        poster = row_df['poster'].values[0]
        

        st.markdown(f"# Selected Movie: `{row_df['title'].values[0]}`")
        # -- display selected movie
        st1, st2 = st.columns(2)
        # -- display its agraph cast network
        with st1:
            st.markdown("### Cast Network")
            agraph_network(row_df)

        with st2:
            st.markdown("### Movie details")
            st.data_editor(row, use_container_width=True, height=500)
        
    
        # -- display the description
        st1, st2 = st.columns(2)
        
        with st1:
            st.image(poster, caption=row['title'])
        with st2:
            # -- OpenAI client to generate description of the movie plot and its poster
            with st.spinner("Analyzing the movie plot and its poster..."):
                @st.cache_data(show_spinner=False)
                def cached_response(full_plot, poster):
                    return llm_client.describe_images(full_plot, poster)
                description, prompt = cached_response(full_plot, poster)
            st.markdown(f"### What the movie poster tells about the plot?")
            st.write(description)

        with st.expander("LLM prompt"):
            st.code(prompt)

if __name__ == "__main__":
    main()
    