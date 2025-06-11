import os
from bs4 import BeautifulSoup
import json
import re
from calendar import month_name

input_dir = "C:/Temp/paginas"
output_dir = "C:/Temp/tokenize"
relatorio_class_path = "relatorios/relatorio_classificado.json"
relatorio_links_path = "relatorios/links_malware_bing_ultimos_3_meses_completo.txt"
os.makedirs(output_dir, exist_ok=True)

# carrega o JSON de classificações
with open(relatorio_class_path, "r", encoding="utf-8") as f:
    relatorio = json.load(f)

# carrega os links e cria o mapeamento por nome do arquivo
with open(relatorio_links_path, "r", encoding="utf-8") as f:
    links = [linha.strip() for linha in f if linha.strip()]

mapa_links = {
    f"pagina{i + 1}.html": link
    for i, link in enumerate(links)
}

# processa os arquivos HTML
arquivos_html = [f for f in os.listdir(input_dir) if f.endswith(".html")]

for arq in arquivos_html:
    input_path = os.path.join(input_dir, arq)
    output_path = os.path.join(output_dir, arq.replace(".html", ".txt"))

    # extrai HTML
    with open(input_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
        for tag in soup(["script", "style"]):
            tag.decompose()

        titulo = soup.title.string.strip() if soup.title else "Sem título"
        paragrafos = soup.find_all('p')
        corpo = "\n".join(p.get_text(strip=True) for p in paragrafos if p.get_text(strip=True))


    # tenta extrair mês e ano do link
    link = mapa_links.get(arq, "")
    match = re.search(r'/(\d{4})/(\d{2})/', link)
    if match:
        ano = match.group(1)
        mes_num = int(match.group(2))
        mes = month_name[mes_num].lower()


    # salva resultado
    with open(output_path, "w", encoding="utf-8") as f_out:
        f_out.write(f"TÍTULO:\n{titulo}\n\n")
        f_out.write(f"CORPO DA NOTÍCIA:\n{corpo}\n\n")
     

    print(f"Texto estruturado salvo em: {output_path}")

print("\nTokenização estruturada concluída.")
