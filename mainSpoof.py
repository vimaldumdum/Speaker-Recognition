from readAudioFile import read_wav
import os
from os import system


def helpFun():
    print("This message will show how to use this project.")
    msg="you can select from the following options: \n" \
        "1. ENROLL \n" \
        "   Enroll: Enter an audio file in the dataset. Enter '-e' without quotes to select this option.\n" \
        "2. PREDICT\n" \
        "   Predict: Enter an audio file and predict the result. Enter '-p' without quotes to select this option."
    print(msg)

def enroll():
    train_sounds_path = os.path.join(os.getcwd(), "trainSounds")
    print('inside enroll fun')

    dirs = os.listdir(train_sounds_path)
    wavs = []
    if len(dirs) == 0:
        print('Directory empty')
    else:
        for d in dirs:
            ext = os.path.splitext(d)[-1].lower()
            if ext == '.wav':
                wavs.append(d)

    print(wavs)


def predict():
    predict_sound_path=os.path.join(os.getcwd(),'predictSounds')
    dirs = os.listdir(predict_sound_path)
    wavs=[]
    if len(dirs)==0:
        print('No wav files found')
    else:
        for d in dirs:
            ext = os.path.splitext(d)[-1].lower()
            if ext=='.wav':
                wavs.append(d)


if __name__ == '__main__':
    x='y'
    while x=='y' or x=='Y':
        helpFun()
        choice=input('Enter your choice: ')
        if choice=='-e':
            enroll()
        elif choice=='-p':
            predict()
        else:
            print('Invalid choice... Enter again(Y/N)')

