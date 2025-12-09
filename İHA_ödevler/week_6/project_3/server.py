#Broadcasting

import socketio

sio = socketio.AsyncServer(async_mode ="asgi")
app = socketio.ASGIApp(sio)

@sio.event
async def connect(sid,environ):
    print("Client connect",sid)

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


#terminal --> uvicorn server:app --host 0.0.0.0 --port 5000