import socket
import threading

PORT = 5050
HEADER = 64 
SERVER  = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER,PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONECT"


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn,addr): #handle individual connections, one client , one server
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_lenght = conn.recv(HEADER).decode(FORMAT)
        if msg_lenght:
            msg_lenght = int(msg_lenght)
            msg = conn.recv(msg_lenght).decode(FORMAT)

        if msg == DISCONNECT_MESSAGE:
            connected = False

        print(f"[{addr} {msg}")

        conn.send("Msg recevied".encode(FORMAT))
    conn.close()

def start(): #handle new connections and distributes it 
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn,addr))
        thread.start()
        print(f"[ACIVE CONNECTIONS]  {threading.activeCount() -1}")



print("[STARTING] server is starting ...")
start()