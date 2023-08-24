import socket
client = socket.socket()
host = socket.gethostname()
port = 5000
client.connect((host,port))

message = input(">>")
while True:
    client.send(message.encode())
    recieved = client.recv(1024).decode()
    print(f"server : {recieved}")
    message = input(">>")