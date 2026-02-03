import socket             
 
s = socket.socket() 
port = 12345                

s.connect(("127.0.0.1", port)) 

data = s.recv(1024)
print(data.decode())

s.close()