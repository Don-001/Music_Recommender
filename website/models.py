from . import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    user_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(60), nullable=False)
    playlists = db.relationship('Playlist')
    likes = db.relationship('Like')

   # def __repr__(self):
        #return f"User('{self.user_id}', '{self.username}', '{self.email}')"


class Playlist(db.Model):
    playlist_id = db.Column(db.Integer, primary_key=True)
    playlist_name = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    songs = db.relationship('Song', secondary='playlist_song')

    #def __repr__(self):
        #return f"Playlist('{self.playlist_id}', '{self.playlist_name}')"


class Song(db.Model):
    song_id = db.Column(db.Integer, primary_key=True)
    song_name = db.Column(db.String(100), nullable=False)
    artist = db.Column(db.String(100), nullable=False)
    album = db.Column(db.String(100), nullable=False)

   # def __repr__(self):
      #  return f"Song('{self.song_id}', '{self.song_name}', '{self.artist}', '{self.album}')"


class Like(db.Model):
    like_id = db.Column(db.Integer, primary_key=True)
    song_id = db.Column(db.Integer, db.ForeignKey('song.song_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))

    #def __repr__(self):
       # return f"Like('{self.like_id}', '{self.song_id}', '{self.user_id}')"


# association table for many-to-many relationship between Song and Playlist
