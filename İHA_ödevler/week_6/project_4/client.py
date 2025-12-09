import socketio

sio = socketio.Client()

# SUNUCUDAN GELEN EVENTLER
@sio.event
def connect():
    print("Connected to server")


@sio.event
def joined_room(data):
    print(f"Joined room: {data['room']}")


@sio.event
def room_message(data):
    print("Message in your room:", data["message"])


# SUNUCUYA BAĞLAN
sio.connect("http://localhost:5000")

# Kullanıcıdan oda seçimi
room = "roomA"
sio.emit("join_room", {"room": room})

print("Type your messages (ctrl+c to exit)")
while True:
    msg = input("> ")
    sio.emit("room_message", {"room": room, "message": msg})
