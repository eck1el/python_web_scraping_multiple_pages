import bs4
import requests
from lxml import html

def webscraping_test():
    url_base = 'http://books.toscrape.com/catalogue/page-{}.html'


    for n in range(1, 11):
        print(url_base.format(n))
if __name__ == '__main__':
    webscraping_test()
