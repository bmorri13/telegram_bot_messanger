import asyncio
import aiohttp
from telegram import Bot

# Replace 'YOUR_TELEGRAM_BOT_TOKEN' with the token you received from BotFather
TELEGRAM_BOT_TOKEN = 'REDACTED'

# Replace 'YOUR_CHAT_ID' with your chat ID (or the ID of the user you want to send a message to) Example: '-234234234234'
YOUR_CHAT_ID = 'REDACTED'



async def get_crypto_data():
    url = 'https://api.coingecko.com/api/v3/simple/price?ids=ethereum,bitcoin&vs_currencies=usd&include_24hr_change=true'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            return data

def get_price_emoji(price_change):
    if price_change > 0:
        return "🟢"  # Green circle for price increase
    elif price_change < 0:
        return "🔴"  # Red circle for price decrease
    else:
        return "⚪"  # White circle for no change

async def send_message():
    bot = Bot(token=TELEGRAM_BOT_TOKEN)
    
    # Fetch crypto data
    crypto_data = await get_crypto_data()
    
    # Extract prices and 24h changes
    eth_price = crypto_data['ethereum']['usd']
    eth_change = crypto_data['ethereum']['usd_24h_change']
    btc_price = crypto_data['bitcoin']['usd']
    btc_change = crypto_data['bitcoin']['usd_24h_change']
    
    # Create message
    eth_emoji = get_price_emoji(eth_change)
    btc_emoji = get_price_emoji(btc_change)
    
    message = f"""Current cryptocurrency prices:

ETH: ${eth_price:.2f} {eth_emoji}
BTC: ${btc_price:.2f} {btc_emoji}"""
    
    # Send message
    await bot.send_message(chat_id=YOUR_CHAT_ID, text=message)
    print("Message sent successfully!")


# Run the asyncio event loop
if __name__ == "__main__":
    asyncio.run(send_message())
