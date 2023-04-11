import speech_recognition as sr

import pyttsx3

import datetime

import wikipedia

import pywhatkit

import psutil

import smtplib

listener = sr.Recognizer()

engine = pyttsx3.init()

def say(text):

    engine.say(text)

    engine.runAndWait()

def get_command():

    try:

        with sr.Microphone() as source:

            print('Listening...')

            listener.adjust_for_ambient_noise(source, duration=0.5)

            voice = listener.listen(source, timeout=5)

            command = listener.recognize_google(voice)

            command = command.lower()

            if 'alice' in command:

                command = command.replace('alice', '')

                print(command)

    except:

        pass

    return command

def tell_time():

    time = datetime.datetime.now().strftime('%I:%M %p')

    say(f"The current time is {time}")

def tell_date():

    date = datetime.datetime.now().strftime('%d %B %Y')

    say(f"Today's date is {date}")

def show_battery():

    battery = psutil.sensors_battery()

    percent = battery.percent

    if percent < 20:

        say(f"Warning! Battery is low, only {percent} percent remaining")

    else:

        say(f"Battery is at {percent} percent")

def set_alarm():

    say('At what time do you want me to set the alarm?')

    alarm_time = get_command()

    alarm_time = datetime.datetime.strptime(alarm_time, '%I:%M %p')

    current_time = datetime.datetime.now()

    delta_t = alarm_time - current_time

    secs = delta_t.seconds

    mins, secs = divmod(secs, 60)

    hours, mins = divmod(mins, 60)

    time = f"{hours} hours, {mins} minutes, and {secs} seconds"

    say(f"Alarm set for {alarm_time.strftime('%I:%M %p')}, which is {time} from now.")

def send_email():

    say("What is the subject of the email?")

    subject = get_command()

    say("What is the message?")

    message = get_command()

    try:

        server = smtplib.SMTP('smtp.gmail.com', 587)

        server.starttls()

        server.login('your_email@gmail.com', 'your_password')

        server.sendmail('your_email@gmail.com', 'recipient_email@gmail.com', f'Subject: {subject}\n\n{message}')

        say("Email sent successfully!")

    except:

        say("Sorry, there was an error sending the email")

def play_music():

    say('What song would you like me to play?')

    song = get_command()

    pywhatkit.playonyt(song)

    say(f"Playing {song} on Youtube.")

def run():

    say('Hi, I am Alice. How can I assist you?')

    while True:

        command = get_command()

        if 'time' in command:

            tell_time()

        elif 'date' in command:

            tell_date()

        elif 'battery' in command:

            show_battery()

        elif 'set alarm' in command:

            set_alarm()

        elif 'send email' in command:

            send_email()

        elif 'play music' in command:

            play_music()

        elif 'exit' in command:

            say('Goodbye!')

            break

if __name__ == '__main__':

    run()

