from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

class Browser:
    def __init__(self):
        options = Options()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-features=IsolateOrigins,site-per-process")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    def pagina(self, url):
        self.driver.get(url)
        time.sleep(3)
        return self.driver.page_source

    def fechar(self):
        try:
            self.driver.quit()
        except Exception:
            pass
