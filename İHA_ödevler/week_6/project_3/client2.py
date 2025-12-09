import asyncio
import socketio

sio = socketio.AsyncClient()

@sio.event
async def connect():
    print("Connected to server")

    await sio.emit("chat_message", {
        "username": "Tuana",
        "message": "Hi from Client 2"
    })

@sio.on("new_message")
async def on_new_message(data):
    print("Broadcast:", data["text"])

@sio.event
async def disconnect():
    print("Disconnected")

async def main():
    await sio.connect("http://localhost:5000")
    await sio.wait()

asyncio.run(main())


#terminal --> python client2.py

