"""Programma che legge dalla cartella temp e disegna un grafico"""
from matplotlib import pyplot as plt
import glob
import json
all = []
durate = []
totali = {}
for file in glob.glob("saves/save-(*).json"):
    f = open(file, "r")
    js = json.loads(f.read())
    durate.append(js.pop("durata"))
    totali[js.pop("data")] = js.pop("tot")
    all.append(js)
print(all)
print(durate)
for i in all:
    plt.plot(i.keys(), i.values())
    plt.title("Media: {} ok al minuto".format(
        sum(totali.values()) * 60 / sum(durate)))
    plt.subplots_adjust(top=0.961, bottom=0.04, left=0.024, right=0.992)
    plt.legend(totali.keys())
plt.show()
plt.title("Totale lezioni: {}".format(len(totali)))
plt.bar(totali.keys(), totali.values())
plt.show()
