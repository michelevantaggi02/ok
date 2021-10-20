""" Programma che preso un video estrae l'audio e conta quante volte viene detto 'ok' """
import os
from speech_recognition import AudioFile, Recognizer
from threading import Thread
import json
import time
from datetime import date
durata_frame = 20
f = "/run/media/michi/2996DB510A1C7C78/LEZ.4-20-10-21.mkv"
stamp = os.path.getctime(f)
contati = {"durata": 0, "data": str(date.fromtimestamp(stamp)), "tot": 0}


def calcola(pos):
    """Funzione che conta le volte in cui viene scritto 'ok'"""
    sec = "ffmpeg -i {} -vn -ss {} -t {} {}".format(f, pos
                                                    * durata_frame, durata_frame, "temp/{}.wav".format(pos))
    pid = os.popen(sec)
    pid.close()
    audio_file = AudioFile("temp/{}.wav".format(pos))
    rec = Recognizer()
    with audio_file as fi:
        audio = rec.record(fi)
        testo = rec.recognize_google(audio, language="it-IT")
        print(testo)
        conta = testo.lower().count("ok")
        contati["{}".format(pos * durata_frame)] = conta
        contati["tot"] += conta


comm = "ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 " + f
pid = os.popen(comm)
durata = int(float(pid.read()))
contati["durata"] = durata
pid.close()
print(durata)
div = durata//durata_frame
print(div)
threads = []
for i in range(div):
    contati["{}".format(i * durata_frame)] = 0
    th = Thread(target=calcola, args=[i])
    th.start()
    threads.append(th)

for i in threads:
    i.join()

pid = os.popen("rm temp/*.wav")
pid.close()
jtext = json.dumps(contati)
print(contati)
j = open("saves/save-({}).json".format(contati["data"]), "w")
j.write(jtext)
j.close()
