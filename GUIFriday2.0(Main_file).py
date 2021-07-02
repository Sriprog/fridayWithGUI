from fridayUi import Ui_FridayAI
from PyQt5 import QtCore,QtWidgets,QtGui
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUiType
import pyttsx3
import speech_recognition as sr
import pywhatkit as pywhatkit
import datetime
import os
import webbrowser
import random

import requests
from bs4 import BeautifulSoup
from googletrans import Translator
from playsound import playsound
import pyautogui
import whatsapp
from tkinter import Label
from tkinter import Entry
from tkinter import Button
from tkinter import Tk
from tkinter import StringVar
from pytube import YouTube
from PyDictionary import PyDictionary as Dictionary
from pywikihow import search_wikihow
from gtts import gTTS
import keyboard
import wikipedia
import sys
import smtplib
import pyjokes
import PyPDF2


friday = pyttsx3.init('sapi5')
voices = friday.getProperty('voices')
friday.setProperty('voice', voices[3].id)




def speak(audio):
    print("..................")
    friday.say(audio)
    print(f"Friday:{audio}")
    friday.runAndWait()


def OpenApps():
    speak("Ok boss, getting it from stark cloud!!")
    if 'open youtube' in query:
        speak("Opening youtube Boss")
        webbrowser.open("youtube.com")


    elif 'open google' in query:
        speak("Opening google")
        webbrowser.open("google.com")

    elif 'open facebook' in query:
        speak("Opening Facebook")
        webbrowser.open("facebook.com")

    elif 'open github' in query:
        speak("Opening Github")
        webbrowser.open("github.com")

    elif 'open code' in query:
        vscodePath = "C:\\Users\\Universe\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        speak("opening VS Code")
        os.startfile(vscodePath)

    elif 'open word' in query:
        wordPath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
        speak("opening MS Word!!")
        os.startfile(wordPath)

    elif 'open speed' in query.self():
        speak("opening speedtest")
        webbrowser.open("fast.com")

    elif 'open chrome' in query:
        chromePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        speak("Opening Chrome")
        os.startfile(chromePath)

    elif 'open spotify' in query:
        speak("opening spotify")
        webbrowser.open("spotify.com")
    speak("Your command is cooked and served.")

def CloseApp():
    speak("Ok boss,Wait a second!!")

    if 'chrome' in query:
        os.system("TASKKILL /F /im chrome.exe")

    if 'music' in query:
        os.system("TASKKILL /F /im Music.UI.exe")

def YoutubeAuto():
    speak("Whats Your Command?")
    comm = takeCommand()
    if 'pause' in comm:
        keyboard.press("space bar")

    elif 'restart' in comm:
        keyboard.press("0")

    elif 'mute' in comm:
        keyboard.press("m")

    elif 'skip' in comm:
        keyboard.press('l')

    elif 'back' in comm:
        keyboard.press('j')

    elif 'full screen' in comm:
        keyboard.press('f')

    elif 'Theater mode' in comm:
        keyboard.press('t')
    speak("Done sir")

def ChromeAuto():
    speak("Chrome Automation!!")
    comm = takeCommand()

    if "close this tab" in comm:
        keyboard.press_and_release('ctrl + w')

    elif 'open this tab' in comm:
        keyboard.press_and_release('ctrl + t')

    elif 'open new window' in comm:
        keyboard.press_and_release('ctrl + n')

    elif 'history' in comm:
        keyboard.press_and_release('ctrl + h ')

def Dict():
    speak("Opening dictionary!")
    speak("Tell me the word for search!!")
    word = takeCommand()

    if 'meaning' in word:
        word = word.replace("what is the", "")
        word = word.replace("friday","")
        word = word.replace("of", "")
        word = word.replace("meaning", "")
        result = Dictionary.meaning(word)
        speak(f"The Meaning for {word} is {result}")

    elif 'synonym' in word:
        word = word.replace("what is the", "")
        word = word.replace("friday","")
        word = word.replace("of", "")
        word = word.replace("synonym", "")
        result = Dictionary.synonym(word)
        speak(f"The Synonym for {word} is {result}")


    elif 'antonym' in word:
        word = word.replace("what is the", "")
        word = word.replace("friday","")
        word = word.replace("of", "")
        word = word.replace("antonym", "")
        result = Dictionary.antonym(word)
        speak(f"The Antonym for {word} is {result}")
    speak("Dictionary ended sir!!")

