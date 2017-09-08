import os.path
from datetime import *
import shutil

today = datetime.today()
week = today.strftime("%U")
# config = open('nomefile', 'r')


def ricerca(pathCartella):
    listadir = os.listdir(pathCartella)
# il path del listdir deve essere conosciuto precedentemente
    for linea in listadir:
        linea.strip()
        if week in linea:
            shutil.move(pathCartella + '/' + linea, './Master')


ricerca('./W36')
