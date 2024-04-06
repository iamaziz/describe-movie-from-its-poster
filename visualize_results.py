import umap
import pandas as pd
import plotly.express as px


# @lru_cache(maxsize=32)
def plot_umap(df: pd.DataFrame):
    """
    Plot 3D scatter plot of documents embeddings using UMAP or TSNE
    """

    VEC_COL = "plot_embedding"
    GROUP_COL = "genres" # "genres", "title", ..etc 
    PLOT_COL = "plot"
    TITLE_COL = "title"

    # create embeddings df from dict
    vecs_df = df[VEC_COL].apply(pd.Series)
    
    # take the first value of the GROUP_COL list (instead of a list of genres, take the first genre only)
    df[GROUP_COL] = df[GROUP_COL].apply(lambda x: x[0])

    
    # truncate documents strings to improve readability in the plot points with hover over
    # MAX_CHARS = 96
    # df[PLOT_COL] = df[PLOT_COL].apply(lambda x: x[:120] + "..." if len(x) > MAX_CHARS else x)

    # @st.cache_data(show_spinner='transforming...')
    def umap_transform(df):
        reducer = umap.UMAP(n_components=3)
        projections = reducer.fit_transform(df)
        return projections

    # radio to choose between UMAP and TSNE
    projections = umap_transform(vecs_df)

    # -- plot 3D projection as scatter plot
    df[GROUP_COL] = df[GROUP_COL].apply(str)  # from dict to string

    # truncate metadatas to improve readability in the plot
    # df[GROUP_COL] = df[GROUP_COL] #.apply(lambda x: x[:50] + "..." if len(x) > MAX_CHARS else x)  # this will determine color groups

    fig = px.scatter_3d(
        projections, x=0, y=1, z=2,
        color=df[GROUP_COL], labels={'color': GROUP_COL},  # cluster grouping
        hover_data={PLOT_COL: df[PLOT_COL], TITLE_COL: df[TITLE_COL], GROUP_COL: df[GROUP_COL]},
        # color_discrete_sequence=px.colors.qualitative.Antique  # use color gradient
    )
    # change plot size to fit the screen
    fig.update_layout(width=800, height=800)

    # change hover style text orientation from center to left
    fig.update_traces(textposition='bottom left')
    
    # points size
    fig.update_traces(marker_size=4)

    # legend position
    fig.update_layout(legend=dict(
        yanchor="bottom",
        y=0.9,
        xanchor="right",
        x=0.3),
    )

    return fig
