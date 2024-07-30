import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

# Initialize the recognizer and text-to-speech engine
listener = sr.Recognizer()
machine = pyttsx3.init()

def talk(text):
    machine.say(text)
    machine.runAndWait()

def input_instruction():
    global instruction
    try:
        with sr.Microphone() as source:
            print('Listening...')
            speech = listener.listen(source)
            # Use the correct method name: recognize_google
            instruction = listener.recognize_google(speech)
            instruction = instruction.lower()
            if "jarvis" in instruction:
                instruction = instruction.replace('jarvis', "").strip()
                print(instruction)
    except Exception as e:
        print(f"Error: {e}")
        instruction = ""
    return instruction

def play_jarvis():
    instruction = input_instruction()
    print(instruction)
    if "play" in instruction:
        song = instruction.replace('play', "").strip()
        talk(f"Playing {song}")
        pywhatkit.playonyt(song)
    elif 'time' in instruction:
        current_time = datetime.datetime.now().strftime('%I:%M %p')
        talk(f"Current time is {current_time}")
    elif 'date' in instruction:
        current_date = datetime.datetime.now().strftime('%d/%m/%Y')
        talk(f"Today's date is {current_date}")
    elif 'how are you' in instruction:
        talk('I am fine, how about you?')
    elif 'what is your name' in instruction:
        talk('I am Jarvis. What can I do for you?')
    elif 'who is' in instruction:
        person = instruction.replace('who is', "").strip()
        try:
            info = wikipedia.summary(person, 1)
            print(info)
            talk(info)
        except wikipedia.exceptions.PageError:
            talk("I couldn't find information on that topic.")
    else:
        talk('Please repeat.')

# Run the play_jarvis function
play_jarvis()
