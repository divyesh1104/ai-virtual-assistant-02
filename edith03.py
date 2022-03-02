from cgitb import text
from socket import timeout
from typing_extensions import Self
import pywhatkit as kit
import datetime
import pyttsx3
import speech_recognition  as sr
import os
import webbrowser
import time
import pyautogui
from requests import get
import wikipedia
import sys
import flask 
import PyPDF2
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from edithui import Ui_edith



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 140)


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


def wish():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<=12:
        speak("good moring sir")
    elif hour>12 and hour<18:
        speak("good afternoon sir")
    else:
        speak("good evening sir")
    speak("i am edith. version 2 point o. please tell me how can i help you")  

def pdf_reader():
    book = open('py3.pdf','rb')
    pdfReader = PyPDF2.PdfFileReader(book)
    pages = pdfReader.numPages
    speak(f"Total numbers of pages in This book {pages}")
    speak("sir please enter the page number i have to read")
    pg = int(input("please enter the page number: "))
    page = pdfReader.getPage(pg)
    text = page.extractText()
    speak(text) 

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=5,phrase_time_limit=20)

    try:
        print("recognizing....")
        Self.query = r.recognize_google(audio, language='en-in')
        print(f"user said: {Self.query}")

    except Exception as e:
        speak("say that again please....")
        return "none"
        Self.query = Self.query.lower()    
        return Self.query 

class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()

    def run(self):
        self.TaskExecution()        



    def TaskExecution():

        Self.self.query = takecommand()

        if "open notepad" in Self.query:
            npath = "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(npath)

        elif "open command prompt" in Self.query:
            os.system("start cmd")  

        elif "open facebook" in Self.query:
            webbrowser.open("facebook.com") 

        elif "open whatsapp" in Self.query:
            webbrowser.open("whatsapp.com") 

        elif "open instagram" in Self.query:
            webbrowser.open("instagram.com")   


        elif 'switch the window' in Self.query:
            pyautogui.keydown("alt") 
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyup("alt")    


        elif 'open youtube' in Self.query:
            webbrowser.open("youtube.com")

        elif "close notepad" in Self.query:
            speak("okay sir, closing notepad")
            os.system("taskkill /f /im notepad.exe")    

        elif 'open google' in Self.query:
            speak("sir, what i search on google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")



        elif 'time' in Self.query:
            strtime = datetime.datetime.now().strftime("%h:%m:%S")
            speak(f"sir, the time is {strtime}")


        elif "take screenshot" in Self.query or "take a screenshot" in Self.query:
            speak("sir, please tell me the name for this screenshot file")
            name = takecommand().lower()
            speak("please sir hold the screen for few seconds, i am taking screenshot")
            time.sleep(3)
            img = pyautogui.screenshot()
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("i am done sir, the screenshot is saved in our main folder. now i am ready for next command")         


        elif "temperature" in Self.query:

            search = "temperature in surat"
            url = f"https://www.google.com/search?q={search}"
            r = "requests".get(url)
            data = "beautifulsoup"(r.text,"html.parser")
            temp = data.find("div",class_="BNewe").text
            speak(f"current {search} is {temp}")



        elif "shut down the system" in Self.query:
            os.system("shutdown /s /t 5")

        elif "restart the system" in Self.query:
            os.system("shutdown /r /t 5")

        elif "ip address" in Self.query:
            ip = get('https://api.ipify.org').text
            speak(f"your ip address is {ip}")

        elif "wikipedia" in Self.query:
            speak("searching wikipedia.... ")
            Self.query = Self.query.replace("wikipedia", "")
            results = wikipedia.summary(Self.query, sentences=4)
            speak("according to wikipedia")
            speak(results)
            print(results)

        elif "play song on youtube" in Self.query:
            kit.playonyt("Bilionera - Otilia")            


        elif "no thanks" in Self.query:
            speak("thanks for using me sir, have a good day.")
            sys.exit()

        speak("sir, do you have any other work")  

startExecution = MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_edith()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("../Gui/7LP8.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.Qtmovie("../Gui/VID-1608093668227.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = timeout.connect(self.showTime) 
        timer.start(0)   
        startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)

app = QApplication(sys.argv)
edith = Main()
edith.show()
exit(app.exec())            



if __name__ == "__main__":
    wish()
    while True:
        Self.query = takecommand()