Projekti nga lënda Siguria ne Internet

Tema e Projektit: Zhvillimi i aplikacionit për komunikim të sigurtë klient-server.

Përshkrimi i aplikacionit: 
  Aplikacioni përmban një meny per perzgjedhjen e opcioneve/funksionaliteteve të veta. Menyja është punuar si GUI (graphical user interface) duke përdorur modulin tkinter të Python. Gjithashtu, për ta bërë komunikimin klient-server kemi përdorur mënyren e enkriptimit FERNET.
Kemi krijuar 3 file clientGUI.py, clientGUI2.py dhe serverGUI.py të cilat përmbajne kod në gjuhën python. Pjesa kodit për interface, si dhe pjesa e threadeve, socketave, qe mundesojne lidhjen (konektimin) e klienteve me server gjendet në filen serverGUI.py. Përmes emrit te hostit, që në rastin tonë është localhost ose permes IP adressess dhe numrit të portit i cili duhet të jetë i njejte në të gjitha filet, mundesohet konektimi i klienteve me serverin. Tek pjesa e clientGUI.py dhe clientGUI2.py kemi pjesën ku fillimisht shkruhet mesazhi, enkriptohet end-to-end dhe përmes serverGUI.py dërgohet tek klienti tjetër.
Për enkriptim kemi perdorur llojin e enkriptimit FERNET e cili na mundeson enkriptimin e mesazheve të dërguara te serveri pa pasur mundësi që ato mesazhe të përgjohen, pasi që për dekriptimin e tyre përdorim një qeles i cili gjenerohet duke perdorur librarinë e Fernet. Në këtë mënyre mesazhet e derguara bëhen më të sigurta për klientin, pasi që janë end-to-end encrypted. Pra nëse mesazhet që po transmetohen përmes serverit te klientat që i dërgojne ato mesazhe kapen on-the-air permes veglave të ndryshme përgjuese do te jetë shum problem që të dekriptohet përmbajtja e paketave (mesazheve) që dërgohen.

Test Case: Fillimisht hapen të gjitha filet. Pastaj vazhdohet me ekzekutimit të kodit në file-in serverGUI.py, që sinjalizon se këta dy klientë janë te gatshem për konektim. Pas kësaj hapet file clientGUI.py i cili përmban edhe pjesën e kodit në tkinter pra përmban GUI-n, kod ky i cili mundëson që dy klientat  që ishin të gatshem për tu lidhur paraprakisht, lidhen dhe kanë mundesine e dërgimit të mesazheve te njëri-tjetri. Pas shkrimit të mesazhit nga njëri ose tjetri klient në momentin e shtypjes së butonit SEND mesazhi enkriptohet përmes FERNET dhe si i tillë dërgohet te klienti tjëter. Në këtë mënyrë pra bëhet marrja dhe dergimi i mesazheve deri sa njeri prej klienteve vendos që të largohet nga chat-i(linja).

Note: Llogaritë agonmustafa1 dhe agonmustafa2 në github jane te personit tëv njejte, mirepo gabimisht është postuar kodi përmes dy llogarive të ndryshme.
