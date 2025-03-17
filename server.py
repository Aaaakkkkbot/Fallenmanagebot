from flask import Flask
from threading import Thread

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!", 200

def run_server():
    app.run(host='0.0.0.0', port=8000)

server_thread = Thread(target=run_server)
server_thread.start()
