# BAIXAR TODAS AS PAGINAS PARA PROCESSAR DEPOIS
import time, os, traceback, sys, inspect, hashlib, nltk;

from utilitario import *;
from nltk import tokenize;
nltk.download('punkt')


CURRENTDIR = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())));
sys.path.append(CURRENTDIR);

if not os.path.exists("C:/Temp/tokenize"):
    os.mkdir("C:/Temp/tokenize");

arquivos = os.listdir("C:/Temp/paginas");

for arquivo in arquivos:
    with open("C:/Temp/paginas/" + arquivo, 'r') as f:
        conteudo = f.read();
        frases = tokenize.sent_tokenize(conteudo);
        with open("C:/Temp/tokenize/" + arquivo, "w") as  w:
            for frase in frases:
                w.write(frase + "\n");


#pip3 install nltk