import socket             

s = socket.socket()     
print("Created a socket object")

port = 12345                
s.bind(("", port))

s.listen(5)     
print(f"Socket is listening on port {port}")            

while (True): 
  c, addr = s.accept()     
  print("Got connection from ", addr)
 
  c.send("Connected to the server".encode()) 
  c.close()
  
  break