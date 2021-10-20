""" Programma che preso un video estrae l'audio e conta quante volte viene detto 'ok' """
import os
from speech_recognition import AudioFile, Recognizer
from threading import Thread
import json, sys
from datetime import date

#imposta quanti secondi dura un file audio (non impostare più di 30s a causa di speech_recognition)
DURATA_FRAME = 20

#controlla il file specificato da linea di comando
f = ""
try:
    f = sys.argv[1]
except Exception:
    print("File video non specificato")
    quit()
#ottengo la data di ultima modifica del file e inizializzo il doc con cui si creerà il file json
stamp = os.path.getctime(f)
contati = {"durata": 0, "data": str(date.fromtimestamp(stamp)), "tot": 0}


def calcola(pos):
    """Funzione che converte una frazione di video in audio e conta le volte in cui viene scritto 'ok'"""

    #formatto con ffmpeg una frazione del video in un audio wav
    sec = "ffmpeg -i {} -vn -ss {} -t {} {}".format(f, pos
                                                    * DURATA_FRAME, DURATA_FRAME, "temp/{}.wav".format(pos))
    pid = os.popen(sec)
    pid.close()

    #apro il file audio e lo faccio riconoscere dalla API di Google
    audio_file = AudioFile("temp/{}.wav".format(pos))
    rec = Recognizer()
    with audio_file as fi:
        audio = rec.record(fi)
        testo = rec.recognize_google(audio, language="it-IT")
        print(testo)

        #conto il numero di ok
        conta = testo.lower().count("ok")
        contati["{}".format(pos * DURATA_FRAME)] = conta
        contati["tot"] += conta

#ottengo la durata del file video
comm = "ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 " + f
pid = os.popen(comm)
durata = int(float(pid.read()))
contati["durata"] = durata
pid.close()
print(durata)


div = durata//DURATA_FRAME #quantità di file che verranno generati
print(div)
#avvio in thread separati il calcolo di ogni file audio che viene creato
threads = []
for i in range(div):
    contati["{}".format(i * DURATA_FRAME)] = 0
    th = Thread(target=calcola, args=[i])
    th.start()
    threads.append(th)

for i in threads:
    i.join()

#rimuovo tutti i file audio ormai superflui
pid = os.popen("rm temp/*.wav")
pid.close()

#salvo il file json
jtext = json.dumps(contati)
print(contati)
j = open("saves/save-({}).json".format(contati["data"]), "w")
j.write(jtext)
j.close()
