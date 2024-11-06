#!/usr/bin/python


from bs4 import BeautifulSoup
import requests


def parser(url):
    req = requests.get(url).text
    soup = BeautifulSoup(req, 'lxml')
    for article in soup.find_all('article'):
        print(article.h4.a.text)



def main():
    parser("https://www.theaustralian.com.au/")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(str(e))