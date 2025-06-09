import json
import os
from bs4 import BeautifulSoup
from datetime import datetime

# Caminhos
html_dir = "C:/Temp/paginas"
token_dir = "C:/Temp/tokenize"
relatorio_path = "relatorios/relatorio_classificado.json"
saida_dir = "relatorios/textos_finais"
os.makedirs(saida_dir, exist_ok=True)

# Carrega classificação
with open(relatorio_path, "r", encoding="utf-8") as f:
    relatorio = json.load(f)

# Função para extrair título da página HTML
def extrair_titulo(html_path):
    with open(html_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
        titulo = soup.title.string.strip() if soup.title else "Sem título"
    return titulo

# Gera os arquivos .txt com informações completas
for nome_arquivo in os.listdir(token_dir):
    if not nome_arquivo.endswith(".txt"):
        continue

    # Nome base sem extensão
    nome_base = nome_arquivo.replace(".txt", "")
    
    # Caminhos
    token_path = os.path.join(token_dir, nome_arquivo)
    html_path = os.path.join(html_dir, f"{nome_base}.html")
    saida_txt = os.path.join(saida_dir, f"{nome_base}_completo.txt")

    # Extrair título
    titulo = extrair_titulo(html_path)

    # Extrair corpo da notícia
    with open(token_path, "r", encoding="utf-8") as f:
        corpo = f.read().strip()

    # Dados de classificação
    dados_classificacao = relatorio.get(nome_arquivo, {})
    categorias = ", ".join(dados_classificacao.get("categorias", ["desconhecido"]))

    # Data atual como suposição do mês/ano
    mes = "maio"
    ano = "2025"

    # Monta conteúdo
    conteudo = f"""TÍTULO:
{titulo}

CATEGORIA:
{categorias}

MÊS:
{mes.upper()}

ANO:
{ano}

CORPO DA NOTÍCIA:
{corpo}
"""

    # Salva o .txt final
    with open(saida_txt, "w", encoding="utf-8") as out:
        out.write(conteudo)
    print(f"[✔] Texto final salvo: {saida_txt}")

print("\n✅ Todos os textos finais foram gerados com sucesso.")
