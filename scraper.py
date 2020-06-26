from bs4 import BeautifulSoup
import requests
import json

url = 'https://www.imdb.com/chart/top/'
response = requests.get(url, timeout=5)
content = BeautifulSoup(response.content, "html.parser")


#movie = content.findAll('div',attrs={"class" : "lister-list"}).text
#movie = content.find_all('a')

movies = content.find_all('td', class_='titleColumn')
list_names = []
list_year = []
for movie in movies:
    moviename = movie.find('a').get_text()
    year = movie.find('span').get_text()
    list_names.append(moviename)
    list_year.append(year)

    
ratings = []
for rating in content.find_all('td', class_='ratingColumn imdbRating'):
    r = rating.find('strong').get_text()
    r = float(r)
    ratings.append(r)

movieArr = []
for i in range (250):
    movieObject = {
        "title": list_names[i],
        "year": list_year[i],
        "rating": ratings[i]
    }
    movieArr.append(movieObject)
with open('movieData.json', 'w') as outfile:
    json.dump(movieArr, outfile)