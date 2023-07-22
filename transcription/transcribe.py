from omnizart.music.app import MusicTranscription
from omnizart.drum.app import DrumTranscription
# from omnizart.chord.app import ChordTranscription
from omnizart.vocal.app import VocalTranscription
from omnizart.beat.app import BeatTranscription

def transcribe(file, difficulty = 3):
    """
    Transcribes the audio file at a given difficulty, and outputs the .midi file with the same filename.
    EASY = 0
    MEDIUM = 1
    HARD = 2
    EXTREME = 3
    """
    model = None
    if difficulty == 0: model = VocalTranscription()
    elif difficulty == 1: model = DrumTranscription()
    elif difficulty == 2: model = BeatTranscription()
    else: model = MusicTranscription()
    model.transcribe(file) # output is file.midi
