import speech_recognition as sr

import pyttsx3

import pyjokes

import wikipedia

# Initializing the speech recognizer and engine

listener = sr.Recognizer()

engine = pyttsx3.init()

# A function to convert text to speech

def speak(text):

    engine.say(text)

    engine.runAndWait()

# A function to listen to user input and convert speech to text

def get_command():

    with sr.Microphone() as source:

        print("Listening...")

        listener.adjust_for_ambient_noise(source)

        audio = listener.listen(source)

    try:

        print("Recognizing...")

        command = listener.recognize_google(audio)

        command = command.lower()

        print(f"User said: {command}")

    except sr.UnknownValueError:

        print("Sorry, I did not understand that.")

        command = ""

    except sr.RequestError:

        print("Sorry, my speech service is down.")

        command = ""

    return command

# A function to tell jokes

def tell_joke():

    joke = pyjokes.get_joke()

    print(joke)

    speak(joke)

# A function to get information from Wikipedia

def get_wikipedia_info(topic):

    try:

        info = wikipedia.summary(topic, sentences=2)

        print(info)

        speak(info)

    except wikipedia.exceptions.PageError:

        print("Sorry, I could not find any information on that topic.")

        speak("Sorry, I could not find any information on that topic.")

    except wikipedia.exceptions.DisambiguationError:

        print("There are multiple pages with that name. Please be more specific.")

        speak("There are multiple pages with that name. Please be more specific.")

# A function to handle user commands

def handle_command(command):

    if "tell me a joke" in command:

        tell_joke()

    elif "tell me about" in command:

        topic = command.split("about")[1].strip()

        get_wikipedia_info(topic)

    else:

        print("Sorry, I did not understand that.")

        speak("Sorry, I did not understand that.")

# A welcome message

speak("Hello, how can I assist you today?")

# Listening to user commands and handling them

while True:

    command = get_command()

    handle_command(command)

