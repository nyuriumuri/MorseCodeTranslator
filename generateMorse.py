import argparse

import matplotlib.pyplot as plt
import numpy as np
from scipy.io.wavfile import write

import alpha_morse


def check_substring(string, sub_str):
    if string.find(sub_str) == -1:
        return False
    else:
        return True


f = 400
fs = 22050
unit = 0.1


def char_to_wave(c):
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


parser = argparse.ArgumentParser(description='Converts the input sentence to a Morse WAV file')
parser.add_argument('sentence', type=str)
args = parser.parse_args()
sentence = args.sentence
# print(type(sentence))
# if check_substring(sentence, ", "):
#     sentence = sentence.replace(", ", ",")

sentence = sentence.upper()
morse = ""

for c in sentence:
    morse += alpha_morse.MORSE_CODE_DICT[c]
    if c != ' ':
        morse += ' '
data = np.array([])
print(morse);
for c in morse:
    data = np.concatenate((data, char_to_wave(c)), axis=0)

plt.plot(data)
plt.show()

sentence = sentence.title()

output_file_name = "wav/" + sentence + ".wav"

write(output_file_name, fs, data)
