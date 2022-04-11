import pandas as pd
import numpy as np

if __name__ == "__main__":
    #Read Netflix data
    netflix_data = pd.read_csv("netflix_titles.csv")

    #Read imdb movies + tv series
    imdb_data = pd.read_csv("title_basic_imdb.tsv", sep = '\t')

    #Read imdb ratings
    imdb_rating = pd.read_csv("movie_ratings.tsv", sep = "\t")

    #Merge IMDB ratings + items
    new_dataframe_with_rating = pd.merge(imdb_data, imdb_rating, how = 'inner',on = ['tconst'])

    #Remove TV Episodes
    new_dataframe_with_rating = new_dataframe_with_rating[new_dataframe_with_rating['titleType']!='tvEpisode']

    #Rename column
    new_dataframe_with_rating = new_dataframe_with_rating.rename(columns={"originalTitle":"title"})
    new_dataframe_with_rating = new_dataframe_with_rating.drop_duplicates(subset=['title'])

    #Merge Netflix data and Rating data
    new_data_netflix = pd.merge(netflix_data,new_dataframe_with_rating, how = 'inner', on = ['title'])
    
    print(new_data_netflix)
    new_data_netflix.to_csv('netflix_ratings_data.csv', sep=',', index=False)
