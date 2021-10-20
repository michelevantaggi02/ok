""" Programma che con ffmpeg converte da video .mkv ad audio .wav"""
import os
from datetime import date
import sys
print(sys.argv[1])
stamp = os.path.getctime(
    "/run/media/michi/2996DB510A1C7C78/LEZ.3-13-10-21.mkv")
print(stamp)
print(str(date.fromtimestamp(stamp)))
