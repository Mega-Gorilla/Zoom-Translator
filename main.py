import speech_recognition
 
r = speech_recognition.Recognizer()
with speech_recognition.AudioFile('hoge.wav') as src:
    audio = r.record(src)
print(r.recognize_google(audio, key='Your API Key', language='ja-JP'))