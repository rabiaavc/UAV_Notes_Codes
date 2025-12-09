import socketio
import asyncio
# Asyncio, beklenen işlemler (IO) sırasında programın durmasını 
# engelleyerek aynı anda birden fazla işi verimli bir şekilde yapmayı sağlar.
sio = socketio.AsyncServer(async_mode="asgi")
app = socketio.ASGIApp(sio)

@sio.event
async def connect(sid,environ):
    print("Client Connected",sid)

@sio.event
async def disconnect(sid):
    print("Client disconnected",sid)

@sio.on("login")
async def on_login(sid,data):
    new_data = data.get("message")
    await sio.emit(
        "login_response",
        {"message" : f"Merhaba {new_data['username']}! Seviyen {new_data['level']}"},
        to = sid 
    )

# terminale --> uvicorn server:app --host 0.0.0.0 --port 5000