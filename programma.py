import os.path
from datetime import *
import shutil
import json
import tarfile
import ast

today = datetime.today()
week = today.strftime("%U")

# carica file json


def loadConfig():
    try:
        with open('./config.json') as confFile:
            config = json.load(confFile)
            confFile.close()
            return config
    except Exception as e:
        print e


jConf = loadConfig()
master = jConf['file'][0]['Master']
path36 = jConf['file'][0]['Cartella1']
path37 = jConf['file'][0]['Cartella2']
usr1 = jConf['file'][0]['USR1']
usr2 = jConf['file'][0]['USR2']
# recupera il valore di un parametro dal json

# funzione di ricerca nella cartella che si legge dal json


def ricerca(pathCartella, usr):
    if(usr == ""):
        listadir = os.listdir(pathCartella)
# il path del listdir deve essere conosciuto precedentemente
        for linea in listadir:
            linea.strip()
            if week in linea:
                shutil.move(pathCartella + '/' + linea, master)


ricerca(path36, usr1)
ricerca(path37, usr2)


with tarfile.open('./Master/W' + week + '.tgz', 'w:gz') as tar:
    listadir = os.listdir('./Master')
    for linea in listadir:
        linea.strip()
        tar.add('./Master/' + linea, arcname=os.path.basename('./Master/' + linea))

listadir = os.listdir('./Master')
linea = week
contaneg = 0
contapos = 0
for linea in listadir:
    linea.strip()
    if 'txt' in linea:
        primo = open('./Master/' + linea)
        for riga in primo.readlines():
            if((int(riga)) < 0):
                contaneg = contaneg + int(float(riga))
            else:
                contapos = contapos + int(float(riga))
log = open('analisi.log', 'w')
log.writelines('Settimana ' + week + '  ')
log.write('positivi: ' + str(contapos) + ', negativi: ' + str(contaneg))
