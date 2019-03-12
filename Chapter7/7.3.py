import unittest
class Song():
    def __init__(self,title,data):
        self.playing = False
        self.title = title
        self.data = data
        self.play_count = 0

    def stop(self):
        self.playing = False

    def play(self):
        self.is_playing = True
        self.play_count += 1

class JukeBox():
    def __init__(self,songs):
        self.songs = dict()
        for song in songs:
            self.songs[song.title] = song
        self.playing = None

    def play_song(self,title):
        if self.playing == None:
            self.playing = title
            self.songs[title].play()
        else:
            self.song[self.playing].stop()
            self.playing = title
            self.songs[title].play()

    def now_playing(self):
        print(self.playing)


def main():
    song1 = Song("It was just a dream", "1234567890234567")
    song2 = Song("I believe I can", "123456098765432")
    jukebox = JukeBox([song1, song2])
    jukebox.play_song("I believe I can")
    jukebox.now_playing()

if __name__ == "__main__":
    main()
