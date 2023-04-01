
from flask import render_template,Flask
import os
import threading
from pydub import AudioSegment
from playsound import playsound
from pydub.playback import play
os.environ['FLASK_DEBUG'] = 'development'
os.environ["PYDUB_PLAYBACK"] = "audio"
app = Flask(__name__)
app.config["SECRET_KEY"] = "thsdssf"

@app.route('/')
def index():
    # t = threading.Thread(target=play_audio)
    # t.start()
    return render_template('/index.html')

if __name__ == "__main__":
    app.run(debug=True)
