import socketio
import uvicorn

sio = socketio.AsyncServer()
app = socketio.ASGIApp(sio) #Uvicorn üzerinde Socket.IO çalıştırır

@sio.event
async def connect(sid,environ):
    print("Client connected",sid)

@sio.event(namespace = "/chat")
async def chat_message(sid,data):
    message = data["message"]
    print(f"[CHAT] Client connected: {sid}")

    # aynı namespace’e geri broadcast et
    #Mesajı yalnızca /chat namespace’indeki client’lara gönderir
    await sio.emit("chat_message", {"message": message}, namespace="/chat")

@sio.event(namespace = "/status")
async def health_check(sid,data):
    print(f"[STATUS] Client connected: {sid}")

    #healt_check clienttan gelen event
    #healt_responce server -ın cevabı
    await sio.emit("health_response", {"status": "ok"}, namespace="/status", to=sid)

@sio.event
async def disconnect(sid):
    print("Client disconnect",sid)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)