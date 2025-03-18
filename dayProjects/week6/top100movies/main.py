from bs4 import BeautifulSoup
import requests

URL = "https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(URL)
website_html = response.text
site = BeautifulSoup(website_html, "html.parser")
movie_titles = site.select("span h2 strong")
movie_titles = [title.getText().replace("é", "e") + "\n" for title in movie_titles]
movie_titles.reverse()
with open(file="dayProjects/week6/top100movies/movie_list.txt", mode="w") as movie_list:
    movie_list.writelines(movie_titles)