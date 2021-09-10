import config
from bot import InstaBot


def main():
    # Instantiate
    instabot = InstaBot(config.USERNAME, config.PASSWORD, config.CHROMEDRIVER_PATH)

    # Open browser and login and then wait 3 seconds for things to load
    instabot.login()
    time.sleep(3)

    # Switch to explore page and to the specific hashtag, and wait again for things to load
    instabot.search_hashtag('climbing')
    time.sleep(3)

    # Start liking photos
    instabot.like_photos(50)

    print("Finished liking!")


if __name__ == __main__():
    main()