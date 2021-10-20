# Programma che conta gli OKKEY 

### Descrizione
Questo programma, dato un file video, conta quante volte viene detta la parola OK a intervalli di 20 secondi.
È inoltre possibile stampare 2 grafici utilizzando i file JSON salvati

## Installazione
### FFMPEG
Prima di poter avviare il programma bisogna avere installato un programma esterno chiamato [FFMPEG](https://www.ffmpeg.org/).
Ed averlo accessibile da linea di comando (solo per [Windows](https://qastack.it/video/20495/how-do-i-set-up-and-use-ffmpeg-in-windows), Linux lo fa in automatico)

### Python e dipendenze
Oltre al programma esterno ovviamente c'è bisogno dell'interprete di [Python3](https://www.python.org/downloads/) e delle sue dipendenze (installabili tramite PIP)
1. [SpechRecognition](https://pypi.org/project/SpeechRecognition/)
1. [Matplotlib](https://pypi.org/project/matplotlib/)

## Utilizzo
### [contatore.py](contatore.py)
