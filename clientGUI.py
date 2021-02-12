#importimi i librarive te nevojshme
from cryptography.fernet import Fernet
import socket 
import threading 

  
PORT = 13000   
SERVER = 'localhost' 
ADDRESS = (SERVER, PORT) 
FORMAT = "utf-8"
  
#lista qe ka emrat e te gjith klienteve te konektuar
clients, names = [], [] 
  
#krijimi i soketes
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 

#e bind adresen  e seeverit ne soket 
server.bind(ADDRESS) 



#fillimi i konektimit
def startChat(): 
    
    print("Serveri " + SERVER) 
      
    #shikon te gjitha konektimet 
    server.listen() 
      
    while True: 
        
        #prano konektimet dhe kthen konektime te reja te klienti dhe adreses se lidhur me te
        conn, addr =  server.accept() 
        conn.send("NAME".encode(FORMAT)) 
          
        #tregon sasin e te dhenave qe mund te pranohet
        name = conn.recv(2048).decode(FORMAT) 
          
       #tregon emrin e klientit
        names.append(name) 
        clients.append(conn) 
          
        print(f"Emri perdoruesit :{name}") 
          
        #mesazhi i transmetuar
        broadcastMessage(f"{name} has joined the chat".encode(FORMAT)) 
          
        conn.send(''.encode(FORMAT)) 
          
        #fillom thread handling
        thread = threading.Thread(target = handle, 
                                  args = (conn, addr)) 
        thread.start() 
          
        #numri i klientave te konektuar
        print(f"Numri koneksioneve aktive {threading.activeCount()-1}") 
  