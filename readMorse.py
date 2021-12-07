# from scipy.io import wavfile as wav
import re

import librosa
import numpy as np

unit = 0.1
data, rate = librosa.load('WAV Files/Hello Friend.wav', mono=True)
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
