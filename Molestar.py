import requests
import time

def send_message(token, chat_id, message):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    params = {"chat_id": chat_id, "text": message}
    response = requests.post(url, params=params)
    if response.status_code != 200:
        print(f"Error: {response.text}")

def main():
    telegram_bot_token = ''
    chat_id = ''


    message = '¡Hola desde tu bot de Telegram!'
    num_messages = 500

    for i in range(num_messages):
        send_message(telegram_bot_token, chat_id, message)
        time.sleep(1)

if __name__ == "__main__":
    main()
