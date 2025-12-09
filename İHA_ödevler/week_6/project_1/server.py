import eventlet #mini web sunucusu
import socketio #SOCKET.IO için python kütüphanesi

sio = socketio.Server() #Bir Socket.IO sunucusu oluşturuyoruz.
# WSGI, Python web uygulamaları ile web sunucuları arasındaki iletişim standartıdır.
app = socketio.WSGIApp(sio)

@sio.event
# sid -> Socket.IO tarafından her bağlanan 
# istemciye otomatik olarak verilen benzersiz bir kimliktir.

# environ, WSGI’mimarisinden gelen bir değişkendir ve bağlantı 
# yapan istemci hakkında ortam bilgilerini içerir.

# sid → bağlanan istemcinin benzersiz ID’si
# environ → istemci hakkında çeşitli bilgiler içeren bir sözlük (dict)
def connect(sid,environ):
    print("Client Connected")

    sio.emit("welcome",   # event adı
             {"message": "Welcome to the Socket.IO server!"},  # veri
             to=sid  # sadece bu bağlanan client'a
            )

# İstemci bağlantıyı kapattığında
@sio.event
def disconnect(sid):
    print("Client disconnect",sid)


# Sunucuyu başlat
if __name__ == "__main__":
    #Eventlet’in WSGI sunucusunu başlat, 5000 portunu 
    #dinle ve gelen bağlantıları Socket.IO uygulamasına yönlendir.

    #Bu kısım bir WSGI sunucusu başlatır.
    #Eventlet’in içinde mini bir web sunucusu vardır.
    # eventlet.wsgi.server() → bu sunucuyu çalıştırır.
    #hangi IP ve Port u dinleyeceğini belirti 
    # " " -> tüm IP adreslerini dinle (0.0.0.0 anlamına gelir)
    # 5000 -> port numarası

    eventlet.wsgi.server(eventlet.listen(("",5000)),app)