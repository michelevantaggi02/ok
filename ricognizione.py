from speech_recognition import AudioFile, Recognizer
fi = AudioFile("lezione.wav")
rec = Recognizer()
with fi as f:
    audio = rec.record(f)
    print("Lezione ascoltata")
    testo = rec.recognize_google(audio, language="it-IT")
    print(testo)
    print(testo.lower().count(" ok "))