def TakeScreenShot():
    speak("Ok Boss,What Should I call it??")
    path = takeCommand()
    imgPath = path + ".png"
    path1 = "C:\\Users\\Universe\\Pictures\\Screenshots" + imgPath
    sc = pyautogui.screenshot()
    sc.save(path1)
    os.startfile("C:\\Users\\Universe\\Pictures")
    speak("Here is the snapshot captured!!")

def Temp():
    search = "temperature in kakinada"
    url = "https://www.google.com/search?q=" + search
    j = requests.get(url)
    data = BeautifulSoup(j.text,"html.parser")
    temperature = data.find("div",class_="BNeawe").text
    speak(f"The Temperature in kakinada is {temperature} outside")

def Reader():
    speak("Reading your book Sir!!")
    os.startfile("D:\\book\\Ethfrog.pdf")
    book = open("D:\\book\\Ethfrog.pdf",'rb')
    pdfReader = PyPDF2.PdfFileReader(book)
    pages = pdfReader.getNumPages()
    speak(f'Number of pages in this book are {pages}')
    speak(f'From which page I have To start Reading??')
    numPage = int(input())
    page = pdfReader.getPage(numPage)
    text = page.extractText()
    speak("Choose the language Sir!!")
    lang = takeCommand()

    if 'hindi' in lang.lower():
        trans1 = Translator()
        textHin = trans1.translate(text,'hi')
        textfile=textHin.text
        speech = gTTS(text=textfile)
        try:
            speech.save('book.mp3')
            playsound('book.mp3')
        except:
            playsound('book.mp3')
    else:
        speak(text)

def SpeedTest():
    import speedtest
    speak("checking speed....")
    playsound("Jarvis On.mp3")
    speed = speedtest.Speedtest()
    downloading = speed.download()
    correctDown = int(downloading/800000)
    uploading = speed.upload()
    correctUpload = int(uploading/800000)

    if 'uploading' in query:
        speak(f'The uploading Speed is {correctUpload} mbps')
    elif 'downloading' in query:
        speak(f'The downloading speed is {correctDown} mbps')
    else:
        speak(f'The Downloading speed is {correctDown} and the uploading speed is {correctUpload}')


