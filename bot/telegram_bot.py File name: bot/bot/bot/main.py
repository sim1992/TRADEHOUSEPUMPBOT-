from bot.telegram_bot import send_telegram_message

def main():
    message = "TradeHousePumpBot is now running!"
    result = send_telegram_message(message)
    print("Telegram Response:", result)

if __name__ == "__main__":
    main()
