from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth


date = input(
    "What year would you like to travel to? Type the data in this format YYYY-MM-DD: ")

URL = f"https://www.billboard.com/charts/hot-100/{date}"
response = requests.get(URL)
response_html = response.text

soup = BeautifulSoup(response_html, "html.parser")

# Get entire tag elements hor song titles and song writers:
all_song_titles = soup.select("h3.a-no-trucate")
all_song_writers = soup.select("span.a-no-trucate")

# Get song titles and song writers text only:
song_titles = [record.getText().strip() for record in all_song_titles]
song_writers = [record.getText().strip() for record in all_song_writers]

# print(song_titles)
# print(song_writers)

# SPOTIFY API SETUP

SPOTIFY_ID = "d0e50d9cb9ca4a3f88bb4ceb1cdc71ad"
SPOTIFY_SECRET = ""

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://localhost:8888/callback",
        client_id=SPOTIFY_ID,
        client_secret=SPOTIFY_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)

user_id = sp.current_user()["id"]
