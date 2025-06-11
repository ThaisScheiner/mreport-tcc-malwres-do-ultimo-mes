from estagio1 import Browser
import os

input_path = "relatorios/links_malware_bing_ultimos_3_meses_completo.txt"
saida_dir = "C:/Temp/paginas"
os.makedirs(saida_dir, exist_ok=True)

browser = Browser()

with open(input_path, "r", encoding="utf-8") as f:
    links = [linha.strip() for linha in f if linha.strip()]

for i, link in enumerate(links):
    try:
        conteudo = browser.pagina(link)
        if conteudo:
            with open(os.path.join(saida_dir, f"pagina{i + 1}.html"), "w", encoding="utf-8") as arq:
                arq.write(conteudo)
            print(f"Página salva: pagina{i + 1}.html")
        else:
            print(f"Conteúdo nulo (possível CAPTCHA): {link}")
    except Exception as e:
        print(f"Erro ao baixar {link}: {e}")

browser.fechar()
