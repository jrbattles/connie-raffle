import random
import time
# Import the required module for text
# to speech conversion
from gtts import gTTS

# This module is imported so that we can
# play the converted audio
import os

# Open the text file containing the list of people
with open('people.txt', 'r') as file:
    people_list = file.read().splitlines()

random_person = random.choice(people_list)

# The text that you want to convert to audio
mytext00 = "It is time to select our Tech Crusaders Funstream Raffle Winner."
mytext01 = "I have created a list of all attendees.  I am scrambling this list now."
mytext02 =  "And now I am randomizing again based on quantum conditions."
mytext03 =  "The randomly selected winner is "
mytext04 = random_person

# Language in which you want to convert
language = 'en'

# Passing the text and language to the engine,
# here we have marked slow=False. Which tells
# the module that the converted audio should
# have a high speed
myobj = gTTS(text=mytext00, lang=language, slow=False)

# Saving the converted audio in a mp3 file named
# welcome
myobj.save("mytext00.mp3")

# Playing the converted file
os.system("mpg321 mytext00.mp3")
time.sleep(1)

myobj = gTTS(text=mytext01, lang=language, slow=False)
myobj.save("mytext01.mp3")
os.system("mpg321 mytext01.mp3")
time.sleep(1)

myobj = gTTS(text=mytext02, lang=language, slow=False)
myobj.save("mytext02.mp3")
os.system("mpg321 mytext02.mp3")
time.sleep(1)

myobj = gTTS(text=mytext03, lang=language, slow=False)
myobj.save("mytext03.mp3")
os.system("mpg321 mytext03.mp3")
time.sleep(3)

myobj = gTTS(text=mytext04, lang=language, slow=False)
myobj.save("mytext04.mp3")
os.system("mpg321 mytext04.mp3")