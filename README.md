# To convert a sentence to Morse

```
python3 generateMorse.py <sentence>
```
For example:
```bash
python3 generateMorse.py 'Good Morning!'
```
This will generate the morse code `--. --- --- -.. /-- --- .-. -. .. -. --. -.-.--` and the WAV file `wav/Good Morning!.wav`.

# To convert a Morse WAV file to English

```
 python3 readMorse.py <wavfile>
```
For example:

```bash
 python3 readMorse.py 'wav/Good Morning!.wav'
```
This will generate the following output:

```
--. --- --- -../ -- --- .-. -. .. -. --. -.-.--
GOOD MORNING!
```