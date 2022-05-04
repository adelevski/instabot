from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class ENSBot:
    def __init__(self, driver_path):
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("enable-automation")
        options.add_argument("--disable-infobars")
        options.add_argument("--disable-dev-shm-usage")
        self.bot = webdriver.Chrome(executable_path=driver_path, chrome_options=options)
        # self.bot = webdriver.Remote()

    def connect(self):
        self.bot.get('https://ens.tools/domains?showFilters=true&length_min=5&length_max=5&numbers=only&tab=available&sort=domain&direction=asc&perPage=250')

    def get_last_domain(self):
        try:
            # last_row = WebDriverWait(driver, 5).until(
            #     EC.presence_of_element_located((By.XPATH, "//*[@class= 'w-full domains-table max-w-full']/tbody/tr[250]/td"))
            # )
            last_row = self.bot.find_elements_by_xpath("//*[@class= 'w-full domains-table max-w-full']/tbody/tr[250]/td")
            domain = last_row[2].text
            num, _ = domain.split(".")
        except:
            self.bot.quit()
            return -1
        return int(num)


    def next_page(self, button):
        self.bot.find_element_by_xpath(f"/html/body/div[1]/div[4]/div/div[3]/div[4]/div[2]/div/div[2]/div/button[{str(button)}]").click()


    