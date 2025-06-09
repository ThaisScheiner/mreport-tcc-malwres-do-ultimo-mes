from selenium.webdriver.common.by import By
import time

class Thn:
    def __init__(self):
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options
        from selenium.webdriver.chrome.service import Service
        from webdriver_manager.chrome import ChromeDriverManager

        options = Options()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-blink-features=AutomationControlled")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    def buscar_malwares_maio_2025(self, month, year, max_pages=25):
        self.driver.get("https://thehackernews.com/")
        time.sleep(5)
        links = []

        artigos = self.driver.find_elements(By.XPATH, '//div[@class="bc_latest_news"]/ul/li/a')

        for a in artigos:
            href = a.get_attribute("href")
            title = a.text
            if "2025" in title or "Mai" in title or "Maio" in title:
                if href not in links:
                    links.append(href)
            if len(links) >= max_links:
                break

        return links

    def fechar(self):
        try:
            self.driver.quit()
        except Exception:
            pass
