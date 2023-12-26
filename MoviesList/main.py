#making requests

import requests
from bs4 import BeautifulSoup

url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response=requests.get(url)

web_page=response.text

#parsing the html content

soup=BeautifulSoup(web_page,'html.parser')
all_movies=soup.find_all(name="h3", class_="title")
print(all_movies)

movie_titles = [movie.getText() for movie in all_movies]
movies = movie_titles[::-1]

with open("movies.txt", mode="w" ,encoding='utf-8') as file:
    for movie in movies:
        file.write(f"{movie}\n")