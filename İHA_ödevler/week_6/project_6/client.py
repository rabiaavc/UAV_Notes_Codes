import socketio
import asyncio

# ASGI uyumlu async client
sio = socketio.AsyncClient()

@sio.event
async def connect():
    print("Connected to server!")


async def main():
    await sio.connect("http://localhost:5000")

    while True:
        response = await sio.call("get_time")
        print("Server time:", response["server_time"])
        await asyncio.sleep(1)

asyncio.run(main())
