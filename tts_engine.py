import pyttsx3
from gtts import gTTS
import os

def speak_text(text):
    try:
        # Try using gTTS first (more reliable)
        tts = gTTS(text=text, lang='en')
        tts.save("temp.mp3")
        os.system("mpg123 temp.mp3")
        os.remove("temp.mp3")
    except Exception as e:
        print(f"gTTS error: {str(e)}")
        try:
            # Fallback to pyttsx3
            engine = pyttsx3.init()
            engine.setProperty('rate', 160)
            engine.say(text)
            engine.runAndWait()
        except Exception as e:
            print(f"pyttsx3 error: {str(e)}")
            print("Text-to-speech failed. Skipping audio output.")
