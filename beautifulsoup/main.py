import requests
from bs4 import BeautifulSoup

url = "https://www.infoworld.com/"

# url = "https://www.developer-tech.com/news"

# url = "https://www.crn.com/news/"


response = requests.get(url)

filename = "news.html"

# print(response.content)

data = BeautifulSoup(response.content, "html.parser")

with open(filename, 'w') as f:
    f.write(str(data))
