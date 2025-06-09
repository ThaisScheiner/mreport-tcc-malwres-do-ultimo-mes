# estagio0.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import quote_plus
import time
import os

chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("user-agent=Mozilla/5.0")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

termo = "thehackernews.com malwares maio 2025"
url = f"https://www.bing.com/search?q={quote_plus(termo)}"
driver.get(url)

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'li.b_algo h2 a'))
)

resultados = driver.find_elements(By.CSS_SELECTOR, 'li.b_algo h2 a')
links = set()
for r in resultados:
    href = r.get_attribute("href")
    if href and "thehackernews.com" in href:
        links.add(href)

print(f"\nTotal de links do TheHackerNews encontrados: {len(links)}")
for link in links:
    print(f"Link: {link}")

output_txt = os.path.join(os.getcwd(), 'relatorios', 'links_malware_bing.txt')
os.makedirs(os.path.dirname(output_txt), exist_ok=True)
with open(output_txt, "w", encoding="utf-8") as f:
    for link in links:
        f.write(link + "\n")

print(f"\nLinks salvos em: {output_txt}")
time.sleep(2)
driver.quit()
