# pygame mixer
from pygame import mixer
mixer.init()
mixer.music.load(r'C:....Desktop\music'+ r'/Dus.mp3')
mixer.music.play()
mixer.music.stop()

# vlc
from vlc import MediaPlayer
x_song = MediaPlayer('x.mp3')
x_song.play()
x_song.stop()
