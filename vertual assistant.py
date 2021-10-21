import pyttsx3
import datetime
import speech_recognition as sr

import wikipedia as wiki
engine = pyttsx3.init()
voices = engine.getProperty("voices")
#print(voices[0].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    pass

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12 :
        speak("good morning ")
    elif hour>= 12 and hour < 18 :
        speak("good afternoon ")
    else:
        speak("good evening")
    speak("hello i am omee, your vertual assistance at your service . please tell me ,"
          " how may i help you ..?")
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening .... ")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("recognizing....")
        query = r.recognize_google(audio,language="en-in")
        print(f"user said ...{query}\n")
    except Exception as e:
        print("say that again please ...")
        return "none"
    return query

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 1
        audio = r.listen(source)
    try :
        print("Recognizing......")
        query = r.recognize_google(audio,language="en-in")
        print(f"User said {query} \n")
    except Exception as e:
        print("say that again please ....")
        return "None"
    return query




if __name__ =="__main__":
    #speak("my name is omee")
    #wishme()
    takecommand()