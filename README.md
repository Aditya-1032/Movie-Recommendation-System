# Movie Recommendation System
### Content-Based Filtering Using Python & Streamlit

A content-based movie recommendation application that suggests five similar movies based on a user's selected movie.

The system analyses movie metadata, including genres, keywords, plot overviews, cast and crew, to identify similarities between movies.

## Features

- Search and select movies from the available dataset.
- Get five similar movie recommendations.
- View movie posters alongside recommendations.
- Content-based filtering using cosine similarity.
- Interactive web interface built with Streamlit.

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- NLTK
- Streamlit
- TMDB API

## Recommendation Approach

1. Movie metadata is combined to create a text-based representation of each movie.
2. Text preprocessing and stemming are applied.
3. CountVectorizer converts movie metadata into numerical vectors.
4. Cosine similarity measures similarity between movies.
5. The system retrieves the top five recommendations for the selected movie.

## Dataset

The project uses the TMDB 5000 Movies and TMDB 5000 Credits datasets.

## Run Locally

```bash
git clone https://github.com/Aditya-1032/Movie-Recommendation-System.git

cd Movie-Recommendation-System

pip install -r requirements.txt

streamlit run app.py
```

A TMDB API key is required to retrieve movie posters. Configure it securely using Streamlit secrets.

## Deployment

The application is intended to be deployed using Streamlit Community Cloud.

## Acknowledgements

- TMDB for movie data and poster information.
- Scikit-learn for machine learning utilities.
- Streamlit for the application framework.
