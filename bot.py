from selenium import webdriver
import time


class InstaBot:
    def __init__(self, username, password, driver_path):
        self.username = username
        self.password = password
        self.bot = webdriver.Chrome(executable_path=driver_path)

    def login(self):
        self.bot.get('https://instagram.com/accounts/login')
        time.sleep(3)
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
            time.sleep(0.5)
            self.bot.find_element_by_class_name('coreSpriteRightPaginationArrow').click()
        
        for i in range(amount):
            time.sleep(3)
            self.bot.find_element_by_class_name('fr66n').click()
            self.bot.find_element_by_class_name('coreSpriteRightPaginationArrow').click()