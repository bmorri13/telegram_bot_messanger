#Telegram Chatbot Setup Guide
- This guide walks you through the steps to create a Telegram chatbot using Python and the python-telegram-bot library. It also includes instructions for adding your bot to a group and retrieving the group chat ID.

## Prerequisites
- A Telegram account
- Python 3.7 or higher installed
- pip package manager installed

## Step-by-Step Instructions
### 1. Create a Telegram Bot
    1. Open Telegram and search for BotFather.
    2. Start a conversation with BotFather by clicking Start.
    3. Use the command /newbot to create a new bot.
    4. Follow the instructions to set a name and username for your bot. The username must end with "bot" (e.g., myfirsttelegram_bot).
    5. After creating the bot, BotFather will provide a bot token. Save this token; you’ll need it to interact with the Telegram API.

### 2. Set Up Your Development Environment
- Install Python: Ensure Python 3.7 or higher is installed on your system. Download it from the official Python website.

- Install Required Python Libraries: Open a terminal or command prompt and run:

```bash
pip install python-telegram-bot requests
```

### 3. Get Your Chat ID
- To send messages, you need your Telegram chat ID:

    1. Start a Chat with Your Bot:
        - Search for your bot in Telegram using the username you set.
        - Send a message to your bot (e.g., "Hello").

    2. Retrieve the Chat ID:
    - Modify your script to retrieve the chat ID:

``` python
import asyncio
from telegram import Bot
from telegram.error import TelegramError

TELEGRAM_BOT_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'

async def get_chat_id():
    bot = Bot(token=TELEGRAM_BOT_TOKEN)
    try:
        updates = await bot.get_updates()
        if updates:
            for update in updates:
                print(f"Chat ID: {update.message.chat.id}")
        else:
            print("No updates received. Make sure you have sent a message to the bot.")
    except TelegramError as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    asyncio.run(get_chat_id())
```

> NOTE: Run this script to get your chat ID, which will be printed to the console. Update YOUR_CHAT_ID in your main script with this ID.

### 4. Add Your Bot to a Group and Get the Group Chat ID
1. Add Your Bot to a Group:
    - Open Telegram and create a new group or choose an existing group.
    - Add your bot to the group by searching for its username and adding it as a member.

2. Get the Group Chat ID:
    - Create a new Python script named get_group_chat_id.py with the following code:

``` python
import requests
import json

TELEGRAM_BOT_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'

url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/getUpdates"

# Make the request and store the response
response = requests.get(url)

# Convert the response to JSON and pretty-print it
result = json.dumps(response.json(), indent=4)
print(result)
```


3. Replace 'YOUR_TELEGRAM_BOT_TOKEN' with your bot's token.\
4. Run the script:
``` bash
python3.12 get_group_chat_id.py
```

> NOTE: Look for the "chat" object in the printed JSON output to find the "id" of your group. It will typically be a negative number (e.g., -123456789).


6. Run Your Bot Script
- Run your bot script to send a message:

``` bash
python3.12 telegram_bot.py
```
