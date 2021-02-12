#Klasa per ndertimin e GUI
class GUI: 

    #konstruktori
    def __init__(self): 
        
        #Krijimi i dritares se pare
        self.Window = Tk() 
        self.Window.withdraw() 

       
            #_________PJESA E MENUSE________________________________
        menubar= Menu(self.Window)
        file=Menu(menubar, tearoff=0)
        file.add_separator()
        file.add_command(label="Exit", command=self.Window.quit)
        menubar.add_cascade(label="File",menu=file)
        edit=Menu(menubar,tearoff=0)
        menubar.add_cascade(label="Edit",menu=edit)
        help=Menu(menubar,tearoff=0)
        menubar.add_cascade(label="Help",menu=help)
        self.Window.config(menu=menubar)
          
        #Krijimi dritares per Login
        self.kyqja = Toplevel() 
        #Titulli
        self.kyqja.title("LOGIN PAGE") 
        self.kyqja.resizable(width = False,height = False) 
        self.kyqja.configure(width = 900, height = 400) 
        #____________TITULLI I LOGIN-IT______
        self.titulli = Label(self.kyqja, text = "LOGIN PAGE",justify = CENTER,font = "Gadugi 20") 
        #________POZICIONIMI______________
        self.titulli.place(relheight = 0.15,relx = 0.4,rely = 0.07) 

        #_________PJESA E MENUSE________________________________
        menubar= Menu(self.kyqja)
        file=Menu(menubar, tearoff=0)
        file.add_separator()
        file.add_command(label="Exit", command=self.kyqja.quit)
        menubar.add_cascade(label="File",menu=file)
        edit=Menu(menubar,tearoff=0)
        menubar.add_cascade(label="Edit",menu=edit)
        help=Menu(menubar,tearoff=0)
        menubar.add_cascade(label="Help",menu=help)
        self.kyqja.config(menu=menubar)

        #_________USERNAME___________________
        self.username = Label(self.kyqja, text = "USERNAME",font = "Gadugi 16") 
        self.username.place(relheight = 0.2,relx = 0.42,rely = 0.18) 
          
        #_________PJESA KU SHKRUHET USERNAME-I__________
        self.usernamefield = Entry(self.kyqja,font = "Gadugi 14")  
        self.usernamefield.place(relwidth = 0.2,relheight = 0.08,relx = 0.38,rely = 0.33) 
        # me fokusu kursorin
        self.usernamefield.focus() 
        #_________BUTONI LOGIN-IT_____
        self.butoni = Button(self.kyqja,text = "LOGIN",font = "Gadugi 14",bg="#b3b3ff",height = 1,width = 10,command = lambda: self.goAhead(self.usernamefield.get())) 
        self.butoni.place(relx = 0.41,rely = 0.43) 
        self.Window.mainloop() 

       
        #dalja ne dritaren tjeter
    def goAhead(self, name): 
        self.kyqja.destroy() 
        self.chat(name) 
          
        #me marr mesazhe 
        rcv = threading.Thread(target=self.receive) 
        rcv.start() 
  
    #Dritarja e CHAT-it
    def chat(self,name): 
        self.name = name 
        #____________CHAT__________________________-
        self.Window.deiconify() 
        self.Window.title("CHAT") 
        self.Window.resizable(width = False, height = False) 
        self.Window.configure(width = 900, height = 400,bg = "#17202A") 
        #____________PJESA E USERNAME-IT LART_______________
        self.head = Label(self.Window, bg = "#050a14", fg = "#EAECEE", text = self.name , font = "Gadugi 14",pady = 5) 
        #________VIZA NDARESE______________________ 
        self.head.place(relwidth = 1) 
        self.line = Label(self.Window, width = 450, bg = "#f2f2f2") 
          
        self.line.place(relwidth = 1, rely = 0.07,relheight = 0.012) 
        #_______________HAPSIRA E CHATIT_______________
        self.teksti = Text(self.Window, width = 20,height = 2, bg = "#333333", fg = "#EAECEE", font = "Gadugi 14", padx = 5,pady = 5) 
        self.teksti.place(relheight = 0.745,relwidth = 1,rely = 0.08) 
        #vija posht
        self.bottom = Label(self.Window, bg = "#ABB2B9",height = 80)   
        self.bottom.place(relwidth = 1, rely = 0.825) 
         #___________PJESA ME SHKRU MESAZHIN__________ 
        self.mesazhi = Entry(bg = "#0d0d0d", fg = "#EAECEE", font = "Gadugi 14") 
        
        #pjesa e shkruarjes se mesazhit
        self.mesazhi.place(relwidth = 0.7,relheight = 0.09, rely = 0.85,relx = 0.011) 
        self.mesazhi.focus() 
        #_________BUTONI SEND______________ 
        self.butoniSend = Button(text = "SEND", font = "Gadugi 14",width = 4,height = 5,bg = "#ABB2B9",command = lambda : self.sendButton(self.mesazhi.get())) 
        self.butoniSend.place(relx = 0.77,rely = 0.85,relheight = 0.09,relwidth = 0.2) 
        self.teksti.config(cursor = "arrow") 
          
        #krijimi i scroll bar 
        scrollbar = Scrollbar(self.teksti) 
          
        #vendosja e scroll bar n GUI
        scrollbar.place(relheight = 1,relx = 0.974) 
        scrollbar.config(command = self.teksti.yview) 
        self.teksti.config(state = DISABLED) 
  
    #fillimi i threadit per dergimin e mesazheve 
    def sendButton(self, msg): 
        self.teksti.config(state = DISABLED) 
        self.msg=msg 
        self.mesazhi.delete(0, END) 
        snd= threading.Thread(target = self.sendMessage) 
        snd.start() 

        
        
        
        
        
        
        
