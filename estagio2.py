from estagio1 import Browser
from datetime import datetime, timedelta
from urllib.parse import urlparse
import os
import re

input_path = 'relatorios/links_malware_bing_ultimo_mes_completo.txt'
saida_dir = "C:/Temp/paginas"
os.makedirs(saida_dir, exist_ok=True)

if not os.path.exists(input_path):
    print(f"[ERRO] Arquivo não encontrado: {input_path}")
    exit(1)

with open(input_path, "r", encoding="utf-8") as f:
    links = [linha.strip() for linha in f if linha.strip()]

if not links:
    print(f"[AVISO] Nenhum link para processar no arquivo: {input_path}")
    exit(0)

# Pega os meses válidos (mês atual e anterior)
hoje = datetime.today()
mes_atual = hoje.strftime('%Y/%m')
mes_anterior = (hoje.replace(day=1) - timedelta(days=1)).strftime('%Y/%m')

# Regex para extrair trecho tipo /2025/06
padrao_data_url = re.compile(r'/(\d{4}/\d{2})')

# Inicia navegador
browser = Browser()

salvos = 0
ignorados = 0

for i, link in enumerate(links):
    # Verifica se tem /YYYY/MM válido na URL
    match = padrao_data_url.search(link)
    if match:
        data_url = match.group(1)
        if data_url not in [mes_atual, mes_anterior]:
            print(f"[AVISO] Ignorando (fora do período): {link}")
            ignorados += 1
            continue
    else:
        print(f"[AVISO] Ignorando (sem data reconhecida): {link}")
        ignorados += 1
        continue

    try:
        conteudo = browser.pagina(link)
        if conteudo:
            nome_arquivo = os.path.join(saida_dir, f"pagina{salvos + 1}.html")
            with open(nome_arquivo, "w", encoding="utf-8") as arq:
                arq.write(conteudo)
            print(f"[OK] Página salva: pagina{salvos + 1}.html")
            salvos += 1
        else:
            print(f"[AVISO] Conteúdo nulo (possível CAPTCHA ou bloqueio): {link}")
    except Exception as e:
        print(f"[ERRO] Ao baixar {link}: {e}")

browser.fechar()

print(f"\n[OK] Total salvos: {salvos}")
print(f"[AVISO] Total ignorados: {ignorados}")
