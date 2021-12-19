from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Write your informations below this line 👇 (You can achieve it on developer.spotify.com)
CLIENT_ID = "YOUR CLIENT ID"
CLIENT_SECRET = "YOUR CLIENT SECRET"


# Scraping Billboard 100
date = input("Which year do you want to travel to? Type the date in this format (YYYY-MM-DD): ")

URL = f"https://www.billboard.com/charts/hot-100/{date}"

response = requests.get(URL)

billboard_page = response.text

soup = BeautifulSoup(response.text, 'html.parser')
song_names_spans = soup.find_all("h3", class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021"
                                              " lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 "
                                              "u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 "
                                              "u-max-width-230@tablet-only")
song_names = [song.getText() for song in song_names_spans]

#Spotify Authentication
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id= CLIENT_ID,
        client_secret= CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
print(user_id)

#Searching Spotify for songs by title
song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

#Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

#Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
