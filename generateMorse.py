import matplotlib.pyplot as plt
import numpy as np
from scipy.io.wavfile import write

f = 400
fs = 22050
unit = 0.1

MORSE_CODE_DICT = {'A': '.-',
                   'B': '-...',
                   'C': '-.-.',
                   'D': '-..',
                   'E': '.',
                   'F': '..-.',
                   'G': '--.',
                   'H': '....',
                   'I': '..',
                   'J': '.---',
                   'K': '-.-',
                   'L': '.-..',
                   'M': '--',
                   'N': '-.',
                   'O': '---',
                   'P': '.--.',
                   'Q': '--.-',
                   'R': '.-.',
                   'S': '...',
                   'T': '-',
                   'U': '..-',
                   'V': '...-',
                   'W': '.--',
                   'X': '-..-',
                   'Y': '-.--',
                   'Z': '--..',
                   '1': '.----',
                   '2': '..---',
                   '3': '...--',
                   '4': '....-',
                   '5': '.....',
                   '6': '-....',
                   '7': '--...',
                   '8': '---..',
                   '9': '----.',
                   '0': '-----',
                   ', ': '--..--',
                   '.': '.-.-.-',
                   '?': '..--..',
                   '/': '-..-.',
                   '-': '-....-',
                   '(': '-.--.',
                   ')': '-.--.-',
                   ' ': '/'}


def charToWave(c):
    out = None
    if c == '.':
        out = np.sin(2 * np.pi * f * np.arange(0, unit, step=1 / fs))
        out = np.concatenate((out, np.zeros(int(fs * unit))), axis=0)

    elif c == '-':
        out = np.sin(2 * np.pi * f * np.arange(0, unit * 3, step=1 / fs))
        out = np.concatenate((out, np.zeros(int(fs * unit))), axis=0)
    elif c == ' ':
        out = np.zeros(int(fs * unit * 3))
    elif c == '/':
        out = np.zeros(int(fs * unit * 7))
    return out


sentence = input('Input a sentence: ')
sentence = sentence.upper()
morse = ""
for c in sentence:
    morse += MORSE_CODE_DICT[c]
    if c != ' ':
        morse += ' '
data = np.array([])
for c in morse:
    data = np.concatenate((data, charToWave(c)), axis=0)

plt.plot(data)
plt.show()
write('WAV Files/out.wav', fs, data)
