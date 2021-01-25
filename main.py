from bs4 import BeautifulSoup
import requests, sys

try:
    url = sys.argv[1]
    html_content = requests.get(url).text

    soup = BeautifulSoup(html_content, 'lxml')

    links = []

    for link in soup.find_all("link"):
        links.append(link.get("href"))

    img_url = links[0]

    print(img_url)

except IndexError:
    url = input("Enter the URL of the score: ")
    html_content = requests.get(url).text

    soup = BeautifulSoup(html_content, 'lxml')

    links = []

    for link in soup.find_all("link"):
        links.append(link.get("href"))

    img_url = links[0]

    print(img_url)