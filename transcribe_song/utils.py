from omnizart.music.app import MusicTranscription
from omnizart.drum.app import DrumTranscription
# from omnizart.chord.app import ChordTranscription
from omnizart.vocal.app import VocalTranscription
from omnizart.beat.app import BeatTranscription
import base64

VOCAL = VocalTranscription()
DRUM = DrumTranscription()
BEAT = BeatTranscription()
MUSIC = MusicTranscription()

def transcribe_b64(file_content, difficulty = 3):
    filename = "temp.mp3"
    try:
        file_content = base64.b64decode(file_content.encode('ascii'))
        with open(filename, "wb") as f:
            f.write(file_content)
        transcribe(filename, difficulty)
        with open(filename[:-3] + "mid", "rb") as f:
            return base64.b64encode(f.read()).decode("ascii")
    except Exception as e:
        print(str(e))

def transcribe(file, difficulty = 3):
    """
    Transcribes the audio file at a given difficulty, and outputs the .midi file with the same filename.
    EASY = 0
    MEDIUM = 1
    HARD = 2
    EXTREME = 3
    """
    model = None
    if difficulty == 0: model = VOCAL
    elif difficulty == 1: model = DRUM
    elif difficulty == 2: model = BEAT
    else: model = MUSIC
    model.transcribe(file) # output is file.mid
