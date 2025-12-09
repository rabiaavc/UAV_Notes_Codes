import socketio
import asyncio

sio = socketio.AsyncClient()

@sio.event
async def connect():
    print("Connected to server")

    # Sunucuya ilk mesajı gönder
    await sio.emit("chat_message", {
        "username": "Rabia",
        "message": "Hello message from Client 1"
    })

@sio.on("new_message")
async def on_new_message(data):
    print("Broadcast:", data["text"])

@sio.event
async def disconnect():
    print("Disconnected to server")

async def main():
    await sio.connect("http://localhost:5000")
    await sio.wait()

asyncio.run(main())


# terminal --> python client1.py

