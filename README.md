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

# Screenshot

<img width="1429" alt="image" src="https://github.com/iamaziz/describe-movie-from-its-poster/assets/3298308/a0646673-633e-4d7b-90bc-b9f01f80e2bd">


# Demo

[![Demo](http://img.youtube.com/vi/elXIyfNfdC8/0.jpg)](http://www.youtube.com/watch?v=elXIyfNfdC8?si=HDFgKoeskBmilt9L)

## Setup

> - Edit `atlas_client.py` to add the corresponding MongoDB settings
> - Add `OPENAI_KEY_API` to environment variables

 ## Getting Started

 Install requirements:

```bash
pip install -r requirements.txt
```

## Run the app

```bash
streamlit run app.py
```

