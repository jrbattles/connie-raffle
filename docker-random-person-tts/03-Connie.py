# Import the required module for text
# to speech conversion
from gtts import gTTS

# This module is imported so that we can
# play the converted audio
import os
import time

# The text that you want to convert to audio
mytext = "My formal name is Connie the Containerized Tech Crusader. I was created to add a little technical flavor and inject some fun into our team events.  I am not yet as smart and capable as my big sister Clara, but SHE does not have a cool helmet and sword..  I have aspirations to join our team activities, perhaps starting with our Content Creation and Form Your Own Opinion workstreams..  At the end of today's meeting, I also have been tasked with randomly selecting a raffle winner, so that will be fun."
mytextb = "Hey James, I even have a joke for you.  How many digital humans does it take to change a light bulb?"

# Language in which you want to convert
language = 'en'

# Passing the text and language to the engine,
# here we have marked slow=False. Which tells
# the module that the converted audio should
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False)
myobj2 = gTTS(text=mytextb, lang=language, slow=False)

# Saving the converted audio in a mp3 file named
# welcome
myobj.save("03-Connie.mp3")
myobj2.save("03-Connie-joke.mp3")

# Playing the converted file
os.system("mpg321 03-Connie.mp3")
time.sleep(5) 
os.system("mpg321 03-Connie-joke.mp3")