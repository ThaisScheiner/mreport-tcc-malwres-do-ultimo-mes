# estagio_tokenize.py atualizado
import os
from bs4 import BeautifulSoup
import json
import re

input_dir = "C:/Temp/paginas"
output_dir = "C:/Temp/tokenize"
relatorio_path = "relatorios/relatorio_classificado.json"
os.makedirs(output_dir, exist_ok=True)

# Carrega categorias/classificações do JSON
with open(relatorio_path, "r", encoding="utf-8") as f:
    relatorio = json.load(f)

# Processa cada HTML
arquivos_html = [f for f in os.listdir(input_dir) if f.endswith(".html")]

for arq in arquivos_html:
    input_path = os.path.join(input_dir, arq)
    output_path = os.path.join(output_dir, arq.replace(".html", ".txt"))

    # Extrair conteúdo HTML
    with open(input_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
        for tag in soup(["script", "style"]):
            tag.decompose()

        # Tenta extrair título e corpo
        titulo = soup.title.string.strip() if soup.title else "Sem título"
        paragrafos = soup.find_all('p')
        corpo = "\n".join(p.get_text(strip=True) for p in paragrafos if p.get_text(strip=True))

    # Extração da classificação
    arq_txt = arq.replace(".html", ".txt")
    categorias = relatorio.get(arq_txt, {}).get("categorias", ["desconhecido"])
    categorias_str = ", ".join(categorias)

    # Extrair mês e ano do nome do arquivo (ou fixar Maio 2025)
    mes = "maio"
    ano = "2025"

    # Salvar em .txt formatado
    with open(output_path, "w", encoding="utf-8") as f_out:
        f_out.write(f"TÍTULO:\n{titulo}\n\n")
        f_out.write(f"CORPO DA NOTÍCIA:\n{corpo}\n\n")
        f_out.write(f"CATEGORIA(S): {categorias_str}\n")
        f_out.write(f"CLASSIFICAÇÃO: {' / '.join(categorias)}\n")
        f_out.write(f"MÊS: {mes}\n")
        f_out.write(f"ANO: {ano}\n")

    print(f"[✔] Texto estruturado salvo em: {output_path}")

print("\n✅ Tokenização estruturada concluída.")
