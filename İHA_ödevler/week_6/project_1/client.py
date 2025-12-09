import socketio

sio = socketio.Client()

@sio.event
def connect():
    print("Client Connected")

@sio.event
def disconnect():
    print("Client disconnect")

@sio.on("welcome")
def on_welcome(data):
    print(data.get("message"))


if __name__ == "__main__":
    sio.connect("http://localhost:5000")
    sio.wait()