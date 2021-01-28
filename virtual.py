import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
from ecapture import ecapture as ec
import wolframalpha
import json
import requests
import pywhatkit
import ctypes
import smtplib


print('Loading your AI personal assistant - REYNA')

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[1].id')


def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello,Good Morning")
        print("Hello,Good Morning")
    elif hour>=12 and hour<18:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
        return statement


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()

    # Enable low security in gmail
    server.login('mayhem7999@gmail.com', 'NITHISATHI0708')
    server.sendmail('your email id', to, content)
    server.close()

speak("Loading your AI personal assistant REYNA")
wishMe()





if __name__=='__main__':


    while True:
        speak("Tell me how can I help you now?")
        statement = takeCommand().lower()
        if statement==0:
            continue

        if "good bye" in statement or "ok bye" in statement or "stop" in statement:
            speak('your personal assistant REYNA is shutting down,Good bye')
            print('your personal assistant REYNA is shutting down,Good bye')
            break



        if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement =statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            time.sleep(0)

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open now")
            time.sleep(0)

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail open now")
            time.sleep(0)

        elif "weather" in statement:
            api_key="8ef61edcf1c576d65d836254e11ea420"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("whats the city name")
            city_name=takeCommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

            else:
                speak(" City Not Found ")



        elif 'time' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        elif 'who are you' in statement or 'what can you do' in statement:
            speak('Im REYNA and im here to help and assist you')


        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by Nithissh")
            print("I was built by Nithissh")

        elif "open stackoverflow" in statement:
            webbrowser.open_new_tab("https://stackoverflow.com/login")
            speak("Here is stackoverflow")

        elif 'news' in statement:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')
            time.sleep(0)

        elif "camera" in statement or "take a photo" in statement:
            ec.capture(0,"robo camera","img.jpg")

        elif 'search'  in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(0)

        elif 'ask' in statement:
            speak('I can answer to computational and geographical questions and what question do you want to ask now')
            question=takeCommand()
            app_id="R2K75H-7ELALHR35X"
            client = wolframalpha.Client('R2K75H-7ELALHR35X')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)

        elif 'college' in statement or 'my college website' in statement:
            speak('here is your college website')
            webbrowser.open_new_tab("https://gurunanakcollege.edu.in")
            time.sleep(0)

        elif 'open steam' in statement or 'steam' in statement:
            speak('opening steam , enjoy gaming')
            codePath= "E:\\STEAM\\steam.exe"
            os.startfile(codePath)

        elif 'play ' in statement:
            song = statement.replace('play', '')
            speak('playing ' + song)
            pywhatkit.playonyt(song)
            time.sleep(0)

        elif 'what is' in statement:
            answer = statement
            speak('searching about' + answer)
            pywhatkit.info(answer)
            speak("Here is the result!")
            time.sleep(0)

        elif 'send a mail' in statement:
                speak("What should I say?")
                content = takeCommand()
                speak("whom should i send")
                to = input()
                sendEmail(to, content)
                speak("email sent successfully")


        elif "open instagram" in statement:
            webbrowser.open_new_tab("https://instagram.com")
            speak("Here is Instagram")

        elif 'take a note for me' in statement or 'make a reminder' in statement:
            speak("Please Proceed")
            rememberMessage = takeCommand()
            speak("you said me to remember" + rememberMessage)
            remember = open('E:\\NOTES.txt', 'w')
            remember.write(rememberMessage)
            remember.close()

        elif 'speak my notes' in statement or 'remind me' in statement:
            remember = open('E:\\NOTES.txt', 'r')
            speak("you said me to remember that" + remember.read())

        elif 'date' in statement or 'can we have date' in statement:
            speak('sorry i have boyfriend')
            print('sorry i have boyfriend')

        elif "calculate" in statement.lower():

            app_id = "R2K75H-7ELALHR35X"
            client = wolframalpha.Client('R2K75H-7ELALHR35X')

            indx = statement.split().index('calculate')
            query = statement.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            speak("The answer is " + answer)
            print("The answer is " + answer)

        elif 'change the wallpaper' in statement or 'desktop' in statement:
            speak("Changing Your Wallpaper")
            ctypes.windll.user32.SystemParametersInfoW(20, 0, "X://wallpaper.png", 0)


        elif  "log off" in statement or "sign out" in statement:
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])

        elif 'lock window' in statement or 'lock' in statement:
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()

        elif 'shutdown system' in statement or 'poweroff' in statement:
            speak("Hold On a Sec ! Your system is on its way to shut down")
            subprocess.call('shutdown / p /f')

        elif "restart" in statement:
            subprocess.call(["shutdown", "/r"])



time.sleep(0)












