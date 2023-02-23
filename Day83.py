# In this we have write a code for pronouncing the name from list using win32package


import pyttsx3
# initialize Text-to-speech engine
engine = pyttsx3.init()
# convert this text to speech
text = ["Amit","AAmit","Misti","Ashis","Rohan"]
for name in text:
    engine.say(f"Shoutout to {name}")
    engine.runAndWait()





