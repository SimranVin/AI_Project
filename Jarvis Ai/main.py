from urllib import response
import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary ##file
import requests
#for openai
import google.generativeai as genai
import os
 
##Global variables
recognizer = sr.Recognizer()  #it is to get speech recognition functionality
engine = pyttsx3.init() # to intialize pyttsx3(text to speech convert lib)
newsapi ="3b7184521de14ca4960acddcaaa9bae6"

def speak(text):
    engine.say(text)
    engine.runAndWait()


# for opennai
def aiProcess(command):
    genai.configure(api_key="AIzaSyBuUxLkJZ4WU-Ny6cVNc_PkNxBYObxXGYc")

    model = genai.GenerativeModel('gemini-1.5-flash')

    response = model.generate_content(command)    

    print(response.text)



def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif c.lower().startswith("play"): ## if user wants to play song
        song = c.lower().split(" ")[1] ##if command is "play song" then it will convert it into a list ..
                                       ##..like ['play','song'] and [1] means it will read the name of the song
        link = musicLibrary.music[song]
        webbrowser.open(link)

    elif "news"  in c.lower():   ##To speak title of the news
        r=requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code== 200:
            #parse the JSON response
            data =r.json()

            #Extract articles
            articles = data.get('articles',[])

            #print the headlines
            for article in articles:
                speak(article['title'])

    else:
        #Let open AI Integration/handle the request
        output =aiProcess(c)
        speak(output)



if __name__ == "__main__":
    speak("Intializing Jarvis ..........")
    while True:
        #Listen for the wake word "Jarvis"
        #Obtain audio from the microphone
        r = sr.Recognizer()
        
        
        try:
            with sr.Microphone() as source:
                print("Listening.....")
                audio = r.listen(source,timeout=2,phrase_time_limit=1)
                print("recognization...")
                ##Recognize speech using Sphinx
            #command =r.recognize_sphinx(audio)  ##sphinx doesn't take perfect input
            word =r.recognize_google(audio) 
            if(word.lower() =="jarvis" ):
                speak("Say Queen")
                ##to listen next command
                with sr.Microphone() as source:
                    print("Jarvis Active....")
                    speak("Jarvis Activating....")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)

            
        except Exception as e:
            print("Error;{0}".format(e))