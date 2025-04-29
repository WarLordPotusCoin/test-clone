
import config

def send_telegram_message(message):
    if config.TEST_MODE:
        print(f"[TESTMODE] Telegram zou nu posten: {message}")
    else:
        # Telegram post logic here
        pass
