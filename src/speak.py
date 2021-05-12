import datetime
from playsound import playsound
import glob, os
from gtts import gTTS
 
def cleartmp ():
  for file in glob.glob("tmp/*.mp3"):
    	os.remove(file)
 
def speak (message=""):
  res = gTTS(message)
  if not os.path.exists('tmp'): os.mkdir('tmp')
  fileName = "tmp/" + str(datetime.datetime.now()).replace(" ", "_") + "-tts-audio.mp3"
  res.save(fileName)
  playsound(fileName)
  cleartmp()
  