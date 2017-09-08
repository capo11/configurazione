import os.path
from datetime import *
import shutil
import json
import tarfile

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
usr1 = jConf['file'][0]['USR']
# recupera il valore di un parametro dal json
print path36

# funzione di ricerca nella cartella che si legge dal json


def ricerca(pathCartella):
    listadir = os.listdir(pathCartella)
# il path del listdir deve essere conosciuto precedentemente
    for linea in listadir:
        linea.strip()
        if week in linea:
            shutil.move(pathCartella + '/' + linea, master)


ricerca(path36)
ricerca(path37)

'''
with tarfile.open('./Master/W' + week + '.tgz', 'w:gz') as tar:
    tar.add('./W36/W' + week, arcname=os.path.basename('./W36/W' + week))
'''
