import socketio
from aiohttp import web

# Asenkron Socket.IO server
sio = socketio.AsyncServer(cors_allowed_origins="*")
app = web.Application()
sio.attach(app)

# Mesaj event'i (async)
@sio.event
async def mesaj_gonder(sid, data):
    print("Gelen mesaj:", data)
    await sio.emit("mesaj_yayinla", data)  # herkese yayınla

@sio.event
async def connect(sid, environ):
    print("Bağlanan:", sid)

@sio.event
async def disconnect(sid):
    print("Ayrıldı:", sid)

# Sunucuyu başlat
if __name__ == "__main__":
    print("Async chat sunucusu çalışıyor...")
    web.run_app(app, host="0.0.0.0", port=5000)
