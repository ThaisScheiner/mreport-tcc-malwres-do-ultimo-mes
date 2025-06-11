import json
import os

# Caminhos fixos
json_path = r"C:\Users\Thais\Desktop\mreport\relatorios\relatorio_classificado.json"
pasta_txt = r"C:\Temp\tokenize"

# Verifica se o JSON existe
if not os.path.exists(json_path):
    raise FileNotFoundError(f"Arquivo '{json_path}' não encontrado. Verifique se o estagio 5 foi executado corretamente.")

# Carrega os dados
with open(json_path, "r", encoding="utf-8") as f:
    dados = json.load(f)

# Para cada arquivo listado no JSON, procurar o .txt correspondente
for nome_arquivo, info in dados.items():
    caminho_txt = os.path.join(pasta_txt, nome_arquivo)

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
