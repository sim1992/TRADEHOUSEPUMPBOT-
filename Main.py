def main_loop():
    print("Starting TradeHousePumpBot...")
    while True:
        tokens = fetch_tokens()
        alerts, premium_alerts = analyze_tokens(tokens)

        # Send to free users (standard alerts)
        for alert in alerts:
            send_telegram_message(alert, tier="free")

        # Send to premium users (exclusive and growth alerts)
        for premium_alert in premium_alerts:
            send_telegram_message(premium_alert, tier="premium")

        time.sleep(180)  # Wait for 3 minutes before checking again
