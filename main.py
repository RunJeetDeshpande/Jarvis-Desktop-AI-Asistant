import pyttsx3

import speech_recognition as sr
import datetime 
import os
import wikipedia
import webbrowser
from PyQt5 import QtWidgets ,QtCore ,QtGui
from PyQt5.QtCore import QTimer ,QTime ,QDate ,Qt
from  PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from  PyQt5.QtGui import *
from  PyQt5.QtWidgets import *
from  PyQt5.uic import loadUiType
from project import Ui_MainWindow
import sys as sys
import subprocess
import pyjokes
from requests import get




engine =pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice',voices[0].id)



def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()
    
    
    


def wish():
    hour= int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("good morning")
    elif hour>12 and hour<18:
        speak("good afteroon")
    else:
        speak("good evening")
    speak("hello i am jarvis , i am here to help you sir ")
    
    

        
        


             
             
class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()
        
    def run(self):
        self.TaskExecution()
        
    def takecommand(self):
        r=sr.Recognizer()
        with sr.Microphone() as source:
            print("listening")
            r.pause_threshold =1
            audio=r.listen(source,timeout=10 ,phrase_time_limit=5)
        try:
            print("Recognixing")
            query=r.recognize_google(audio, language= 'en=in')
            print(f"user said : {query}")
        
        except Exception as e:
            speak("say that again please.....")
            return "none"
        return query
       
    
    def TaskExecution(self):
        
        wish()
       
        while True:
        
            
            self.query= self.takecommand().lower()
            
            if "open notepad"  in self.query:
                path= "C:\\WINDOWS\\system32\\notepad.exe"
                os.startfile(path)
                
            elif 'who is' in self.query:
                speak("seraching .......")
                query1 = self.query.replace("who is", " ")
                #query1 = self.query.replace("search for", " ")
                
                result = wikipedia.summary(query1, sentences=2)
                #speak("Accroding to wikipedia")
                speak(result)
                
            elif 'open youtube' in self.query:
                speak("about what you want to search on youtube")
                s = self.takecommand()
                webbrowser.open("www.youtube.com/results?search_query=" + s + "")
                
            elif 'who is' in self.query:
                webbrowser.open(self.query)
                
            elif "google" in self.query:
                speak("what should i search in google")
                cm = self.takecommand().lower()
                webbrowser.open(f"{cm}")
                

            elif 'help me' in self.query:
                speak("offcourse  ! how can i help you ")
                speak('question !')
                s = self.takecommand()
                print(s)
                speak(
                    "There are 3 thing that i can do for you sir i can search for it on google or youtube or wikipedia")
                speak("where i should to serach ")
                s1 = self.takecommand().lower()
                if s1 == 'google':
                    speak("opening  google !")
                    webbrowser.open(
                        "www.bing.com/search?q=" + s + "=9d02b0a92caa4bc895c28ea9269d27e6&FORM=ANAB01&PC=ASTS")

                elif s1 == 'youtube' in self.query:
                    speak("opening youtube!")
                    webbrowser.open("www.youtube.com/results?search_query=" + s + "")

                elif s1 == 'wikipedia' in self.query:
                    speak("Accroding to wikipedia")
                    result = wikipedia.summary(s, sentences=2)
                    
            elif 'shutdown' in self.query or 'sleep my' in self.query:
                speak("shutting down ")
                os.system("shutdown /h")

            elif "restart" in self.query:
                os.system('shutdown /r')
                
            elif  "exit" in self.query:
                 print("hi")
                 
            elif "weather" in self.query:
                speak(" City name ")
                print("City name : ")
                city_name = self.takecommand()
                webbrowser.open("https://www.accuweather.com/en/in/" + city_name + "/189231/weather-forecast/189231")
                speak("opening wether for")
                speak(city_name)


            elif 'girl' in self.query:
                speak("i would recommend you to stay away from girls")


            elif 'open calculator'in self.query:
                speak("open the calculator")
                subprocess.Popen("C:\\Windows\\System32\\calc.exe")

            elif 'tell me a joke' in self.query:
                joke = pyjokes.get_joke()
                speak(joke)

            elif 'play music' in self.query:
                music_dir = 'E:\\songs'
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir, songs[0]))

            elif 'ip address' in self.query:
                ip = get('https://api.ipify.org').text
                speak(f"your ip address is{ip}")
                print(ip)
            

             



startExecution = MainThread()

           
class Main(QMainWindow)  :
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.INITIATE.clicked.connect(self.startTask)
        
    def startTask(self):
        self.ui.movie=QtGui.QMovie(r"C:\Users\HP\Documents\Downloads\AI gif\AI gif\background.jpg")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
     
        self.ui.movie=QtGui.QMovie(r"C:\Users\HP\Documents\Downloads\AI gif\AI gif\jarvis23.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        
        self.ui.movie=QtGui.QMovie(r"C:\Users\HP\Documents\Downloads\AI gif\AI gif\wave.gif")
        self.ui.label_3.setMovie(self.ui.movie)
        self.ui.movie.start()
        
        self.ui.movie=QtGui.QMovie(r"C:\Users\HP\Documents\Downloads\AI gif\AI gif\initiating.gif")
        self.ui.label_4.setMovie(self.ui.movie)
        self.ui.movie.start()
        #timer =QTimer(self)
        #timer.timeout.connect(self.showTime)
        #timer.start(1000)
        
        
        startExecution.start()
        


app = QtWidgets.QApplication(sys.argv)
jarvis=Main()
jarvis.show()
sys.exit(app.exec_())

        
        
    
    