# What a movie Poster tells about its Story ?

<p align="center"><img src="logo.png" width="500" /></p>

An app to search for a movie and get a description of what the movie poster tells about the plot.

> Event

- MongoDB GenAI Hackathon - NYC April, 6th 2024


> Technology used

- Vision and embedding LLMs (OpenAI)
- Vector Search (MongoDB Atlas)
- UI (Streamlit / Python)
- UMAP projections (embeddings dimensionality reduction)
- Plotly Express (3D projection visualization)


# Demo

<iframe width="560" height="315" src="https://www.youtube.com/embed/elXIyfNfdC8" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


## Setup

> Edit `atlas_client.py` to add the corresponding MongoDB settings
> Add `OPENAI_KEY_API` to environment variables

 ## Getting Started

 Install requirements:

```bash
pip instal -r requirements.txt
```

## Run the app

```bash
streamlit run app.py
```

