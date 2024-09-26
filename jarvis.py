import webbrowser
import pyttsx3
import speech_recognition as sr
jarvis = pyttsx3.init()

def speak(message):
    jarvis.say(message)
    jarvis.runAndWait()

def database():
    z = 1
    data = {}
    while z == 1:
        speak("type the short cut name you want for link")
        x = input("Type the shortcut name you want for link: ")
        speak("Type the link for above short cut")
        y = input("Type the link for above shortut: ")
        data[x] = y
        speak("Type 1 for more input and 2 if you are done")
        z = int(input("Type '1' for more input and '2' if you are done: "))
    return data
    
def takecommand():
    command = sr.Recognizer()
    query = None
    while query is None:
        with sr.Microphone() as source:
            print("Listening...")
            command.adjust_for_ambient_noise(source)
            command.pause_threshold = 1
            audio = command.listen(source)
            print("Recognizing...")
            try:
                query = command.recognize_google(audio, language="en-in")
                print(f"User said: {query.capitalize()}")
                speak(f"User said {query}")
                query = query.lower()
            except sr.UnknownValueError:
                speak("Voice too low. Please try again")
                query = None
            except sr.RequestError:
                speak("Internet Problem. Please try again") 
                query = None  
    return query     

def main():
    data = database()
    while True:
        speak("Hello how can i help you")
        finished_command = takecommand()
        for key in data:
            if "open "+key in finished_command:
                webbrowser.open(data[key])
                speak("opening "+key)  
                break
        speak("Say again for more command and exit if you are done")   
        repeatcmd = takecommand()  
        if 'exit' in repeatcmd:
            speak("Okay, exiting") 
            break
        elif 'again' in repeatcmd:
            speak('taking a new command')
            continue
        else:
            speak('Wrong input so taking new command')
            continue
        
main()