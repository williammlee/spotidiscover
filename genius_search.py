from googlesearch import search as gsearch
from bs4 import BeautifulSoup
from search import Search
import requests


class GeniusSearch(Search):

    def __init__(self, query):
        super().__init__(query)

    def search_web(self):
        # look for "genius" in results
        results = []
        genius_query = "site:genius.com " + self.query
        for url in gsearch(genius_query):
            results.append(url)
        for link in results:
            if "genius" in link:
                self.url = link
                return link
        return None

    def create_soup(self):
        page = requests.get(self.search_web())
        self.soup = BeautifulSoup(page.content, 'html.parser')
        return self.soup

    def find_title(self):
        self.title = self.create_soup().select(
            'h1.header_with_cover_art-primary_info-title')[0].text.strip()
        return self.title

    def find_artist(self):
        self.artist = self.create_soup().select(
            'a.header_with_cover_art-primary_info-primary_artist')[0].text.strip()
        return self.artist
