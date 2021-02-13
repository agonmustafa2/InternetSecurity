Projekti nga lenda Siguria ne Internet

Tema e Projektit: Zhvillimi i aplikacionit per komunikim te sigurte klient-server.

Pershkrimi i aplikacionit: 
  Aplikacioni permban nje meny per perzgjedhjen e opcioneve/funksionaliteteve te veta. Menyja eshte punuar si GUI (graphical user interface) duke perdorur vetem modulin tkinter te Python.Gjithashtu, per ta bere komunikimin klient-server-klient kemi perdorur menyra te enkriptimit....
  Kemi krijuar 3 file serverGUI.py, clientGUI.py dhe clientGUI2.py te cilat permbajne kod ne gjuhen python. Pjesa kodit per interface, si dhe pjesa e threadeve, socketave, qe mundesojne lidhjen(konektimin) e klienteve me server gjendet ne filen serverGUI.py.Permes emrit te hostit, qe ne rastin tone eshte localhost ose permes IP adressess dhe numrit te portit i cili duhet te jete i njejte ne te gjitha filet, mundesohet konektimi i klienteve me serverin. Tek pjesa e clientGUI.py dhe clientGUI2.py kemi pjesen ku fillimisht shkruhet mesazhi, enkriptohet end-to-end dhe permes serverGUI.py dergohet tek klienti tjeter.
  Per enkriptim kemi perdorur llojin e enkriptimit FERNET e cili na mundeson enkriptimin e mesazheve te derguara te serveri pa pasur mundesi qe ato mesazhe te pergjohen, pasi qe per dekriptimin e tyre perdorim nje qeles i cili gjenerohet duke perdorur librarine e Fernet. Ne kete mynyre mesazhet e derguara behet me te sigurta per klientin.
  
