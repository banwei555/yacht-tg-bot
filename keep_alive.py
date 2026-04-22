from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "🤖 Bot is running normally! ✅"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    # 开启后台线程运行Web服务，防止Render休眠
    t = Thread(target=run)
    t.start()