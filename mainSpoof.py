import os
from readAudioFile import read_wav
from interface import ModelInterface

def task_enroll():
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

    m= ModelInterface()

    for w in wavs:
        sample_rate, signal=read_wav(os.path.join(train_sounds_path,w))
        label=os.path.splitext(w)[0]
        m.enroll(label,sample_rate,signal)
        print(label + ' enrolled')

    m.train()
    m.dump('data.bin')

def task_predict():
    m = ModelInterface.load('data.bin')
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
    for w in wavs:
        sample_rate, signal = read_wav(os.path.join(predict_sound_path, w))
        label = os.path.splitext(w)[0]
        label2, score=m.predict(sample_rate, signal)
        print(label , '->',label2 ,'->' , score)

if __name__ == "__main__":
    choice = 'y'
    while choice == 'y' :
        task=input('Enter the task... \n'
                   '1. Enroll: enroll the wav files in the trainSounds directory.\n'
                   '2. Predict: Recognize the speaker of the wav files in predict sounds directory\n'
                   'Enter "enroll" to enroll and "predict" to predict.\n')

        if task == 'enroll' :
            task_enroll()
            choice= input('Do you want to continue using? (y/n)')
        elif task == 'predict' :
            task_predict()
            choice = input('Do you want to continue using? (y/n)')
        else :
            print('Invalid choice... Enter again...')
            continue

