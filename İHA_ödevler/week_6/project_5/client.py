import socketio

sio = socketio.Client()

# /chat namespace : connect
@sio.event(namespace = "/chat")
def connect():
    print("[CHAT] Connected to /chat namespace")

# /chat namespace : chat_message listener
@sio.on("chat_message", namespace="/chat")
def on_chat_message(data):
    print("[CHAT MESSAGE]", data["message"])

# /status namespace : connect
@sio.event(namespace = "/status")
def connect():
    print("[STATUS] Connected to /status namespace")

# /status namespace: health_response listener
@sio.on("health_response", namespace="/status")
def on_health_response(data):
    print("[STATUS RESPONSE]", data["status"])

# Sunucuya bağlan (iki namespace'e birden)
sio.connect("http://localhost:5000", namespaces=["/chat", "/status"])


# Ana döngü: kullanıcıdan komut al
print("\nKomutlar:")
print("  1 - Chat mesajı gönder (/chat)")
print("  2 - Health check gönder (/status)")
print("CTRL+C ile çıkabilirsiniz.\n")

while True:
    choice = input("Seçiminiz (1-2): ")

    if choice == "1":
        msg = input("Chat mesajı: ")
        sio.emit("chat_message", {"message": msg}, namespace="/chat")

    elif choice == "2":
        print("Health check gönderiliyor...")
        sio.emit("health_check", {"check": True}, namespace="/status")

    else:
        print("Geçersiz seçim!")