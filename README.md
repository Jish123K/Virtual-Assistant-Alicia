# Virtual-Assistant-Alicia
This is a Python program that uses the SpeechRecognition library to take voice input from the user and perform various tasks based on the recognized commands. The program can tell the current time and date, show the battery percentage of the system, set an alarm, send an email, and play music on Youtube.

The program initializes a speech recognition object and a text-to-speech engine using the pyttsx3 library. The say() function uses the engine to speak out the text passed as an argument.

The get_command() function listens to the user's voice input using the microphone and recognizes the speech using the Google Speech Recognition API. It then returns the recognized command in lowercase after removing the keyword "alice" if it is present in the command.

The tell_time() and tell_date() functions use the datetime library to get the current time and date, respectively, in a specific format and speak out the results using the say() function.

The show_battery() function uses the psutil library to get the battery percentage of the system and speaks out a warning if the percentage is below 20, else speaks out the battery percentage.

The set_alarm() function takes voice input from the user for the time at which the alarm is to be set, calculates the time difference between the current time and the alarm time, and speaks out the time difference.

The send_email() function takes voice input from the user for the subject and message of the email to be sent, and sends the email using the smtplib library.

The play_music() function takes voice input from the user for the song to be played and uses the pywhatkit library to play the song on Youtube.

The run() function is the main function that executes the program. It starts with a greeting message and listens to the user's input continuously until the user says "exit". It then calls the appropriate function based on the recognized command using if-elif statements.

Overall, this program demonstrates the use of various Python libraries to implement a voice-based virtual assistant that can perform various tasks for the user.
