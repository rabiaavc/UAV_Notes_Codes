@sio.event
async def disconnect(sid):
    print("Client disconnected",sid)

# chat_message event'ini yakala
@sio.on("chat_message")
async def handle_chat_message(sid,data):
    username= data["username"]
    message = data["message"]

    #Tüm clientlara mesajı gönder
    broadcast_text = f"{username} says {message}"

    await sio.emit(
        "new_message",
        {"text":broadcast_text},
        broadcast = True
    )
