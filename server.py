import socket
import sys
import time
s=socket.socket()
host=socket.gethostname()
print("server will start on host",host)
port=8080
s.bind((host,port))
print("")
print("the server has binding to host and port sucessfully")
print("")
print("server is wating for incoming connections")
print("")
s.listen(1)
conn,addr=s.accept()
print(addr,"has connected to the server and it is online")
print("")
while 1:
    message=input(str(">>"))
    message=message.encode()
    conn.send(message)
    print("message has been sent")
    print("")
    incoming_message=conn.recv(1024)
    incoming_message= incoming_message.decode()
    print("client", incoming_message)
    print("")
    
    
