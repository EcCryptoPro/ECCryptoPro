from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "API está funcionando perfeitamente!"}





from fastapi import FastAPI, Request
import os
import httpx

app = FastAPI()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_API_URL = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}"



@app.post("/webhook")
async def telegram_webhook(req: Request):
    body = await req.json()

    message = body.get("message")
    if not message:
        return {"ok": True}

    chat_id = message["chat"]["id"]
    text = message.get("text", "")

    # Resposta automática
    resposta = "Recebido com sucesso! ✅"

    async with httpx.AsyncClient() as client:
        await client.post(
            f"{TELEGRAM_API_URL}/sendMessage",
            json={"chat_id": chat_id, "text": resposta}
        )

    return {"ok": True}



from fastapi import FastAPI
import threading
import telebot

app = FastAPI()

# --- Bot do Telegram ---
bot = telebot.TeleBot("SEU_TOKEN_REAL_DO_BOT")

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



