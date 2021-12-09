# from scipy.io import wavfile as wav
import re
import librosa
import os
import numpy as np
import argparse


# from generateMorse import MORSE_CODE_DICT

def list_to_string(s):
    # initialize an empty string
    str1 = ""

    # traverse in the string
    for ele in s:
        str1 += ele

        # return string
    return str1


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
                   ' ': '/',
                   '': ''
                   }

unit = 0.1

parser = argparse.ArgumentParser(description="Translates audio WAV File Morse signal to English alphabet")
parser.add_argument('filepath', type=str, help="Path of the WAV file")
parser.add_argument('-u', '--unit', type=float, help='dit duration in seconds')
args = parser.parse_args()
if args.unit:
    unit = args.unit
file_path = args.filepath

if not file_path.endswith('.wav'):
    raise Exception("Input must be a WAV file")
if not os.path.isfile(file_path):
    raise Exception("File " + file_path + " does not exist")

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
string = re.sub("[0-9]", "", string)

print(string)

# string.replace("/", " ")

list_of_words = string.split("/")
key_list = list(MORSE_CODE_DICT.keys())
val_list = list(MORSE_CODE_DICT.values())

sentence = []

for word in list_of_words:
    letters = word.split(" ")
    for letter in letters:
        position = val_list.index(letter)
        sentence.append(key_list[position])
        # print(key_list[position])
    sentence.append(" ")
sentence.pop(-1)

sentence = list_to_string(sentence)

print(sentence)
print(list_of_words)

# print(code)
