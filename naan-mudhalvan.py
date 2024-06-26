import speech_recognition as sr

def speech_to_text(stop_word="stop"):
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Use the default microphone as the audio source
    with sr.Microphone() as source:
        print("Speak something...")
        # Adjust for ambient noise
        recognizer.adjust_for_ambient_noise(source)
        
        while True:
            # Listen to the user's input
            audio_data = recognizer.listen(source)
            try:
                print("Recognizing...")
                # Use Google Web Speech API to convert audio to text
                text = recognizer.recognize_google(audio_data)
                print("You said:", text)
                # Check if the stop word is said
                if stop_word.lower() in text.lower():
                    print("Stop word detected. Exiting...")
                    break  # Exit the loop
            except sr.UnknownValueError:
                print("Sorry, I couldn't understand what you said.")
            except sr.RequestError as e:
                print("Sorry, I couldn't request results from the speech recognition service; {0}".format(e))

if __name__ == "__main__":
    speech_to_text()
