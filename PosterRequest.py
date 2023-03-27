#Christopher SanGiovanni

import requests
import random

def get_random_movie():
    # key from TMDB website which we need for all api requests
    key = "a141575823e91856c7c532de60ea8eb6"
    # This link specifically grabs popular movies so we dont fetch anything irrelevant 
    url = f"https://api.themoviedb.org/3/movie/popular?api_key={key}"

    # use .get() to grab top 20 popular movies and convert from json 
    # they are stored in a dictionary object
    response = requests.get(url).json()

    #for i in response["results"]:
    	#print(i["title"])

    # Grab a random movie using random library, "results" is a key for the dict
    movie = random.choice(response["results"])

    # Grab Poster URL
    poster_url = "https://image.tmdb.org/t/p/w500" + movie["poster_path"]
    # Return the movie title and overview
    
    #movie, poster_url = get_random_movie()
    #print(movie)
    #print(poster_url)
    return f"{movie['title']}", poster_url