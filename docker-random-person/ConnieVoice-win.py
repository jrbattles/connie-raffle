# Import the required module for text
# to speech conversion
from gtts import gTTS
from mpyg321.MPyg123Player import MPyg123Player # or MPyg321Player if you installed mpg321


# This module is imported so that we can
# play the converted audio
import os

# The text that you want to convert to audio
mytext = 'Hello Joe.  I am Connie the Containerized Tech Crusader.  Do you think we can be friends after you question the fairness of my raffle selections?  Hello Adam.  Do you think my voice sounds texy?'  

# Language in which you want to convert
language = 'en'

# Passing the text and language to the engine,
# here we have marked slow=False. Which tells
# the module that the converted audio should
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False)

# Saving the converted audio in a mp3 file named
# welcome
myobj.save("welcome.mp3")

# Playing the converted file
os.system("mpg321 welcome.mp3")
