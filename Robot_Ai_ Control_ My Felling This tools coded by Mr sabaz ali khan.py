import pyttsx3
import random
import speech_recognition as sr

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')  # Female voice (Zira)
engine.setProperty('rate', 150)  # Speed of speech

# Lists for suggestions
games = ["Free Fire", "PUBG", "Candy Crush", "Among Us", "Call of Duty"]
activities = ["khana khao", "dost ke saath baat karo", "ek movie dekho", "thodi der walk karo"]
food_suggestions = ["pizza", "biryani", "pasta", "samosa", "ice cream"]

# Function to speak text
def speak(text):
    print(f"Robot: {text}")
    engine.say(text)
    engine.runAndWait()

# Function to detect feelings based on keywords
def detect_feeling(user_input):
    user_input = user_input.lower()
    if any(word in user_input for word in ["sad", "udaas", "dukh", "naraaz"]):
        return "sad"
    elif any(word in user_input for word in ["happy", "khush", "maza", "excited"]):
        return "happy"
    elif any(word in user_input for word in ["bored", "boring", "thak", "tired"]):
        return "bored"
    else:
        return "neutral"

# Function to suggest games or activities
def suggest_action(feeling):
    if feeling == "sad":
        return f"Chalo, thodi der {random.choice(games)} khelte hain ya {random.choice(activities)} karte hain!"
    elif feeling == "happy":
        return f"Wow, aap toh khush ho! {random.choice(games)} khelo ya {random.choice(food_suggestions)} khao!"
    elif feeling == "bored":
        return f"Boring lag raha hai? Try {random.choice(games)} ya {random.choice(activities)}!"
    else:
        return f"Kuch try karna hai? Jaise {random.choice(games)} khelna ya {random.choice(activities)}?"

# Main loop
def main():
    speak("Namaste! Main aapka robot dost hoon. Aap kaisa feel kar rahe hain? Boliye ya type kijiye.")
    
    while True:
        # Option 1: Text input
        user_input = input("Aap: ")

        # Option 2: Voice input (uncomment to enable)
        """
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("Boliye...")
            audio = recognizer.listen(source)
            try:
                user_input = recognizer.recognize_google(audio, language="hi-IN")
                print(f"Aap: {user_input}")
            except sr.UnknownValueError:
                speak("Sorry, main samajh nahi paya. Fir se bolo ya type karo.")
                continue
            except sr.RequestError:
                speak("Internet issue hai. Text mein type karo.")
                continue
        """

        if "bye" in user_input.lower() or "band karo" in user_input.lower():
            speak("Achha, milte hain fir! Khush raho!")
            break

        # Detect feeling
        feeling = detect_feeling(user_input)
        speak(f"Lagta hai aap {feeling} feel kar rahe hain.")

        # Suggest action
        suggestion = suggest_action(feeling)
        speak(suggestion)

if __name__ == "__main__":
    main()