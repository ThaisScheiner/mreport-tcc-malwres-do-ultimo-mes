import time, os, traceback, sys, spacy, json
from utilitario import Utilitario

# Carrega o modelo do spaCy
nlp = spacy.load("en_core_web_sm")

# Diretório de saída de entidades nomeadas
ents_dir = "/tmp/ents"
if not os.path.exists(ents_dir):
    os.makedirs(ents_dir)

# Diretório de entrada com os arquivos tokenizados
tokenize_dir = "/tmp/tokenize"
arquivos = os.listdir(tokenize_dir)

resultado_final = {}  # Dicionário para salvar todas as entidades por arquivo

for arquivo in arquivos:
    with open(os.path.join(tokenize_dir, arquivo), "r") as f:
        saida = []
        linhas = f.readlines()

        for linha in linhas:
            doc = nlp(linha)
            for ent in doc.ents:
                if str(ent) not in saida:
                    saida.append(str(ent))

        # Salva individualmente no /tmp/ents
        with open(os.path.join(ents_dir, arquivo), "w") as w:
            w.write(",".join(saida))

        # Adiciona ao dicionário final
        resultado_final[arquivo] = saida

# Salvar no projeto como JSON final com Utilitario
Utilitario.salvar("3", resultado_final, "relatorio.json")
