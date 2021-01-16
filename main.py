from spotify_api import *
from genius_search import *
import webbrowser
import webpage


CLIENT_ID = "480b5435dcf240fdbfb3fa533d5ab00d"
CLIENT_SECRET = "cb1105402e3142b5a52c38f6d44284e8"


def track(json_query):
    get_track_url = json_query.get("tracks").get(
        "items")[0].get("external_urls").get("spotify")
    return webbrowser.open(get_track_url)


def play(json_query):
    play_track_preview = json_query.get("tracks").get(
        "items")[0].get("preview_url")
    if play_track_preview is None:
        raise Exception("Track Preview Not Found")
    else:
        webbrowser.open(play_track_preview)

if __name__ == "__main__":
    # Begin HTML Scraping

    #ask_query = webpage.request.form['input']

    # Begin Genius Search
    q = input('Type your lyrics: ')
    genius = GeniusSearch(q)
    song_title = genius.find_title()
    song_artist = genius.find_artist()
    print("The title is: " + song_title)
    print("The artist is: " + song_artist)
    print("------Done Scraping------")

    # Begin Spotify Querying

    query = {"track": song_title, "artist": song_artist}
    spotify = SpotifyAPI(CLIENT_ID, CLIENT_SECRET)
    json_query = spotify.search(query, search_type="Track")
    track(json_query)
    play(json_query)