from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

# Configurar as opções do Chrome
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--ignore-certificate-errors")  # Ignora erros SSL

# Usando WebDriver Manager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Acessar a página de notícias de segurança
driver.get("https://www.bleepingcomputer.com/news/security/")

# Espera até os links com "malware" estarem disponíveis
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//a[contains(@href, "malware")]'))
)

# Coletar e filtrar links únicos
resultados = driver.find_elements(By.XPATH, '//a[contains(@href, "malware")]')
links = set()
for r in resultados:
    href = r.get_attribute("href")
    if href:
        links.add(href)

# Exibir os links encontrados
print(f"\nTotal de notícias únicas de malware encontradas: {len(links)}")
for link in links:
    print(f"Link encontrado: {link}")

# Salvar os links em um arquivo txt
output_txt = os.path.join(os.getcwd(), 'relatorios', 'links_malware.txt')
os.makedirs(os.path.dirname(output_txt), exist_ok=True)
with open(output_txt, "w", encoding="utf-8") as f:
    for link in links:
        f.write(link + "\n")
print(f"\nLinks salvos no arquivo: {output_txt}")

# Espera para visualização
time.sleep(3)
driver.quit()
