
import sys
import os
from vosk import Model, KaldiRecognizer
import pyaudio


current_dir = os.path.dirname(os.path.abspath(__file__))


utils_dir = os.path.join(current_dir, '../Speech')


sys.path.append(utils_dir)


from Say import say







model = Model(r"listen\\vosk-model-small-en-us-0.15")

sr = KaldiRecognizer(model,16000)

mic = pyaudio.PyAudio()
stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192 )
stream.start_stream()

while True:
    data = stream.read(4098)

    if sr.AcceptWaveform(data):
        r = sr.Result()
        t = r[14:-3]
        say(t)
        continue
