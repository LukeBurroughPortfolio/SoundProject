#listen to the voice of person using it

#imports: speech recognition, text to speech, url magic, media streamer
import speech_recognition as sr
import pyttsx3
import pafy
#import vlc


#sets defult values
engine = pyttsx3.init()
r = sr.Recognizer()
Done = False

def GetVoice():
    # Record Audio
    with sr.Microphone() as source:
        print("calabrating microphone")
        r.adjust_for_ambient_noise(source, duration=3)
        print("Say something!")
        global audio
        audio = r.listen(source)

    try:
        print("you said: " + r.recognize_google(audio))
        global command
        command=r.recognize_google(audio)
        return
    except sr.UnknownValueError:  
        print("I couldnt understand you")
        return
    except sr.RequestError as e:  
        print("error; {0}".format(e))
        return

while Done != True:
    command="*"
    GetVoice()
    if 'computer' in command:
        if 'shutdown' in command:
            engine.say("Shutting down")
            engine.setProperty('rate',120)  #120 words per minute
            engine.setProperty('volume',0.9) 
            engine.runAndWait()
            Done = True
        elif 'Dad' in command:
            engine.say("daddy")
            engine.setProperty('rate',120)  #120 words per minute
            engine.setProperty('volume',0.9) 
            engine.runAndWait()
            Done = False
        else:
            Done = False
    else:
        Done = False


    
    

