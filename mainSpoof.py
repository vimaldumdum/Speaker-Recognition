from readAudioFile import read_wav
import os
from interface import ModelInterface


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
    m=ModelInterface()

    dirs = os.listdir(train_sounds_path)
    wavs = []
    if len(dirs) == 0:
        print('Directory empty')
    else:
        for d in dirs:
            ext = os.path.splitext(d)[-1].lower()
            if ext == '.wav':
                wavs.append(d)
    for w in wavs:
        sample_rate, signal = read_wav(os.path.join(train_sounds_path, w))
        label=os.path.splitext(w)[0]
        m.enroll(label,sample_rate,signal)
    m.train()
    m.dump()

def predict():
    predict_sound_path=os.path.join(os.getcwd(),'predictSounds')
    m=ModelInterface.load()
    dirs = os.listdir(predict_sound_path)
    wavs=[]
    if len(dirs)==0:
        print('No wav files found')
    else:
        for d in dirs:
            ext = os.path.splitext(d)[-1].lower()
            if ext=='.wav':
                wavs.append(d)
    sum=0
    scores=0
    for w in wavs:
        fs, signal = read_wav(os.path.join(predict_sound_path, w))
        label, score = m.predict(fs, signal)
        sum=sum+score
        scores=scores+1
        print(w, '->', label, ", score->", score)


if __name__ == '__main__':
    x='y'
    enroll()
    predict()
    while x=='y' or x=='Y':
        helpFun()
        choice=input('Enter your choice: ')
        if choice=='-e':
            enroll()
            x='n'
        elif choice=='-p':
            predict()
            x='n'
        else:
            print('Invalid choice... Enter again(Y/N)')

