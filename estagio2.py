# BAIXAR TODAS AS PAGINAS PARA PROCESSAR DEPOIS
import time, os, traceback, sys, inspect, hashlib, nltk;

from utilitario import *;
from nltk import tokenize;
nltk.download('punkt')


CURRENTDIR = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())));
sys.path.append(CURRENTDIR);

if not os.path.exists("/tmp/tokenize"):
    os.mkdir("/tmp/tokenize");

arquivos = os.listdir("/tmp/paginas");

for arquivo in arquivos:
    with open("/tmp/paginas/" + arquivo, 'r') as f:
        conteudo = f.read();
        frases = tokenize.sent_tokenize(conteudo);
        with open("/tmp/tokenize/" + arquivo, "w") as  w:
            for frase in frases:
                w.write(frase + "\n");


#pip3 install nltk