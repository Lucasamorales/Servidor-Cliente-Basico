import socket


PORT = 5050
HEADER = 64 
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONECT"
SERVER = "192.168.0.14"
ADDR = (SERVER,PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    message = msg.encode(FORMAT)
    msg_lenght = len(message)
    send_lenght = str(msg_lenght).encode(FORMAT)
    send_lenght += b' '*(HEADER - len(send_lenght))
    client.send(send_lenght)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))


send('hello world')
input()
send('Testing 123...')
input()
send('testing 1234...')

send(DISCONNECT_MESSAGE)