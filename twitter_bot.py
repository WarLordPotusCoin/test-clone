
import config

def send_twitter_message(message):
    if config.TEST_MODE:
        print(f"[TESTMODE] Twitter zou nu posten: {message}")
    else:
        # Twitter post logic here
        pass
