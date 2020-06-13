from scipy.io import wavfile

def read_wav(name) :
    sample_rate, signal=wavfile.read(name)
    if len(signal.shape) != 1:
        print('File in stereo mode... converting to mono')
        signal =signal[:,0]
    return sample_rate, signal
