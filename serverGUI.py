#pjesa e serverit
#importimi i librarive te nevojshme
from cryptography.fernet import Fernet
from tkinter import *
from tkinter import font 
from tkinter import ttk 
import socket 
import threading 



PORT = 13000 
SERVER = "localhost" 
ADDRESS = (SERVER, PORT) 
FORMAT = "utf-8"
  
#Krijimi i nje socket-i per konektim
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
client.connect(ADDRESS)#pjesa e serverit
#importimi i librarive te nevojshme
from cryptography.fernet import Fernet
from tkinter import *
from tkinter import font 
from tkinter import ttk 
import socket 
import threading 



PORT = 13000 
SERVER = "localhost" 
ADDRESS = (SERVER, PORT) 
FORMAT = "utf-8"
  
#Krijimi i nje socket-i per konektim
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
client.connect(ADDRESS)