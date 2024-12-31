import pyttsx3
import speech_recognition as sr
import random
import webbrowser
import datetime
from plyer import notification
import pyautogui
import wikipedia
import pywhatkit as pwk

engine = pyttsx3.init()
voices = engine.getProperty('voices')       #getting details of current voice
engine.setProperty('voice', voices[0].id)  
engine.setProperty('rate', 150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def command():
    content = " "
    while content == " ":
        # obtain audio from the microphone
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)
            
        try:
            content = r.recognize_google(audio, language='en-in')
            print("so you said : " + content)
        except Exception as e:
            print("Please try again...")
            content = " "  # **Corrected: Ensures content is reset on exception**
            
    return content 

def main_process():
    while True:  
        request = command().lower()
        if "hello" in request:
            speak("Hello sir, how can i help you...")
        elif "play music" in request:
            speak("Playing music")
            song = random.randint(1,5)
            if song == 1:
                webbrowser.open("https://www.youtube.com/watch?v=ZRJY0Xp_BuA")
            elif song == 2:
                webbrowser.open("https://www.youtube.com/watch?v=ekr2nIex040")
            elif song == 3:
                webbrowser.open("https://www.youtube.com/watch?v=bB3-CUMER")
            elif song == 4:
                webbrowser.open("https://www.youtube.com/watch?v=hbcGx4MGUMg")
            elif song == 5:
                webbrowser.open("https://www.youtube.com/watch?v=YudHcBIxlYw")
        elif "what is the time" in request:
            now_time=datetime.datetime.now().strftime("%H:%M")
            speak("The time is" + str(now_time))        
        elif "what is the date" in request:
            now_time=datetime.datetime.now().strftime("%d:%m")
            speak("The date is" + str(now_time))  
        elif "new task" in request:
            task = request.replace("new task", "")
            task = task.strip()
            if task != "":
                speak("Adding task..." + task)
                with open("todo.txt", "a") as file:
                    file.write(task + "\n")   
        elif "speak task" in request:
           with open("todo.txt", "r") as file:
               speak("The work we have to do today is : " + file.read())  
        elif "show work" in request:
            with open("todo.txt", "r") as file:  # **Added file open for reading tasks**
                tasks = file.read()              # **Assign tasks to the variable `tasks`**
            notification.notify(
                title = "Today's to do list",
                message = tasks                 # **Corrected: `messagw` to `message`**
            )
        elif "open" in request:
            query = request.replace("open","")
            pyautogui.press("super")
            pyautogui.typewrite(query)
            pyautogui.sleep(2)
            pyautogui.press("enter")
        elif "wikipedia" in request:
            request = request.replace("jarvis","")
            request = request.replace("search wikipedia","")
            print("Your command :    ", request)
            result = wikipedia.summary(request, sentences=3)
            print(result)
            speak(result)
        elif "search on google" in request:
            request = request.replace("jarvis", "")
            request = request.replace("search on google", "")
            webbrowser.open("https://www.google.com/search?q="+request)
            speak("Here's your result")
        elif "send whatsapp" in request:
            pwk.sendwhatmsg("+917984397799", "HIII", 17, 12)

            
        
main_process()
