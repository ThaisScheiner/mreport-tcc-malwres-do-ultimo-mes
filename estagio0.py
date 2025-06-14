from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import quote_plus
from datetime import datetime, timedelta
import time
import os

site_desejado = "thehackernews.com"  

# Configuração: escolha entre usar mês/ano específico ou mês anterior automático
usar_mes_especifico = False # Mude para False para usar mês anterior automaticamente
                            # True = para escolher o mes espscifico
# Define o mês/ano específico
mes_especifico = "April"   # mês em inglês, ex: "April"
ano_especifico = 2025      

# Gera o mês anterior (automático)
def gerar_mes_anterior():
    hoje = datetime.today()
    primeiro_dia_mes_atual = datetime(hoje.year, hoje.month, 1)
    mes_anterior = primeiro_dia_mes_atual - timedelta(days=1)
    nome_mes = mes_anterior.strftime('%B')
    ano = mes_anterior.year
    return nome_mes, ano

def buscar_links_bing(driver, termo, site_alvo, max_paginas=5):
    url = f"https://www.bing.com/search?q={quote_plus(termo)}" # Se usar o mes espscifico comentar a linha de baixo
    # url = f"https://www.bing.com/search?q={quote_plus(termo)}&qft=+filterui:age-lt=1m"
    driver.get(url)
    todos_links = set()

    wait = WebDriverWait(driver, 15)

    for pagina in range(max_paginas):
        try:
            wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'li.b_algo h2 a')))
            resultados = driver.find_elements(By.CSS_SELECTOR, 'li.b_algo h2 a')
            for r in resultados:
                try:
                    href = r.get_attribute("href")
                    if href and site_alvo in href:
                        todos_links.add(href)
                except Exception as e:
                    print(f"[AVISO] Erro ao acessar link: {e}")
                    continue

            print(f"Página {pagina + 1} - {len(todos_links)} links coletados até agora.")

            # Rebusca o botão de próxima página a cada iteração para evitar erro
            next_button = None
            try:
                next_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.sb_pagN')))
            except:
                print("[AVISO] Botão 'Próxima' não encontrado. Fim da navegação.")
                break

            if next_button and pagina < max_paginas - 1:
                driver.execute_script("arguments[0].scrollIntoView();", next_button)
                next_button.click()
                time.sleep(2)
            else:
                break

        except Exception as e:
            print(f"Erro na página {pagina + 1}: {e}")
            with open(f"pagina_erro_{pagina + 1}.html", "w", encoding="utf-8") as f:
                f.write(driver.page_source)
            break

    return todos_links


# Configurações do navegador
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/124.0.0.0 Safari/537.36")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Define mês e ano a usar
if usar_mes_especifico:
    nome_mes = mes_especifico
    ano = ano_especifico
else:
    nome_mes, ano = gerar_mes_anterior()

termo = f"{site_desejado} malware {nome_mes} {ano}"

print(f"\nBuscando por: {termo}")
links_encontrados = buscar_links_bing(driver, termo, site_desejado)
print(f"\nTotal de links encontrados: {len(links_encontrados)}")

driver.quit()

# Salva os links encontrados
output_txt = os.path.join(os.getcwd(), 'relatorios', f'links_malware_bing_{nome_mes}_{ano}.txt')
os.makedirs(os.path.dirname(output_txt), exist_ok=True)

if links_encontrados:
    # Salva com nome por mês e ano
    with open(output_txt, "w", encoding="utf-8") as f:
        for link in links_encontrados:
            f.write(link + "\n")
    print(f"\n[OK] Links salvos em: {output_txt}")

    # Também salva com nome fixo para o ESTÁGIO 2
    copia_simples = os.path.join(os.getcwd(), 'relatorios', 'links_malware_bing_ultimo_mes_completo.txt')
    with open(copia_simples, "w", encoding="utf-8") as f:
        for link in links_encontrados:
            f.write(link + "\n")
    print(f"Cópia salva para uso contínuo: {copia_simples}")

else:
    print("[AVISO] Nenhum link encontrado. Nenhum arquivo foi criado.")
