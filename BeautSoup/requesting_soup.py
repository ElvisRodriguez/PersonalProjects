import requests
from bs4 import BeautifulSoup

def example():
    result = requests.get("https://www.google.com/")
    # print(result.status_code)
    # print(result.headers)
    src = result.content
    soup = BeautifulSoup(src, features="html.parser")
    links = soup.find_all("a")
    # print(links)
    # print("\n")
    for link in links:
        if "About" in link.text:
            print(link)
            print(link.attrs['href'])

def white_house():
    result = requests.get("https://www.whitehouse.gov/briefings-statements/")
    if result.status_code == 200:
        urls = []
        src = result.content
        soup = BeautifulSoup(src, features="html.parser")
        for h2_tag in soup.find_all("h2"):
            a_tag = h2_tag.find("a")
            urls.append(a_tag.attrs['href'])
        print(urls)

if __name__ == "__main__":
    white_house()
