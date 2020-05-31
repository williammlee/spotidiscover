from googlesearch import search as gsearch
from bs4 import BeautifulSoup
from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials
import requests
import sys
import spotipy.util as util
from spotify_api import SpotifyAPI

SPOTIPY_CLIENT_ID = "480b5435dcf240fdbfb3fa533d5ab00d"
SPOTIPY_CLIENT_SECRET = "cb1105402e3142b5a52c38f6d44284e8"


def ten_urls(lyrics):
    results = []

    # now searching
    for url in gsearch(lyrics, tld="com", num=10, stop=10, pause=2):
        results.append(url)

    return results


def search_web(urls):
    # look for "genius" in results
    for link in urls:
        if "genius" in link:
            return link

    return None


def create_soup(url):
    page = requests.get(url)
    return BeautifulSoup(page.content, 'html.parser')


def find_title(soup):
    title = soup.select(
        'h1.header_with_cover_art-primary_info-title')[0].text.strip()
    return title


def find_artist(soup):
    artist = soup.select(
        'a.header_with_cover_art-primary_info-primary_artist')[0].text.strip()
    return artist
