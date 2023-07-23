from omnizart.music.app import MusicTranscription
model = MusicTranscription()
def train():
    # generate feature files from dataset
    model.generate_feature("./testing_dataset/maestro") 

    # train model based on feature files
    model.train("./testing_dataset/maestro/train_feature") # not working (library bug?)

def main():
    train()

if __name__ == "__main__":
    main()
