"""Programma che legge dalla cartella temp i file json e disegna un grafico"""
from matplotlib import pyplot as plt
import glob
import json

#varie liste con cui stampare i grafici
frammenti = []
durate = []
totali = {}

#ottengo la lista dei file json salvati
for file in glob.glob("saves/save-(*).json"):
    f = open(file, "r")
    js = json.loads(f.read())
    durate.append(js.pop("durata"))
    totali[js.pop("data")] = js.pop("tot")
    frammenti.append(js)
print(frammenti)
print(durate)

for i in frammenti:
    #creo un grafico lineare per ogni file json salvato
    #ogni grafico è a intervalli di 20 secondi
    plt.plot(i.keys(), i.values())
    plt.title("Media: {} ok al minuto".format(
        sum(totali.values()) * 60 / sum(durate)))
    plt.subplots_adjust(top=0.961, bottom=0.04, left=0.024, right=0.992)
    plt.legend(totali.keys())
plt.show()

#creo un grafico a barre con i valori totali delle lezioni
plt.title("Totale lezioni: {}".format(len(totali)))
plt.bar(totali.keys(), totali.values())
plt.show()
