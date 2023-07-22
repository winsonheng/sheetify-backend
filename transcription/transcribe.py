from omnizart.music.app import MusicTranscription
model = MusicTranscription()
def transcribe(file):
    model.transcribe(file) # output is file.midi
