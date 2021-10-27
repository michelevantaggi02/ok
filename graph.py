"""Programma che legge dalla cartella temp i file json e disegna un grafico"""
from matplotlib import pyplot as plt
import glob
import json

colors = plt.rcParams["axes.prop_cycle"]()

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
fig, ax = plt.subplots(len(frammenti), sharex=True)

fig.suptitle("Media: {} ok al minuto".format(
    sum(totali.values()) * 60 / sum(durate)))

for i in range(len(frammenti)):
    #creo un grafico lineare per ogni file json salvato
    #ogni grafico è a intervalli di 20 secondi

    c = next(colors)["color"]

    ax[i].plot(frammenti[i].keys(), frammenti[i].values(), color=c)
    chiavi = ax[i].get_xticks()
    ax[i].set_xticks(chiavi[::len(chiavi)//60])
    ax[i].set_xlim(left=-1)
    plt.xticks(rotation=90)
    print(list(totali.keys())[i])

#sistemo un po' il grafico e lo mostro
plt.subplots_adjust(top=0.961, bottom=0.055, left=0.024, right=0.992, hspace=0)
fig.legend(totali.keys())
mng = plt.get_current_fig_manager()
mng.window.state("zoomed")
plt.show()

#creo un grafico a barre con i valori totali delle lezioni
plt.title("Totale lezioni: {}".format(len(totali)))
plt.bar(totali.keys(), totali.values())
mng = plt.get_current_fig_manager()
mng.window.state("zoomed")
plt.subplots_adjust(top=0.97, bottom=0.03, left=0.04, right=0.96)
plt.show()
