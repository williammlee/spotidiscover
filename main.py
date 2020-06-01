from spotify_api import *
from genius_search import *
import webbrowser


CLIENT_ID = "480b5435dcf240fdbfb3fa533d5ab00d"
CLIENT_SECRET = "cb1105402e3142b5a52c38f6d44284e8"


def main():

    # Begin HTML Scraping

    ask_query = input("Lyrics: ")

    # Begin Genius Search

    genius = GeniusSearch(ask_query)
    song_title = genius.find_title()
    song_artist = genius.find_artist()
    print("The title is: " + song_title)
    print("The artist is: " + song_artist)
    print("------Done Scraping------")

    # Begin Spotify Querying

    query = {"track": song_title, "artist": song_artist}
    spotify = SpotifyAPI(CLIENT_ID, CLIENT_SECRET)
    json_query = spotify.search(query, search_type="Track")
    get_track_url = json_query.get("tracks").get(
        "items")[0].get("external_urls").get("spotify")
    play_track_preview = json_query.get("tracks").get(
        "items")[0].get("preview_url")
    webbrowser.open(get_track_url)
    if play_track_preview is None:
        raise Exception("Track Preview not Available")
    else:
        webbrowser.open(play_track_preview)


if __name__ == '__main__':
    main()
