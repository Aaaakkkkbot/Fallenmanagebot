import os
import time
from flask import Flask
from threading import Thread

app = Flask(__name__)

# Basic route for health check
@app.route('/')
def index():
    return "Bot is running!", 200

def start_bot():
    """
    This function simulates the bot operation.
    Debug messages are printed only in 'dev' mode.
    """
    bot_mode = os.environ.get("BOT_MODE", "prod")
    
    if bot_mode == "dev":
        print("Dev: Starting bot process...")
    
    # Simulate bot operations with an infinite loop and periodic sleep
    while True:
        if bot_mode == "dev":
            print("Dev: Bot is polling updates...")
        # Insert your actual bot logic here
        time.sleep(10)

if __name__ == "__main__":
    # Start the bot in a background thread
    bot_thread = Thread(target=start_bot)
    bot_thread.daemon = True  # Ensures the thread exits when the main process exits
    bot_thread.start()

    # Use the PORT environment variable if available, otherwise default to 8000
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