#Klasa per ndertimin e GUI
class GUI: 

    #konstruktori
    def __init__(self): 
        
        #Krijimi i dritares se pare
        self.Window = Tk() 
        self.Window.withdraw() 

       
            #_________PJESA E MENUSE________________________________
        menubar= Menu(self.Window)
        file=Menu(menubar, tearoff=0)
        file.add_separator()
        file.add_command(label="Exit", command=self.Window.quit)
        menubar.add_cascade(label="File",menu=file)
        edit=Menu(menubar,tearoff=0)
        menubar.add_cascade(label="Edit",menu=edit)
        help=Menu(menubar,tearoff=0)
        menubar.add_cascade(label="Help",menu=help)
        self.Window.config(menu=menubar)
          
        #Krijimi dritares per Login
        self.kyqja = Toplevel() 
        #Titulli
        self.kyqja.title("LOGIN PAGE") 
        self.kyqja.resizable(width = False,height = False) 
        self.kyqja.configure(width = 900, height = 400) 
        #____________TITULLI I LOGIN-IT______
        self.titulli = Label(self.kyqja, text = "LOGIN PAGE",justify = CENTER,font = "Gadugi 20") 
        #________POZICIONIMI______________
        self.titulli.place(relheight = 0.15,relx = 0.4,rely = 0.07) 

        #_________PJESA E MENUSE________________________________
        menubar= Menu(self.kyqja)
        file=Menu(menubar, tearoff=0)
        file.add_separator()
        file.add_command(label="Exit", command=self.kyqja.quit)
        menubar.add_cascade(label="File",menu=file)
        edit=Menu(menubar,tearoff=0)
        menubar.add_cascade(label="Edit",menu=edit)
        help=Menu(menubar,tearoff=0)
        menubar.add_cascade(label="Help",menu=help)
        self.kyqja.config(menu=menubar)

        #_________USERNAME___________________
        self.username = Label(self.kyqja, text = "USERNAME",font = "Gadugi 16") 
        self.username.place(relheight = 0.2,relx = 0.42,rely = 0.18) 
          
        #_________PJESA KU SHKRUHET USERNAME-I__________
        self.usernamefield = Entry(self.kyqja,font = "Gadugi 14")  
        self.usernamefield.place(relwidth = 0.2,relheight = 0.08,relx = 0.38,rely = 0.33) 
        # me fokusu kursorin
        self.usernamefield.focus() 
        #_________BUTONI LOGIN-IT_____
        self.butoni = Button(self.kyqja,text = "LOGIN",font = "Gadugi 14",bg="#b3b3ff",height = 1,width = 10,command = lambda: self.goAhead(self.usernamefield.get())) 
        self.butoni.place(relx = 0.41,rely = 0.43) 
        self.Window.mainloop() 

       
        #dalja ne dritaren tjeter
    def goAhead(self, name): 
        self.kyqja.destroy() 
        self.chat(name) 
          
        #me marr mesazhe 
        rcv = threading.Thread(target=self.receive) 
        rcv.start() 
  
    #Dritarja e CHAT-it
    def chat(self,name): 
        self.name = name 
        #____________CHAT__________________________-
        self.Window.deiconify() 
        self.Window.title("CHAT") 
        self.Window.resizable(width = False, height = False) 
        self.Window.configure(width = 900, height = 400,bg = "#17202A") 
        #____________PJESA E USERNAME-IT LART_______________
        self.head = Label(self.Window, bg = "#050a14", fg = "#EAECEE", text = self.name , font = "Gadugi 14",pady = 5) 
        #________VIZA NDARESE______________________ 
        self.head.place(relwidth = 1) 
        self.line = Label(self.Window, width = 450, bg = "#f2f2f2") 
          
        self.line.place(relwidth = 1, rely = 0.07,relheight = 0.012) 
        #_______________HAPSIRA E CHATIT_______________
        self.teksti = Text(self.Window, width = 20,height = 2, bg = "#333333", fg = "#EAECEE", font = "Gadugi 14", padx = 5,pady = 5) 
        self.teksti.place(relheight = 0.745,relwidth = 1,rely = 0.08) 
        #vija posht
        self.bottom = Label(self.Window, bg = "#ABB2B9",height = 80)   
        self.bottom.place(relwidth = 1, rely = 0.825) 
         #___________PJESA ME SHKRU MESAZHIN__________ 
        self.mesazhi = Entry(bg = "#0d0d0d", fg = "#EAECEE", font = "Gadugi 14") 
        
        #pjesa e shkruarjes se mesazhit
        self.mesazhi.place(relwidth = 0.7,relheight = 0.09, rely = 0.85,relx = 0.011) 
        self.mesazhi.focus() 
        #_________BUTONI SEND______________ 
        self.butoniSend = Button(text = "SEND", font = "Gadugi 14",width = 4,height = 5,bg = "#ABB2B9",command = lambda : self.sendButton(self.mesazhi.get())) 
        self.butoniSend.place(relx = 0.77,rely = 0.85,relheight = 0.09,relwidth = 0.2) 
        self.teksti.config(cursor = "arrow") 
          
        #krijimi i scroll bar 
        scrollbar = Scrollbar(self.teksti) 
          
        #vendosja e scroll bar n GUI
        scrollbar.place(relheight = 1,relx = 0.974) 
        scrollbar.config(command = self.teksti.yview) 
        self.teksti.config(state = DISABLED) 
  
    #fillimi i threadit per dergimin e mesazheve 
    def sendButton(self, msg): 
        self.teksti.config(state = DISABLED) 
        self.msg=msg 
        self.mesazhi.delete(0, END) 
        snd= threading.Thread(target = self.sendMessage) 
        snd.start()  
