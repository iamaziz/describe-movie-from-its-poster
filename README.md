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

# Screenshot examples

![image](https://github.com/iamaziz/describe-movie-from-its-poster/assets/3298308/2828832e-c39e-4171-b5fe-12070f2a5918)

![image](https://github.com/iamaziz/describe-movie-from-its-poster/assets/3298308/bf006a7c-191c-4f97-a648-e37118139766)

![image](https://github.com/iamaziz/describe-movie-from-its-poster/assets/3298308/da02df80-6551-48d4-8944-abc8727cad94)

![image](https://github.com/iamaziz/describe-movie-from-its-poster/assets/3298308/5f146812-5865-4d26-9ad2-18e768b4a3b8)

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

