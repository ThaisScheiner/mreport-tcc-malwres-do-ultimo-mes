from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import quote_plus
from datetime import datetime
import calendar
import time
import os

def gerar_ultimos_3_meses():
    hoje = datetime.today()
    meses = []
    for i in range(3):
        mes_atual = (hoje.month - i - 1) % 12 + 1
        ano_atual = hoje.year - ((hoje.month - i - 1) // 12)
        nome_mes = calendar.month_name[mes_atual]
        meses.append((nome_mes, ano_atual))
    return meses[::-1]

def buscar_links_bing(driver, termo, max_paginas=5):
    url = f"https://www.bing.com/search?q={quote_plus(termo)}"
    driver.get(url)
    todos_links = set()
    
    for pagina in range(max_paginas):
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'li.b_algo h2 a'))
            )
            resultados = driver.find_elements(By.CSS_SELECTOR, 'li.b_algo h2 a')
            for r in resultados:
                href = r.get_attribute("href")
                if href and "thehackernews.com" in href:
                    todos_links.add(href)

            print(f"Página {pagina + 1} - {len(todos_links)} links coletados até agora.")

            next_buttons = driver.find_elements(By.CSS_SELECTOR, 'a.sb_pagN')
            if next_buttons and pagina < max_paginas - 1:
                next_buttons[0].click()
                time.sleep(3)
            else:
                break

        except Exception as e:
            print(f"Erro na página {pagina + 1}: {e}")
            break

    return todos_links


chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("user-agent=Mozilla/5.0")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

todos_links = set()
meses = gerar_ultimos_3_meses()

for nome_mes, ano in meses:
    termo = f"thehackernews.com malwares {nome_mes} {ano}"
    print(f"\nBuscando por: {termo}")
    links_mes = buscar_links_bing(driver, termo)
    print(f"Links encontrados para {nome_mes} {ano}: {len(links_mes)}")
    todos_links.update(links_mes)
    time.sleep(2)

driver.quit()

output_txt = os.path.join(os.getcwd(), 'relatorios', 'links_malware_bing_ultimos_3_meses_completo.txt')
os.makedirs(os.path.dirname(output_txt), exist_ok=True)
with open(output_txt, "w", encoding="utf-8") as f:
    for link in todos_links:
        f.write(link + "\n")

print(f"\nTotal de links únicos encontrados: {len(todos_links)}")
print(f"Links salvos em: {output_txt}")
