
import config
from telegram_bot import send_telegram_message
from twitter_bot import send_twitter_message
from reddit_bot import send_reddit_message
from discord_bot import send_discord_message

def main():
    message = "Hello World! This is a test post."

    send_telegram_message(message)
    send_twitter_message(message)
    send_reddit_message(message)
    send_discord_message(message)

if __name__ == "__main__":
    main()
