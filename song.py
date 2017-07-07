from mongoengine import *


class Song(Document):
    image = StringField()
    title = StringField()
    artist = StringField()