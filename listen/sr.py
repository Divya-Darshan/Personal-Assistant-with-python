import speech_recognition as sr
import pyaudio

r= sr.Recognizer()
print("Running")

p = pyaudio.PyAudio()
for i in range(p.get_device_count()):
   print()

with sr.Microphone(1) as source:
    r.adjust_for_ambient_noise(source, 1)  # Adjust for ambient
    print("Say something!")
    audio=r.listen(source)
print("Runnnnnn")
try:
    print("Analyzing voice data  "+r.recognize_google(audio))
except Exception:
    print("Something went wrong")