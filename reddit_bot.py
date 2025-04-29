
import config

def send_reddit_message(message):
    if config.TEST_MODE:
        print(f"[TESTMODE] Reddit zou nu posten: {message}")
    else:
        # Reddit post logic here
        pass
