# estagio3.py
import spacy, os, json
from utilitario import Utilitario

nlp = spacy.load("en_core_web_sm")
ents_dir = "C:/Temp/ents"
os.makedirs(ents_dir, exist_ok=True)

tokenize_dir = "C:/Temp/tokenize"
arquivos = os.listdir(tokenize_dir)
resultado_final = {}

for arquivo in arquivos:
    with open(os.path.join(tokenize_dir, arquivo), "r", encoding="utf-8") as f:
        saida = []
        for linha in f:
            doc = nlp(linha)
            for ent in doc.ents:
                if str(ent) not in saida:
                    saida.append(str(ent))
        with open(os.path.join(ents_dir, arquivo), "w", encoding="utf-8") as w:
            w.write(",".join(saida))
        resultado_final[arquivo] = saida

Utilitario.salvar("3", resultado_final, "relatorio.json")
print("[✔] Entidades extraídas e salvas.")
