import os
import speech_recognition as sr
import cohere

cohere_client= cohere.Client('Pb0qKlkqiBBJhxSiJnXbrqKwsWKYPvr5CZsF0mTF')

def listen():
    recognizer= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio= recognizer.listen(source)
    try:
        text =recognizer.recognize_google(audio)
        return text
    except Exception as e:
        print("Could not understand audio")
        return None

def generate_response(text):
    response= cohere_client.chat(
        model="command-r-plus",
        message=text
    )
    return response.text

def speak(text):
    os.system(f"say {text}")

def conversation():
    while True:
        user_input= listen()
        if user_input is not None:
            print(f"You said: {user_input}")
            response= generate_response(user_input)
            print(f"AI says: {response}")
            speak(response)
        else:
            print("Could not understand audio. Try again.")

if __name__=="__main__":
    conversation()