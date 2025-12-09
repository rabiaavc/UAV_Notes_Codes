import socketio
import uvicorn

sio = socketio.AsyncServer()
app = socketio.ASGIApp(sio)

@sio.event
async def connect(sid,environ):
    print("Client connected",sid)

#Odaya katılma isteğini iletmek için.
@sio.event
async def on_join_room(sid,data):
    room = data["room"]

    #kullanıcıyı odaya ekle
    sio.enter_room(sid,room)
    print(f"{sid} joined {room}")

    # o odadaki herkese bilgi gönder
    await sio.emit("joined_room", {"room": room}, room=room)



#Odadaki kişilere mesaj göndermek için.
@sio.event
async def room_message(sid,data):
    room = data["room"]
    message = data["message"]

    print(f"{sid} says to {room}: {message}")

    await sio.emit(
        "room_message",
        {"message": message},
        room = room
    )
@sio.event
async def disconnect(sid):
    print("Disconnected client",sid)



# ASGI server çalıştırma
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)

    