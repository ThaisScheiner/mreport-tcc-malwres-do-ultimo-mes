import json
import os
import shutil

# Caminhos fixos
json_path = r"C:\Users\Thais\Desktop\mreport\relatorios\relatorio_classificado.json"
pasta_tokenize = r"C:\Temp\tokenize"
pasta_txt_finais = r"C:\Users\Thais\Desktop\mreport\relatorios\textos_finais"

# Etapa 1: Copiar arquivos .txt de tokenize para textos_finais
if not os.path.exists(pasta_tokenize):
    raise FileNotFoundError(f"Pasta '{pasta_tokenize}' não encontrada.")

os.makedirs(pasta_txt_finais, exist_ok=True)

arquivos_tokenize = [f for f in os.listdir(pasta_tokenize) if f.endswith(".txt")]
for arquivo in arquivos_tokenize:
    origem = os.path.join(pasta_tokenize, arquivo)
    destino = os.path.join(pasta_txt_finais, arquivo)
    shutil.copy2(origem, destino)
    print(f"[COPIADO] {arquivo} -> textos_finais")

# Etapa 2: Verifica se o JSON existe
if not os.path.exists(json_path):
    raise FileNotFoundError(f"Arquivo '{json_path}' não encontrado. Verifique se o estágio 5 foi executado corretamente.")

#  Etapa 3: Carrega os dados do JSON
with open(json_path, "r", encoding="utf-8") as f:
    dados = json.load(f)

#  Etapa 4: Adiciona classificações nos arquivos .txt da pasta textos_finais
for nome_arquivo, info in dados.items():
    if not nome_arquivo.lower().endswith(".txt"):
        nome_arquivo += ".txt"

    caminho_txt = os.path.join(pasta_txt_finais, nome_arquivo)

    if os.path.exists(caminho_txt):
        with open(caminho_txt, "a", encoding="utf-8") as f:
            f.write("\n\n=== Classificação do Malware ===\n")
            for classificacao in info.get("classificacoes", []):
                categoria = classificacao.get("categoria", "Desconhecido")
                nome = classificacao.get("classificacao", "Não identificado")
                f.write(f"- {categoria}: {nome}\n")
        print(f"[OK] Classificação adicionada: {caminho_txt}")
    else:
        print(f"[AVISO] Arquivo TXT não encontrado: {caminho_txt}")
