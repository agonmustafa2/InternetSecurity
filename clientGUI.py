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
  