class MainThread(QThread):

    def __init__(self):
        super(MainThread,self).__init__()


    def run(self):
        self.TaskGui()

    def takeCommand(self):
        '''Takes the microphone input as a string '''
        r = sr.Recognizer()
        with sr.Microphone() as source:

            print("Listening...")
            r.pause_threshold = 1
            r.energy_threshold = 700
            audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said:{query}\n")

        except Exception as e:
            # print(e)

            speak("I didn't catch you BOSS. Say it again please...")
            return "None"
        return query

    def TaskGui(self):
        hour = int(datetime.datetime.now().hour)
        if hour >= 0 and hour < 12:
            speak("Good Morning Sir!")


        elif (hour >= 12 and hour < 18):
            speak("Good Afternoon Sir!")

        else:
            speak("Good Evening Sir!")

        speak("I am friday. Your Personal Assistant. Lets rock and roll")
        speak("What can I do For you")
        while True:

            self.query = self.takeCommand()
            query = self.query.lower()

            if 'hello' in query:
                speak("Hello Sir, How are You?")

            elif 'whatsapp message' in query:
                speak("To whom should I send??")
                name = takeCommand()

                if 'Amma' in name:
                    num = "7794897284"
                    speak(f"Should I ping {name}??")
                    mess = takeCommand()
                    speak("specify time in hr")
                    hr = takeCommand()
                    speak("specify time in min")
                    min = takeCommand()
                    whatsapp.whatsapp(num, mess, hr, min)
                    speak("Message sent successfully")


                elif 'Akka' in name:
                    num = "6300133663"
                    speak(f"Should I ping {name}??")
                    mess = takeCommand()
                    speak("specify time in hr")
                    hr = takeCommand()
                    speak("specify time in min")
                    min = takeCommand()
                    whatsapp.whatsapp(num, mess, hr, min)
                    speak("Message sent successfully")


                elif 'family' in name:
                    gro = "FyBnZ79mevuJJ3uCPjJaeJ"
                    speak(f'What shall I send to group {gro}')
                    mess = takeCommand()
                    speak("specify time in hr")
                    hr = takeCommand()
                    speak("specify time in min")
                    min = takeCommand()
                    whatsapp.Whatsapp_Grp(gro, mess, hr, min)
                    speak("Message sent successfully")

            elif "message now" in query:
                speak("To whom should I send??")
                name = takeCommand()

                if 'Amma' in name:
                    num = "7794897284"
                    mess = takeCommand()
                    whatsapp.WhatsAppInstant(num, mess)
                    speak("Message sent successfully")


                elif 'Akka' in name:
                    num = "6300133663"
                    speak(f"Should I dm {name}??")
                    mess = takeCommand()
                    whatsapp.WhatsAppInstant(num, mess)
                    speak("Message sent successfully")

            elif 'hi friday' in query:
                speak("Hi Boss!!. I am friday")
                speak("How may I assist you?")

            elif "hello friday" in query:
                speak("Hello Boss!!. I am friday")
                speak("What can I do for you")

            elif "how are you" in query:
                speak("I am 1s and 0s")
                speak("whats about you boss?")

            elif "you need a break" in query:
                speak("ok boss, You can call me Anytime!")
                speak("Just say wake up Friday!!")
                break

            elif 'youtube search' in query:
                speak("Ok boss,I found this on youtube")
                query = query.replace("friday", "")
                query = query.replace("youtube search", "")
                ytUrl = "https://www.youtube.com/results?search_query=" + query
                webbrowser.open(ytUrl)
                speak("Done Boss")

            elif "website" in query:
                speak("Ok boss,Launching your request...")
                query = query.replace("friday", "")
                query = query.replace("website", "")
                web1 = query.replace("open", "")
                webUrl = "https://www." + web1 + ".com"
                webbrowser.open(query)
                speak("Done Boss")

            elif 'open google' in query:
                OpenApps()

            elif 'open youtube' in query:
                OpenApps()

            elif 'open facebook' in query:
                OpenApps()

            elif 'open github' in query:
                OpenApps()

            elif 'open code' in query:
                OpenApps()

            elif 'open word' in query:
                OpenApps()

            elif 'open speed' in query:
                OpenApps()

            elif 'open chrome' in query:
                OpenApps()

            elif 'open spotify' in query:
                OpenApps()

            elif 'close chrome' in query:
                CloseApp()

            elif 'stop music' in query:
                CloseApp()

            elif 'play music' in query:
                music_dir = 'E:\\Music\\songs'
                songs = os.listdir(music_dir)
                num = random.randint(0, len(songs))
                speak("Playing Music!!")
                os.startfile(os.path.join(music_dir, songs[num]))
                speak("Done Boss")

            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir,the time is {strTime}")
                speak("Done Boss")

startFunction = MainThread()

class Gui_Start(QMainWindow):
    def __init__(self):
        super().__init__()
        self.friday_ui_el = Ui_FridayAI()
        self.friday_ui_el.setupUi(self)

        self.friday_ui_el.StartBtn.clicked.connect(self.startFun)
        self.friday_ui_el.StopBtn.clicked.connect(self.close)

    def startFun(self):

        self.friday_ui_el.movies_1 = QtGui.QMovie("head.gif")
        self.friday_ui_el.aiHead.setMovie(self.friday_ui_el.movies_1)
        self.friday_ui_el.movies_1.start()

        self.friday_ui_el.movies_2 = QtGui.QMovie("alexa.gif")
        self.friday_ui_el.SmAi.setMovie(self.friday_ui_el.movies_2)
        self.friday_ui_el.movies_2.start()

        self.friday_ui_el.movies_3 = QtGui.QMovie("intial.gif")
        self.friday_ui_el.SysIn.setMovie(self.friday_ui_el.movies_3)
        self.friday_ui_el.movies_3.start()

        self.friday_ui_el.movies_4 = QtGui.QMovie("code.gif")
        self.friday_ui_el.dataAi.setMovie(self.friday_ui_el.movies_4)
        self.friday_ui_el.movies_4.start()

        self.friday_ui_el.movies_5 = QtGui.QMovie("wave.gif")
        self.friday_ui_el.waveai.setMovie(self.friday_ui_el.movies_5)
        self.friday_ui_el.movies_5.start()


        startFunction.start()

Gui_App = QApplication(sys.argv)
Gui_Friday = Gui_Start()
Gui_Friday.show()
exit(Gui_App.exec_())
