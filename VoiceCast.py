from gtts import gTTS
from playsound import playsound

audio = "speech.mp3"
language = 'en'
sp = gTTS(text="Hello, I'm Ram, A full-stack developer from India",
          lang=language, slow=False)
sp.save(audio)
playsound(audio)
print("===Audio is playing===")
