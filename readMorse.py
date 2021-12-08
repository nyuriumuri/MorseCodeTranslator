# from scipy.io import wavfile as wav
import re
import librosa
import os
import numpy as np
from sys import platform

unit = 0.1


def get_file_relative_path():
    global file_path
    print("Please make sure that the file to be translated is in .wav format, and is located in WAV Files Input directory")
    file_name = input("Please enter file name:")
    file_path = 'WAV Files Input/' + file_name + '.wav'


while platform == 'darwin' or platform == 'linux' or platform == 'linux2':
    get_file_relative_path()
    if os.path.exists(file_path):
        data, rate = librosa.load(file_path, mono=True)
        interval = int(rate * unit)
        ranges = (np.arange(0, len(data), step=interval))
        fourier = [np.fft.fft(data[i:i + interval]) for i in ranges]
        max_f = [max(np.absolute(i)) for i in fourier]
        code = [1 if i > 50 else 0 for i in max_f]
        string = "".join([str(i) for i in code])

        dash = re.compile('1110')
        dot = re.compile('10')
        word = re.compile('0000000')
        letter = re.compile('000')

        string = dash.sub('-', string)
        string = dot.sub('.', string)
        string = word.sub('/', string)
        string = letter.sub(' ', string)

        print(string)
        print(code)
