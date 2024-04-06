# What a movie Poster tells about its Story ?

<p align="center"><img src="logo.png" width="500" /></p>

> What

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

[![Demo](http://img.youtube.com/vi/elXIyfNfdC8/0.jpg)](http://www.youtube.com/watch?v=elXIyfNfdC8?si=HDFgKoeskBmilt9L)

## Setup

> - Edit `atlas_client.py` to add the corresponding MongoDB settings
> - Add `OPENAI_KEY_API` to environment variables

 ## Getting Started

 Install requirements:

```bash
pip instal -r requirements.txt
```

## Run the app

```bash
streamlit run app.py
```

