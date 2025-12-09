import socketio
import asyncio

sio = socketio.AsyncClient()

@sio.event
async def connect():
    print("Client Connected")

    await sio.emit(
        "login",
        {"message" : { "username": "Ali", "level": 5 } },
    )

@sio.event
async def disconnect():
    print("Client disconnected")

@sio.on("login_response")
async def on_login_response(data):
    print(data.get("message"))

async def main():
    await sio.connect("http://localhost:5000")
    await sio.wait()

asyncio.run(main()) 



# terminale --> python client.py