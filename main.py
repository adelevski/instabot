import config
import time
from bot import InstaBot


def main():
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



if __name__ == "__main__":
    main()
