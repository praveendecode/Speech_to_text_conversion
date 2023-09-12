# Dependencies
# pip install googletrans==3.1.0a
# pip install SpeechRecognition
# pip install PyAudio
# pip install pandasai


import speech_recognition as sr
import pyaudio as audio
import googletrans
from pandasai import PandasAI
from pandasai.llm.openai import OpenAI
import pandas as pd

# Open AI
model = OpenAI(api_token='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')
praveen =  PandasAI(model,verbose=True)

# DataFrame

try :
    df = pd.read_csv("diabetes.csv")

    # text to speech
    recognizer = sr.Recognizer()


    def speak():
        with sr.Microphone() as source:
            print('Speak Now')
            voice = recognizer.listen(source)
            text = recognizer.recognize_google(voice, language="en")
            return text


    # Open Ai Answer
    while True:
        query = speak()
        print('See your query:', query)
        print()
        c = input('Type "5" to proceed with query else "6" to speak again : ')
        if c == '5':
            result = praveen(df, query)
            print(result)
            if '2' == input('Enter "2" if you wanna stop execution : '):
                break

except :
    print('Re-run the  file')

# note :  must run file on local