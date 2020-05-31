from spotify_api import *
from search import *


CLIENT_ID = "480b5435dcf240fdbfb3fa533d5ab00d"
CLIENT_SECRET = "cb1105402e3142b5a52c38f6d44284e8"


def main():
    ask_query = input("Lyrics: ")
    soup = create_soup(search_web(ten_urls(ask_query)))
    song_title = find_title(soup)
    song_artist = find_artist(soup)
    print("The title is: " + song_title)
    print("The artist is: " + song_artist)
    print("------Done Scraping------")

    query = {"track": song_title, "artist": song_artist}

    spotify = SpotifyAPI(CLIENT_ID, CLIENT_SECRET)
    print(spotify.search(query, search_type="Track"))


if __name__ == '__main__':
    main()

# tracks, items[0], external_urls, spotify-> to open up the link to song
# tracks, items[0], preview_url -> play the song's sample
