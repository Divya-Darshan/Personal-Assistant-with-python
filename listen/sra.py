from vosk import Model, KaldiRecognizer
import pyaudio

model = Model(r"ewe\\vosk-model-small-en-us-0.15")

sr = KaldiRecognizer(model,16000)

mic = pyaudio.PyAudio()
stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192 )
stream.start_stream()

while True:
    data = stream.read(4098)

    if sr.AcceptWaveform(data):
        t = sr.Result()
        print(t[14:-4])