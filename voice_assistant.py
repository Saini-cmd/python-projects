import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import time

class VoiceAssistant:
    def __init__(self, name="Nova"):
        self.name = name
        
        # Initialize recognizer and TTS engine
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 185)
        self.engine.setProperty('volume', 1.0)
        
        print(f"{self.name} is now active...")
        self.speak(f"Hello! I'm {self.name}. Ready when you are.")
    
    def speak(self, text):
        """Speak and print"""
        print(f"{self.name}: {text}")
        self.engine.say(text)
        self.engine.runAndWait()
    
    def listen(self):
        """Listen and return the recognized text"""
        with sr.Microphone() as source:
            print(f"{self.name} is listening...")
            self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
            try:
                audio = self.recognizer.listen(source, timeout=5)
                print("Processing your command...")
                text = self.recognizer.recognize_google(audio)
                print(f"You said: {text}")
                return text.lower()
            except sr.WaitTimeoutError:
                return "timeout"
            except sr.UnknownValueError:
                return "error"
            except sr.RequestError:
                return "network_error"
            except Exception as e:
                print(f"Error: {e}")
                return "error"
    
    def process_command(self, command):
        """Process the voice command"""
        if command == "timeout":
            self.speak("Hmm, I didn't catch that. Let's try again.")
            return True
        elif command == "error":
            self.speak("I couldn't quite hear you. Could you repeat that?")
            return True
        elif command == "network_error":
            self.speak("Looks like there's a network hiccup. Please check your connection.")
            return True
        
        if "hello" in command or "hi" in command:
            self.speak("Hey! What can I do for you?")
            
        elif "your name" in command:
            self.speak(f"I'm {self.name}, your virtual assistant.")
            
        elif "time" in command:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            self.speak(f"It's currently {current_time}.")
            
        elif "date" in command:
            current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
            self.speak(f"Today is {current_date}.")
            
        elif "search" in command or "google" in command:
            search_query = command.replace("search", "").replace("google", "").strip()
            if search_query:
                self.speak(f"Opening Google for {search_query}.")
                webbrowser.open(f"https://www.google.com/search?q={search_query}")
            else:
                self.speak("Could you tell me what you'd like to search for?")
                
        elif "weather" in command:
            self.speak("I can't fetch weather updates just yet. That's coming soon.")
            
        elif "joke" in command:
            self.speak("Sure! Why did the scarecrow win an award? Because he was outstanding in his field!")
            
        elif "help" in command:
            self.speak("You can ask me about the time, date, jokes, or ask me to search Google. Say 'exit' to stop.")
        
        elif "exit" in command or "quit" in command or "goodbye" in command or "bye" in command:
            self.speak("Goodbye. Talk to you soon.")
            return False
            
        else:
            self.speak("I'm still learning that one. Try saying 'help' to see what I can assist you with.")
        
        return True

def main():
    assistant = VoiceAssistant()
    running = True
    while running:
        command = assistant.listen()
        running = assistant.process_command(command)
        time.sleep(0.5)
    print(f"{assistant.name} has gone offline.")

if __name__ == "__main__":
    main()
