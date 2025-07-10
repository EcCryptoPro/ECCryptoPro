from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "API está funcionando perfeitamente!"}



from fastapi import FastAPI
import threading
import telebot
import os

app = FastAPI()

# Pegar o token do ambiente
TOKEN = os.getenv("TELEGRAM_TOKEN")
print("TOKEN LIDO:", TOKEN)  # ⚠ ISSO AQUI É SÓ PRA TESTE — DEPOIS VAMOS REMOVER

# Inicializar o bot do Telegram
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message, "Olá! O robô está ativo!")

def start_bot():
    bot.polling()

# Iniciar o bot em uma thread separada
threading.Thread(target=start_bot).start()

# --- Rotas da API ---
@app.get("/")
def read_root():
    return {"message": "API realmente está lendo esse arquivo"}

@app.get("/status")
def check_status():
    return {"status": "robô está ativo e aguardando comandos"}



    