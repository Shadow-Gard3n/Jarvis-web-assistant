# Jarvis Web Assistant

Jarvis Web Assistant is a Python-based voice-controlled assistant that allows users to open web links using custom shortcuts. It uses speech recognition to take commands and Pyttsx3 for text-to-speech feedback, making it a hands-free tool for browsing the web.

## Features
- **Custom Shortcut Creation**: Easily create custom shortcuts for any website, allowing you to open frequently visited sites with simple voice commands.
- **Voice Recognition**: The assistant listens for your commands and opens the corresponding website. You can say commands like `open Google` or `open YouTube`.
- **Text-to-Speech Feedback**: The assistant provides spoken feedback to let you know what it is doing, whether it’s opening a website or asking for more commands.
- **Repeat and Exit Commands**: After executing a command, you can either repeat with a new command or say `exit` to close the assistant.

## Code Structure
- `speak()`: This function is responsible for converting text messages into speech. It uses the `pyttsx3` library.
- `database()`: Allows the user to input shortcut names and their corresponding links.
- `takecommand()`: Captures the user's voice input and returns it as a string.
- `main()`: The main loop where voice commands are recognized, processed, and the respective websites are opened.


## Required libraries
- `pip install pyttsx3`
- `pip install SpeechRecognition`
## Example for code
- `Type the shortcut name you want for link: youtube`
- `Type the link for above shortcut: https://www.youtube.com`
- `Type '1' for more input and '2' if you are done: 2`
- `Listening...`
- `Recognizing...`
- `User said: Open youtube`
- `Opening youtube`



