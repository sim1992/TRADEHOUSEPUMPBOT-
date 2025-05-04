# Dictionary to store initial volume, market cap, and price for each token
initial_token_data = {}

def analyze_tokens(tokens):
    global known_tokens, initial_token_data
    alerts = []
    premium_alerts = []

    for token in tokens:
        address = token.get("address")
        name = token.get("name", "Unnamed")
        volume = token.get("volume", 0)
        market_cap = token.get("market_cap", 0)  # assuming market cap is available
        price = token.get("price", 0)  # assuming price is available
        holders = token.get("holders", 0)
        previous_holders = token.get("previous_holders", 0)  # previous holders count for growth

        # Detect new tokens (both free and premium)
        if address not in known_tokens:
            known_tokens.add(address)
            initial_token_data[address] = {
                "initial_volume": volume,
                "initial_market_cap": market_cap,
                "initial_price": price
            }
            alerts.append(f"<b>New Meme Detected:</b>\n{name}\nHolders: {holders} | Volume: {volume}\nMarket Cap: ${market_cap}\nPrice: ${price}\nhttps://pump.fun/{address}")

        # Check for relative growth (2x or 5x increase in volume, market cap, or price)
        elif address in initial_token_data:
            initial_data = initial_token_data[address]
            initial_volume = initial_data["initial_volume"]
            initial_market_cap = initial_data["initial_market_cap"]
            initial_price = initial_data["initial_price"]

            # Volume Growth (2x or 5x)
            if volume >= initial_volume * 2:
                premium_alerts.append(f"<b>{name} - 2x Volume Alert (Premium Only):</b>\nVolume: {volume} | Initial: {initial_volume}\nMarket Cap: ${market_cap} | Initial: ${initial_market_cap}\nPrice: ${price} | Initial: ${initial_price}\nhttps://pump.fun/{address}")
            if volume >= initial_volume * 5:
                premium_alerts.append(f"<b>{name} - 5x Volume Alert (Premium Only):</b>\nVolume: {volume} | Initial: {initial_volume}\nMarket Cap: ${market_cap} | Initial: ${initial_market_cap}\nPrice: ${price} | Initial: ${initial_price}\nhttps://pump.fun/{address}")

            # Market Cap Growth (2x or 5x)
            if market_cap >= initial_market_cap * 2:
                premium_alerts.append(f"<b>{name} - 2x Market Cap Alert (Premium Only):</b>\nMarket Cap: ${market_cap} | Initial: ${initial_market_cap}\nVolume: {volume} | Initial: {initial_volume}\nPrice: ${price} | Initial: ${initial_price}\nhttps://pump.fun/{address}")
            if market_cap >= initial_market_cap * 5:
                premium_alerts.append(f"<b>{name} - 5x Market Cap Alert (Premium Only):</b>\nMarket Cap: ${market_cap} | Initial: ${initial_market_cap}\nVolume: {volume} | Initial: {initial_volume}\nPrice: ${price} | Initial: ${initial_price}\nhttps://pump.fun/{address}")

            # Price Growth (2x or 5x)
            if price >= initial_price * 2:
                premium_alerts.append(f"<b>{name} - 2x Price Alert (Premium Only):</b>\nPrice: ${price} | Initial: ${initial_price}\nVolume: {volume} | Initial: {initial_volume}\nMarket Cap: ${market_cap} | Initial: ${initial_market_cap}\nhttps://pump.fun/{address}")
            if price >= initial_price * 5:
                premium_alerts.append(f"<b>{name} - 5x Price Alert (Premium Only):</b>\nPrice: ${price} | Initial: ${initial_price}\nVolume: {volume} | Initial: {initial_volume}\nMarket Cap: ${market_cap} | Initial: ${initial_market_cap}\nhttps://pump.fun/{address}")

        # Free users: Pumping alerts (volume > 5000 SOL)
        elif volume > 5000:
            alerts.append(f"<b>Pumping Meme Alert:</b>\n{name}\nHolders: {holders} | Volume: {volume}\nMarket Cap: ${market_cap} | Price: ${price}\nhttps://pump.fun/{address}")

        # Premium users: Exclusive high-potential tokens (market cap > $4000 or holders growing fast)
        if market_cap > 4000 or (previous_holders and holders > previous_holders * 1.5):  # 50% growth
            premium_alerts.append(f"<b>Exclusive Pumping Meme (Premium Only):</b>\n{name}\nHolders: {holders} | Volume: {volume}\nMarket Cap: ${market_cap} | Price: ${price}\nhttps://pump.fun/{address}")

    return alerts, premium_alerts
