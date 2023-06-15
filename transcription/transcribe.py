from omnizart.music.app import MusicTranscription
model = MusicTranscription()
def transcribe(file):
    model.transcribe(file, model_path = "./test_model") # output is file.midi
