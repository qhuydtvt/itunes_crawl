from urllib import request
from bs4 import BeautifulSoup
import mlab
from mongoengine import *
from song import *

mlab.connect()

html = request.urlopen("https://www.apple.com/itunes/charts/songs/").read().decode("utf-8")

soup = BeautifulSoup(html, "html.parser")

songs_section = soup.find("section", "section chart-grid")

songs_div_content = songs_section.find("div", "section-content")

song_ul_list = songs_div_content.ul

song_li_info_list =  song_ul_list.find_all("li")

print("Deleting all songs")
Song.drop_collection()
print("Done")

for li_song_info in song_li_info_list:
    image = "https://www.apple.com" + li_song_info.a.img["src"]
    title = li_song_info.h3.a.string
    artist = li_song_info.h4.a.string

    print("Saving {0}...".format(title))
    song = Song(image=image, title=title, artist=artist)
    song.save()
