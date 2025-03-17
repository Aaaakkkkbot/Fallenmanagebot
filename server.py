import os
import time
import logging
from flask import Flask
from threading import Thread

app = Flask(__name__)

# Health check endpoint; ensures instance is healthy
@app.route('/')
def index():
    return "Bot is running!", 200

def start_bot():
    """
    This function starts your bot.
    Make sure that your FallenRobot module has a function 'main()' which starts the bot.
    """
    try:
        # Adjust this import according to your project structure
        from FallenRobot import main
        main()  # This should be a blocking call that runs your bot
    except Exception as e:
        logging.exception("Error starting bot: %s", e)

if __name__ == "__main__":
    # Start the bot in a background thread
    bot_thread = Thread(target=start_bot)
    bot_thread.daemon = True  # Bot thread will exit when main process exits
    bot_thread.start()

    # Use PORT from environment variable (or default to 8000)
    port = int(os.environ.get("PORT", 8000))
    # Running Flask's built-in server for simplicity (not recommended for high traffic)
    app.run(host="0.0.0.0", port=port)
