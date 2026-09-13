import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')

print("Available voices on your system:")
for index, voice in enumerate(voices):
    print(f"Index {index}: {voice.name}")