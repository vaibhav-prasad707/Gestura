import speech_recognition as sr
import pyttsx3
import time

class GesturaAssistant:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        
        # Configure voice properties
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[0].id)  # Select a clear voice
        self.engine.setProperty('rate', 150)  # Speaking speed
        
        # Contact list for Vaibhav Prasad
        self.contacts = ["Mom", "Dad", "Kevin", "Sam"]

    def speak(self, text):
        """Converts text to speech and outputs it."""
        print(f"Assistant: {text}")
        self.engine.say(text)
        self.engine.runAndWait()
        
    def listen(self):
        """Listens to user input and returns recognized text."""
        with self.microphone as source:
            print("Listening...")
            self.recognizer.adjust_for_ambient_noise(source)
            try:
                audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=10)
                print("Processing...")
                text = self.recognizer.recognize_google(audio)
                print(f"User: {text}")
                return text.lower()
            except sr.WaitTimeoutError:
                self.speak("Please repeat yourself.")
                return None  # Allow retry in main_flow()
            except sr.UnknownValueError:
                self.speak("I didn't understand. Please repeat yourself.")
                return None  # Allow retry in main_flow()
            except Exception as e:
                self.speak("There was an error. Please repeat yourself.")
                return None  # Allow retry in main_flow()

    def introduction(self):
        """Introduces the assistant and lists available contacts."""
        self.speak("Welcome to Gestura - Your accessible communication platform!")
        time.sleep(1)
        self.speak("Our platform supports multiple accessibility features including:")
        self.speak("Voice commands, Sign language translation, and Haptic feedback.")
        time.sleep(1)
        
        self.speak("You can contact:")
        for contact in self.contacts:
            self.speak(contact)
        self.speak("Who would you like to chat with today?")

    def main_flow(self):
        """Main function to initiate the conversation and handle user input."""
        self.introduction()
        
        while True:
            self.speak("Please say the name of the person you want to connect with, or say 'help' for options.")
            
            response = self.listen()
            if not response:
                continue  # Retry listening
            
            if "help" in response:
                self.speak("You can connect with: " + ", ".join(self.contacts))
                continue

            contact = self.validate_contact(response)
            
            if contact:
                self.speak(f"Connecting you with {contact}. Please wait while we establish the connection.")
                break
            else:
                self.speak("I didn't recognize that contact. Please repeat yourself.")

    def validate_contact(self, response):
        """Validates if the spoken name matches a known contact."""
        for contact in self.contacts:
            if contact.lower() in response:
                return contact
        return None  # Contact not found

if __name__ == "__main__":
    assistant = GesturaAssistant()
    try:
        assistant.main_flow()
    except KeyboardInterrupt:
        assistant.speak("Exiting Gestura assistant. Goodbye!")
