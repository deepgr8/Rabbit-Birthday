from pydub import AudioSegment
from pydub.playback import play

aud = AudioSegment.from_file('new.wav')
play(aud)