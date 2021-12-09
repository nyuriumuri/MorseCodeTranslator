# Digital Signal Processing Project

- [Digital Signal Processing Project](#digital-signal-processing-project)
  - [Morse Code Translator](#morse-code-translator)
    - [Introduction](#introduction)
    - [Problem Specification](#problem-specification)
    - [Data](#data)
    - [Evaluation Criteria](#evaluation-criteria)
    - [Approach](#approach)
    - [Results and Analysis](#results-and-analysis)
    - [Development](#development)
    - [Usage Documentation](#usage-documentation)
      - [To convert a sentence to Morse](#to-convert-a-sentence-to-morse)
      - [To convert a Morse WAV file to English](#to-convert-a-morse-wav-file-to-english)
    - [References](#references)

## Morse Code Translator

**Submitted by:**

- Mohamed Mansour
  - 900172822
  - [email](gurinucida@aucegypt.edu)
- Omar Elewa
  - 900140492
  - [email](elewa97@aucegypt.edu)

Supervised By:

- Dr. Nourhan Zayed
  - [email](n.zayed@aucegypt.edu)

### Introduction

Morse code is a method of encryption made possible by the invention of the telegraph that was used in telecommunication to decode standard English alphabet into a predefined translation of dashes and dots. The summary of the morse code can be seen in the diagram provided below.
International Morse Code is the standard most widely used, which is composed of letters from A-Z, with no distinction between uppercase and lowercase letters, in addition to a small set of punctuation marks and procedural signals.
![Morse Code](assets/mc.png)

### Problem Specification

The solution we aimed to provide is for the lack of availability of reliability of morse code translators, that's why we decided to provide a program that is capable of generating morse code wav files from inserted texts and vice versa.

### Data

The morse code we are translating from and into is carried on audio signals. Specifically, we are outputting WAV sound files that contain audio signals of frequency of 400Hz and a dit length of 0.1 seconds.

### Evaluation Criteria

Morse Decoder <sup>[1]</sup>  has options to translate morse code to and from text. Furthermore, it has an option to download the morse code as a WAV audio file. We used the website as a golden model for our project. When translating the alphabet to morse, we checked the resultant morse code against the code generated from the website. Likewise, when translating morse back to alphabet, we downloaded sample audio files from the website and checked if the outputted sentence matches the input from the website.

### Approach

In translating audio morse code to text, we divided the problem into four tasks.
First, we needed to split the audio file into fragments of dit-length each.
Next, we had to check if an audio signal was present at each fragment. To achieve so, we calculated the fourier transform at each fragment and obtained the maximum frequency in the interval. If the frequency exceeded a certain threshold, then a signal was present. Hence, we translated each fragment into either a ‘1’ or a ‘0’.  The result of this process was a string of 1’s and 0’s representing spaces, dits, and dahs.
Thirdly, we needed to convert the binary strings into meaningful morse code. To do so, we used regular expressions to convert ‘1110’s to dashes, ‘10’s to dots, ‘0000000’ to ‘/’ (representing spaces between words), and ‘000’s to spaces between letters.  Finally, we converted each space-separated sequence to the corresponding English letter by using a pre-defined dictionary.
In translating text to morse code, we converted each letter in the input string to its corresponding morse code.
Once we obtained the string of dots and dashes, we created an empty array representing the data of the output audio signal. We then looped over each character in the morse string and appended into the array of the audio signal the equivalent of sine wave values. For example, upon reaching a dot, we append _f<sub>s</sub>_ &times; unit many _sin(2f<sub>n</sub>)_ values followed by _f<sub>s</sub>_ &times; unit zeroes, where _f<sub>s</sub>_ = sample frequency of the audio signal,  unit = length of the dit in seconds, and _f_ =  frequency of the sine wave. _f<sub>s</sub>_ , _unit_, and _f_ are all arbitrary predefined constants. We chose _f<sub>s</sub>_ = 22050, unit = 0.1, and f = 400Hz.
Once we looped through all the morse characters, we generated a WAV using the generated data and the predefined _f<sub>s</sub>_.

### Results and Analysis

All our generated test cases created morse code that was correctly translated on Morse Decoder. Likewise, all downloaded audio files from Morse Decoder were translated correctly.

### Development

We have 2 main programs and a file containing a dictionary that were implemented using python programming language:

- readMorse.py
  - Reads morse code wav file and converts it to its spring representation.
- generateMorse.py
  - Takes a string and converts it into a morse code and stores it into a wav file.
- alpha_morse.py
  - Contains the dictionary required to do any translation procedures.

These 2 files were implemented with the aid of a couple of external python packages:

- re
  - `import re`
  - To provide regular expressions matching operations that can be useful in the translation process.
- librosa
  - `import librosa`
  - To provide extra functions and methods that can be handy in audio and musical analysis
- os
  - `import os`
  - To provide the ability to use operating system dependent functionalities such as files accessing.
- numpy
  - `import numpy as np`
  - Important in any python program that requires scientific computing
- matplotlib.pyplot
  - `import matplotlib.pyplot as plt`
  - To help with plotting and viewing graphs
- scipy
  - `from scipy.io.wavfile import write`
  - Provides the necessary algorithms for scientific computation
- argparse
  - `import argparse`
  - For an easier way to add the functionality of being executed from the command line, and parse arguments.

### Usage Documentation

#### To convert a sentence to Morse

```bash
python3 generateMorse.py <sentence>
```

For example:

>```bash
>python3 generateMorse.py 'Good Morning!'
>```
>
>>This will generate the morse code `--. --- --- -.. /-- --- .-. -. .. -. --. -.-.--` and the WAV file `wav/Good Morning!.wav`.

#### To convert a Morse WAV file to English

```bash
 python3 readMorse.py <wavfile>
```

For example:

>```bash
> python3 readMorse.py 'wav/Good Morning!.wav'
>```
>
>>```bash
>>--. --- --- -../ -- --- .-. -. .. -. --. -.-.--
>>GOOD MORNING!
>>```

### References

1. “Morse Code Translator | Morse Decoder,” Morse Code Translator | Morse Decoder. [link](https://morsedecoder.com) (accessed Dec. 09, 2021).
2. "International Morse Code, Hand Sending", Nuclear Vault. [link](https://www.youtube.com/watch?v=R-petiNdCIY)