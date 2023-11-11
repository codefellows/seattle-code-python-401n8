import requests
from bs4 import BeautifulSoup


url = "https://adamowada.github.io/scrape-demo/"
response = requests.get(url)

# print(response.content)  # see the html response of the GET request

# 1. Go to target website
# 2. Find the content you WANT to scrape
# 3. Trial and error to target the content

# Target the h1 element
soup = BeautifulSoup(response.content, "html.parser")
h1_result = soup.find("h1")
print(h1_result.text)

# Target the li elements
li_results = soup.find_all("li")
print(li_results)

for item in li_results:
    print(item.text)
