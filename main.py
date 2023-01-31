from bs4 import BeautifulSoup
import requests


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

print(song_titles)
print(song_writers)
