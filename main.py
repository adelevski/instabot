import config
import time
from bot import InstaBot
from ens import ENSBot


def main_insta():
    # Instantiate
    instabot = InstaBot(config.USERNAME, config.PASSWORD, config.CHROMEDRIVER_PATH)

    # Open browser and login and then wait 3 seconds for things to load
    instabot.login()
    time.sleep(4)

    # Switch to explore page and to the specific hashtag, and wait again for things to load
    instabot.search_hashtag('climbing')
    time.sleep(3)

    # Start liking photos
    successful_likes = instabot.like_photos(50)

    print(f"Liked {successful_likes} likes!")

def main_ens1():
    ens_bot = ENSBot(config.CHROMEDRIVER_PATH)
    ens_bot.connect()
    count = 249
    for i in range(100):
        domain = ens_bot.get_last_domain()
        if domain == count:
            print(f"page {i+1} scanned, no domains missing")
            count += 250
            if i <= 3:
                ens_bot.next_page(8)
            else:
                ens_bot.next_page(7)
            time.sleep(4)
        else:
            print(f"Missing domain found, count = {count}, but last domain = {domain}")


def main_ens2():
    ens_bot = ENSBot(config.CHROMEDRIVER_PATH)
    missing = []
    for i in range(40, 99):
        print(f"missing = {missing}")
        num = ens_bot.check_1000(i)
        if num == '1,000':
            print(f"Starting with {i} scanned, none missing")
        else:
            print(f"Some missing {num}, starting with {i}")
            nums = []
            for j in range(3):
                domains = ens_bot.get_domains()
                ens_bot.next_page(5)
                time.sleep(3)
                for dom in domains:
                    nums.append(int(dom))
            nums = sorted(nums)
            for j in range(1, len(nums)):
                prev = nums[j-1]
                cur = nums[j]
                if cur > prev + 1:
                    for k in range(prev, cur):
                        missing.append(k)
            





if __name__ == "__main__":
    main_ens2()
