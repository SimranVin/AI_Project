# Jarvis Voice Assistant

Welcome to **Jarvis**, a voice-controlled personal assistant built using Python! This project integrates speech recognition, text-to-speech, AI, and web automation to create a smart assistant that can interact with you.

## Features

- **Voice Commands**: Open websites like Google and YouTube with just your voice.
- **Music Playback**: Control music playback using voice commands.
- **News Reader**: Listen to the latest news headlines.
- **AI-powered Conversations**: Use OpenAI's **Gemini** model to have intelligent conversations.
- **Speech-to-Text and Text-to-Speech**: Convert spoken commands to text and responses to speech.

## Libraries and APIs Used

- **speech_recognition**: To listen for voice commands.
- **pyttsx3**: To convert text into speech (text-to-speech).
- **requests**: To fetch news headlines from a public API.
- **google.generativeai**: For integrating OpenAI’s Gemini AI model to respond intelligently.
- **webbrowser**: To open websites via voice commands.
- **Custom `musicLibrary` Module**: For playing music based on user requests.

## Installation

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/yourusername/your-repository-name.git
    cd your-repository-name
    ```

2. **Install the Required Libraries**:

    ```bash
    pip install -r requirements.txt
    ```

3. **Setup OpenAI API Key**:
    - Get your OpenAI API key and insert it into the code where required.

## Usage

### Running the Assistant

1. **Run the Script**:

    ```bash
    python jarvis_assistant.py
    ```

2. **Voice Activation**: After running the script, the assistant listens for the wake word "Jarvis". Once activated, you can give commands like:

    - "Open Google"
    - "Open YouTube"
    - "Play [Song Name]"
    - "Read the news"

### Example Code

```python
import speech_recognition as sr
import pyttsx3
import webbrowser
import musicLibrary
import requests
import google.generativeai as genai

recognizer = sr.Recognizer()
engine = pyttsx3.init()

newsapi = "your_newsapi_key_here"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def aiProcess(command):
    genai.configure(api_key="YOUR_API_KEY")
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(command)
    return response.text

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            data = r.json()
            articles = data.get('articles', [])
            for article in articles:
                speak(article['title'])
    else:
        output = aiProcess(c)
        speak(output)

if __name__ == "__main__":
    speak("Initializing Jarvis ..........")
    while True:
        r = sr.Recognizer()
        try:
            with sr.Microphone() as source:
                print("Listening.....")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
                word = r.recognize_google(audio)
                if word.lower() == "jarvis":
                    speak("Say Command")
                    with sr.Microphone() as source:
                        print("Jarvis Active....")
                        speak("Jarvis Activating....")
                        audio = r.listen(source)
                        command = r.recognize_google(audio)
                        processCommand(command)
        except Exception as e:
            print(f"Error: {e}")
