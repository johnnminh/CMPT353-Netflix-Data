# Required datasets:
## Please download the following datasets: 
- netflix_titles.csv: https://www.kaggle.com/datasets/shivamb/netflix-shows

- title.basic.tsv.gz: https://datasets.imdbws.com/title.basics.tsv.gz
  After downloading and unzipping this dataset, please **`rename`** the file to **`title_basic_imdb.tsv`**
  
- title.ratings.tsv.gz: https://datasets.imdbws.com/title.ratings.tsv.gz
  After downloading and unzipping this dataset, please **`rename`** the file to **`movie_ratings.tsv`**

# Prepare datasets:
- First, run the **`preparing_data.ipynb`** file in Jupyter notebook for reading datasets and preparing dataset
- Run **`title_recommendation.ipynb`** in Jupyter notebook for title recommendation. 
- Run **`genre_analysis.ipynb`** in Jupyter notebook for quality analysis between genres and the Posthoc.png 
- Run **`predict_imdb_score.ipynb`** in Jupyter notebook for analyzing imdb score prediction and see output of the models
- Run **`line_plots_rating.ipynb`** in Jupyter notebook to see output of the linegraphs


Analyze:
- predict imdb score of movies based on genre, director, actors
- movies and TV shows rating over time by genre (draw lineplot)
- distribution of movies and TV shows by genre (draw barplot)
- movie recommendation

