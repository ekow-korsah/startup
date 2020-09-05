import speech_recognition as sr
import os
from gtts import gTTS
import datetime
import warnings
import calendar
import random
import wikipedia
from time import ctime
import webbrowser
import time
import playsound


file = open("myfile.txt", "w")

# Ignore any warning messages we might encounter in the programme
warnings.filterwarnings("ignore")


# record audio and return audio as string
def recordAudio(ask = False):
    r = sr.Recognizer()  ## creating a recognizer object
    with sr.Microphone() as source:
        if ask:
            assistantResponse(ask)

        # print("Say something")
        audio = r.listen(source)

    #     use Google speech recognition

        data = ""
        try:
            data = r.recognize_google(audio)
            print("You said: " + data)
            file.write(data)
        except sr.UnknownValueError:
            assistantResponse("Could not understand the audio, unknown error")
        except sr.RequestError as e:
            print("Request results from google speech recognition service error " + e)

        return data





def assistantResponse(text):
    print(text)
    # convert text to speech

    myobj = gTTS(text=text, lang="en", slow=False)
    #
    sound = "assistant_response.mp3"
    # # Save the converted audio to a file
    myobj.save(sound)

    # os.system("afplay assistant_response.mp3")
    playsound.playsound(sound)
    os.remove(sound)


# A function for wake words or phrase
def wakeWord(text):
    Wake_Words = ["hey Alexa", "okay Alexa", "computer", "alexa"]

    text = text.lower()

    # Check to see if users command contains a wake word
    for phrase in Wake_Words:
        if phrase in text:
            return True

    return False


# A function to give us the date

def getDate():
    now = datetime.datetime.now()
    my_date = datetime.datetime.today()
    weekday = calendar.day_name[my_date.weekday()]
    monthNum = now.month
    dayNum = now.day

    # A list of months
    month_Name = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
                  "November", "December"]

    # List of ordinal numbers
    ordinal_Numbers = ["1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th", "10th", "11th", "12th", "13th",
                       "14th", "15th", "16th", "17th", "18th", "19th", "20th", "21st", "22nd", "23rd", "24th", "25th",
                       "26th", "27th", "28th", "29th", "30th", "31st"]

    return "Today is " + weekday + " " + month_Name[monthNum - 1] + " the " + ordinal_Numbers[dayNum - 1] + "."


def responses(data):
    if "what is your name" in data:
        assistantResponse("Alexa")
    if "what is today's date" in  data:
        assistantResponse(getDate())
    if "what is the time " in data:
        assistantResponse(ctime())
    if "search" in data:
        search = recordAudio("What do you want to search for?")
        url = "https://www.google.com/search?q=" + search
        webbrowser.get().open(url)
        assistantResponse("Here is what i found for" + search)
    if "Find location" in data:
        locate = recordAudio("what is the location")
        url = "https://www.google.nl/maps/place/" + locate + "/&mp"
        webbrowser.get().open(url)
        assistantResponse("Here is what i found for" + locate)
    if "exit" in data:
        assistantResponse("Byeeeee!!!. ")
        exit()


time.sleep(1)
assistantResponse("How can i help you")
while 1:
    data = recordAudio()
    responses(data)