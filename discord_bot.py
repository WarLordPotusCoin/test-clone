
import config

def send_discord_message(message):
    if config.TEST_MODE:
        print(f"[TESTMODE] Discord zou nu posten: {message}")
    else:
        # Discord post logic here
        pass
