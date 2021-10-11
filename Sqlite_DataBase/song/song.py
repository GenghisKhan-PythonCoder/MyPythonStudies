import sqlite3

class Song():
    def __init__(self, name , artist , album , production , time):
        self.name = name
        self.artist = artist
        self.album = album
        self.production = production
        self.time = time

    def __str__(self):
        return f"Şarkı ismi:{self.name}\nSanatçı:{self.artist}\nAlbüm:{self.album}\nProdüksiyon şirketi:{self.production}\nŞarkı süresi:{self.time}"


class Data():
    def __init__(self):
        self.connection()

    def connection(self):

        self.connection = sqlite3.connect("data.db")

        self.cursor = self.connection.cursor()

        ask = "CREATE TABLE IF NOT EXISTS songs(name TEXT,artist TEXT,album TEXT,production TEXT,time FLOAT)"

        self.cursor.execute(ask)

        self.connection.commit()

    def disconnect(self):
        self.connection.close()

    def show_songs(self):
        ask = "SELECT * FROM songs"

        self.cursor.execute(ask)

        songs = self.cursor.fetchall()

        if (len(songs) == 0):
            print("Kayıtlı şarkı bulunamadı.")
        else:
            for i in songs:
                song = Song(i[0],i[1],i[2],i[3],i[4])
                print(song,"\n")

    def question_song(self,name):
        ask = "SELECT * FROM songs WHERE name = ?"

        self.cursor.execute(ask,(name,))

        songs = self.cursor.fetchall()

        if (len(songs) == 0):
            print("Kayıtlarda böyle bir şarkı bulunamıyor")
        else:
            song = Song(songs[0][0],songs[0][1],songs[0][2],songs[0][3],songs[0][4])
            print(song)

    def add_song(self,song):
        ask = "INSERT INTO songs VALUES(?,?,?,?,?)"

        self.cursor.execute(ask,(song.name,song.artist,song.album,song.production,song.time))

        self.connection.commit()

    def del_song(self,name):
        ask = "DELETE FROM songs WHERE name = ?"

        self.cursor.execute(ask,(name,))