#listen to the voice of person using it

#imports speech and tts
import speech_recognition as sr
import pyttsx3
import re

#sets defult values
engine = pyttsx3.init()
r = sr.Recognizer()
regex = re.compile('computer .')
command="place holder"
Done = False

def GetVoice():
    # Record Audio
    with sr.Microphone() as source:
        print("calabrating microphone")
        r.adjust_for_ambient_noise(source, duration=5)
        print("Say something!")
        global audio
        audio = r.listen(source)

    try:
        print("you said :" + r.recognize_google(audio))
        return
    except sr.UnknownValueError:  
        print("I couldnt understand you")
        return
    except sr.RequestError as e:  
        print("error; {0}".format(e))
        return

while Done != True:
    GetVoice()
    command=r.recognize_google(audio)
    if 'computer' in command:
        if command == 'computer shutdown':
            engine.say("Shutting down")
            engine.setProperty('rate',120)  #120 words per minute
            engine.setProperty('volume',0.9) 
            engine.runAndWait()
            Done = True
        elif command == 'computer James':
            engine.say("daddyeeeeeeeeee")
            engine.setProperty('rate',120)  #120 words per minute
            engine.setProperty('volume',0.9) 
            engine.runAndWait()
            Done = False
        else:
            Done = False
    else:
        Done = False


    
    

