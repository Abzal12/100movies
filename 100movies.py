from bs4 import BeautifulSoup
import lxml
import requests

response = requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
movies = response.text

soup = BeautifulSoup(movies, "html.parser")

movies = soup.find_all(name="h3", class_="title")

movies = [movie.getText() for movie in movies]
movies.reverse()

with open("movies.txt", "w", encoding="utf-8") as m_file:
    m_file.write(';\n'.join(movies))
