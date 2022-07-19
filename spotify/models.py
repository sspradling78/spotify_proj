from flask_sqlalchemy import SQLAlchemy


# creating the database and connecting to it.
DB = SQLAlchemy()

class Song(DB.Model):
    '''Getting song from Spotify. Load into Database.'''
    track_id = DB.Column(DB.BigInteger, primary_key=True)
    track_name = DB.Column(DB.String, nullable=False)
    explict = DB.Column(DB.Boolean, nullable=False)
    track_length = DB.Column(DB.Time, nullable=False)
    track_genre = DB.Column(DB.String, nullable=False)
    track_artist = DB.Column(DB.String, nullable=False)
    
    def __repr__(self):
        return f'''Song Title: {self.track_name}<p></p>
                   Artist:  {self.track_artist}<p></p>
                   Genre: {self.track_genre}<p></p>
                   Song Length:  {self.track_length}<p></p>
                   Explict:  {self.explict}'''

class Artist(DB.Model):
    pass

class SearchFor(DB.Model):
    '''Search for artist'''
    pass