import requests
from bs4 import BeautifulSoup
import spotipy


date=input("which year do you want to travel to?Type the date in this format YYYY-MM-DD")

url="https://www.billboard.com/charts/hot-100/"
response=requests.get(url + date)
soup = BeautifulSoup(response.text, 'html.parser')
song_names=soup.select("li ul li h3")
songs=[song.getText().strip() for song in song_names]
