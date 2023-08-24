import socket
import sys
server = socket.socket()
server.bind(("",5000))
server.listen()
connection,adress = server.accept()
print(f"new connection from : {adress}")

while True:
    cmd = input()
    if cmd == "exit":
        connection.close()
        server.close()
        sys.exit()
    if len(str.encode(cmd)) > 0:
        connection.send(str.encode(cmd))
        received = connection.recv(1024).decode("utf-8")
        print(received, end="")
