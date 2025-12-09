import socketio
import uvicorn
import time

# ASGI tabanlı async Socket.IO server
sio = socketio.AsyncServer(async_mode="asgi")
app = socketio.ASGIApp(sio)


@sio.event
async def get_time(sid):
    print("get_time request from:", sid)
    return {"server_time": time.time()}


@sio.event
async def connect(sid, environ):
    print("Client connected:", sid)

@sio.event
async def disconnect(sid):
    print("Client disconnected:", sid)



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
