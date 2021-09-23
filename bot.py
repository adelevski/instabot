from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


class InstaBot:
    def __init__(self, username, password, driver_path):
        self.username = username
        self.password = password
        self.chrome_options = Options()
        self.chrome_options.add_argument('--no-sandbox')
        self.chrome_options.add_argument('--headless')
        self.chrome_options.add_argument('--disable-dev-shm-usage')
        self.bot = webdriver.Chrome(executable_path=driver_path, chrome_options=self.chrome_options)

    def login(self):
        self.bot.get('https://instagram.com/accounts/login')
        time.sleep(5)
        self.bot.find_element_by_name('username').send_keys(self.username)
        time.sleep(1)
        self.bot.find_element_by_name('password').send_keys(self.password)
        time.sleep(1)
        self.bot.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button').click()

    def search_hashtag(self, hashtag):
        self.bot.get('https://www.instagram.com/explore/tags/' + hashtag)

    def like_photos(self, amount):
        self.bot.find_element_by_class_name('v1Nh3').click()

        # Get past first 9 photos which are under "Top Posts" since we only want to like "Recent Posts"
        for i in range(9):
            time.sleep(2)
            self.bot.find_element_by_class_name('coreSpriteRightPaginationArrow').click()
            print(f"Skipped {i+1} top posts")

        successful_likes = 0
        for i in range(amount):
            time.sleep(2)
            self.bot.find_element_by_class_name('fr66n').click()
            print(f"Liked {i+1} recent posts!")
            successful_likes += 1
            time.sleep(2)
            self.bot.find_element_by_class_name('coreSpriteRightPaginationArrow').click()
        return successful_likes
