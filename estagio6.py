import json
import os
from bs4 import BeautifulSoup
from datetime import datetime

# diretorios
html_dir = "C:/Temp/paginas"
token_dir = "C:/Temp/tokenize"
relatorio_path = "relatorios/relatorio_classificado.json"
saida_dir = "relatorios/textos_finais"
os.makedirs(saida_dir, exist_ok=True)

# carrega a classificacao
with open(relatorio_path, "r", encoding="utf-8") as f:
    relatorio = json.load(f)

# extrai titulo da pagina HTML
def extrair_titulo(html_path):
    with open(html_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
        titulo = soup.title.string.strip() if soup.title else "Sem título"
    return titulo

# gera os arquivos .txt com informações 
for nome_arquivo in os.listdir(token_dir):
    if not nome_arquivo.endswith(".txt"):
        continue

    # nome base sem a extensão
    nome_base = nome_arquivo.replace(".txt", "")
    
    # caminhos
    token_path = os.path.join(token_dir, nome_arquivo)
    html_path = os.path.join(html_dir, f"{nome_base}.html")
    saida_txt = os.path.join(saida_dir, f"{nome_base}_completo.txt")

    # extrai o titulo
    titulo = extrair_titulo(html_path)

    # extrai o corpo da noticia
    with open(token_path, "r", encoding="utf-8") as f:
        corpo = f.read().strip()

    # dados da classificacao
    dados_classificacao = relatorio.get(nome_arquivo, {})
    categorias = ", ".join(dados_classificacao.get("categorias", ["desconhecido"]))

    # data atual 
    mes = datetime.now().strftime('%b')  # Exemplo: Jun, Jul, Aug
    ano = "2025"

    # monta o conteudo
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

    # salva o .txt final
    with open(saida_txt, "w", encoding="utf-8") as out:
        out.write(conteudo)
    print(f"Texto final salvo: {saida_txt}")

print("\nTodos os textos finais foram gerados com sucesso.")
