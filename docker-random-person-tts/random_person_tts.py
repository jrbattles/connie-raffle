import random
import time
from gtts import gTTS
import os

# Open the text file containing the list of people
with open('people.txt', 'r') as file:
    people_list = file.read().splitlines()

mytext01 = "I am scrambling the list of attendees now."

time.sleep(3)  # Add a delay of 3 seconds for suspense
mytext02 = "And I am randomizing again based on quantum conditions."
mytext03 = "Thinking."
mytext04 = "ok"
mytext05 = "The randomly selected person is."
# Randomly select a person from the list
#random_person = random.choice(people_list)

# Print the randomly selected person
#mytext06 = ("The randomly selected person is: {random_person}")

time.sleep(2)  # Add a delay of 1 second for suspense

# Language in which you want to convert
language = 'en'

# Passing the text and language to the engine,
# here we have marked slow=False. Which tells
# the module that the converted audio should
# have a high speed
myobj = gTTS(text=mytext01, lang=language, slow=False)

# Saving the converted audio in a mp3 file named
# welcome
myobj.save("text01.mp3")

# Playing the converted file
os.system("mpg321 text01.mp3")