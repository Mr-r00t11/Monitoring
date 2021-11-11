from tkinter import PhotoImage
from PIL import Image,ImageTk
from pygame import mixer
import tkinter as tk
import webbrowser
import threading
import requests
import datetime
import getpass
import hashlib
import base64
import time
import os

print("""
  _____  _   _   _ _____ _____ _   _ _____ _____                             
 |_   _|/ \ | | | |_   _| ____| \ | | ____|_   _|                            
   | | / _ \| | | | | | |  _| |  \| |  _|   | |                              
   | |/ ___ \ |_| | | | | |___| |\  | |___  | |                              
  _|_/_/  _\_\___/__|_| |_____|_| \_|_____|_|_| ___ ___  _   _    _    _     
 |_ _| \ | |_   _| ____|  _ \| \ | |  / \|_   _|_ _/ _ \| \ | |  / \  | |    
  | ||  \| | | | |  _| | |_) |  \| | / _ \ | |  | | | | |  \| | / _ \ | |    
  | || |\  | | | | |___|  _ <| |\  |/ ___ \| |  | | |_| | |\  |/ ___ \| |___ 
 |___|_| \_| |_| |_____|_| \_\_| \_/_/   \_\_| |___\___/|_| \_/_/   \_\_____|
""")
h = getpass.getpass("Password >> ")
p = hashlib.sha256(h.encode('ascii')).hexdigest()
if p == '34072f4123400033b3f1a888e93008ac536b4c72a8e6ad8d8980ca5f8dd780a3':
        mute2 = 0
        mute3 = 0
        mute4 = 0
        mute5 = 0
        mute6 = 0
        mute7 = 0
        mute8 = 0
        mute9 = 0
        mute10 = 0
        mute11 = 0
        mute12 = 0
        mute13 = 0
        mute14 = 0
        mute15 = 0
        mute16 = 0
        mute17 = 0
        mute18 = 0
        mute19 = 0
        mute20 = 0
        mute21 = 0
        mute22 = 0
        mute23 = 0
        mute24 = 0

        contador = 0

        root = tk.Tk()
        root.iconbitmap('TN.ico')
        root.title('PyMonitor')
        root.resizable(False, False)
        root.geometry('250x588')
        root.config(bg='navy')
        img = Image.open('Mute.png')
        img = img.resize((15,15), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)

        etiqueta = tk.Label(root, text='WALMART', fg='White',
                        bg='navy', font=("Eras Demi ITC", 20, 'bold'))
        etiqueta.pack(fill=tk.BOTH)
        etiqueta.bind("<Button-1>", lambda e: callback("log.txt"))

        etiqueta2 = tk.Label(root, text='SMO', fg='White',
                        bg='steel blue', font=("Eras Demi ITC", 17, 'bold'))
        etiqueta2.place(x=0, y=38, width=215, height=25)
        etiqueta2.bind("<Button-1>", lambda e: callback("https://10.164.210.29/"))

        etiqueta3 = tk.Label(root, text='SMO-DR ', fg='White',
                        bg='steel blue', font=("Eras Demi ITC", 17, 'bold'))
        etiqueta3.place(x=0, y=63, width=215, height=25)
        etiqueta3.bind("<Button-1>", lambda e: callback("https://10.164.210.38/"))

        etiqueta4 = tk.Label(root, text='CHALCO', fg='White',
                        bg='steel blue', font=("Eras Demi ITC", 17, 'bold'))
        etiqueta4.place(x=0, y=88, width=215, height=25)
        etiqueta4.bind("<Button-1>", lambda e: callback("https://10.157.2.30/"))

        etiqueta5 = tk.Label(root, text='CHALCO-DR', fg='White',
                        bg='steel blue', font=("Eras Demi ITC", 17, 'bold'))
        etiqueta5.place(x=0, y=113, width=215, height=25)
        etiqueta5.bind("<Button-1>", lambda e: callback("https://10.157.2.38/"))

        etiqueta6 = tk.Label(root, text='SNT BARBARA', fg='White',
                        bg='steel blue', font=("Eras Demi ITC", 17, 'bold'))
        etiqueta6.place(x=0, y=138, width=215, height=25)
        etiqueta6.bind("<Button-1>", lambda e: callback("https://10.164.234.30/"))

        etiqueta7 = tk.Label(root, text='SNT BARBARA-DR', fg='White',
                        bg='steel blue', font=("Eras Demi ITC", 17, 'bold'))
        etiqueta7.place(x=0, y=163, width=215, height=25)
        etiqueta7.bind("<Button-1>", lambda e: callback("https://10.164.234.38/"))

        etiqueta8 = tk.Label(root, text='CUAUTITLAN', fg='White',
                        bg='steel blue', font=("Eras Demi ITC", 17, 'bold'))
        etiqueta8.place(x=0, y=188, width=215, height=25)
        etiqueta8.bind("<Button-1>", lambda e: callback("https://10.164.243.30/"))

        etiqueta9 = tk.Label(root, text='CUAUTITLAN-DR', fg='White',
                        bg='steel blue', font=("Eras Demi ITC", 17, 'bold'))
        etiqueta9.place(x=0, y=213, width=215, height=25)
        etiqueta9.bind("<Button-1>", lambda e: callback("https://10.164.243.38/"))

        etiqueta10 = tk.Label(root, text='MANAGER', fg='White',
                        bg='steel blue', font=("Eras Demi ITC", 17, 'bold'))
        etiqueta10.place(x=0, y=238, width=215, height=25)
        etiqueta10.bind("<Button-1>", lambda e: callback("https://148.250.80.219/"))

        etiqueta11 = tk.Label(root, text='AZCAPO', fg='White',
                        bg='steel blue', font=("Eras Demi ITC", 17, 'bold'))
        etiqueta11.place(x=0, y=263, width=215, height=25)
        etiqueta11.bind("<Button-1>", lambda e: callback("https://148.250.31.133/"))

        etiqueta12 = tk.Label(root, text='AZCAPO-DR', fg='White',
                        bg='steel blue', font=("Eras Demi ITC", 17, 'bold'))
        etiqueta12.place(x=0, y=288, width=215, height=25)
        etiqueta12.bind("<Button-1>", lambda e: callback("https://148.250.31.134/"))

        etiqueta13 = tk.Label(root, text='TOREO', fg='White',
                        bg='steel blue', font=("Eras Demi ITC", 17, 'bold'))
        etiqueta13.place(x=0, y=313, width=215, height=25)
        etiqueta13.bind("<Button-1>", lambda e: callback("https://148.250.181.95/"))

        etiqueta14 = tk.Label(root, text='Toreo-DR', fg='White',
                        bg='steel blue', font=("Eras Demi ITC", 17, 'bold'))
        etiqueta14.place(x=0, y=338, width=215, height=25)
        etiqueta14.bind("<Button-1>", lambda e: callback("https://148.250.181.115/"))

        #PEERS AND GIGA
        etiqueta15 = tk.Label(root, text='GIGA AZC', fg='White',
                        bg='steel blue', font=("Eras Demi ITC", 17, 'bold'))
        etiqueta15.place(x=0, y=363, width=215, height=25)
        etiqueta15.bind("<Button-1>", lambda e: callback("https://gigamonazcsec/"))

        etiqueta16 = tk.Label(root, text='GIGA TOREO', fg='White',
                        bg='steel blue', font=("Eras Demi ITC", 17, 'bold'))
        etiqueta16.place(x=0, y=388, width=215, height=25)
        etiqueta16.bind("<Button-1>", lambda e: callback("https://gigamontorsec/"))

        etiqueta17 = tk.Label(root, text='TRIPWIRE', fg='White',
                        bg='steel blue', font=("Eras Demi ITC", 17, 'bold'))
        etiqueta17.place(x=0, y=413, width=215, height=25)
        etiqueta17.bind("<Button-1>", lambda e: callback("https://gigamontorsec/"))

        etiqueta18 = tk.Label(root, text='SPLUNK AZC', fg='White',
                        bg='steel blue', font=("Eras Demi ITC", 17, 'bold'))
        etiqueta18.place(x=0, y=438, width=215, height=25)
        etiqueta18.bind("<Button-1>", lambda e: callback("https://gigamontorsec/"))

        etiqueta19 = tk.Label(root, text='SPLUNK TOREO', fg='White',
                        bg='steel blue', font=("Eras Demi ITC", 17, 'bold'))
        etiqueta19.place(x=0, y=463, width=215, height=25)
        etiqueta19.bind("<Button-1>", lambda e: callback("https://gigamontorsec/"))

        etiqueta20 = tk.Label(root, text='MASTER NODE', fg='White',
                        bg='steel blue', font=("Eras Demi ITC", 17, 'bold'))
        etiqueta20.place(x=0, y=488, width=215, height=25)
        etiqueta20.bind("<Button-1>", lambda e: callback("https://gigamontorsec/"))

        etiqueta21 = tk.Label(root, text='PEER NODE 1', fg='White',
                        bg='steel blue', font=("Eras Demi ITC", 17, 'bold'))
        etiqueta21.place(x=0, y=513, width=215, height=25)
        etiqueta21.bind("<Button-1>", lambda e: callback("https://gigamontorsec/"))

        etiqueta22 = tk.Label(root, text='PEER NODE 2', fg='White',
                        bg='steel blue', font=("Eras Demi ITC", 17, 'bold'))
        etiqueta22.place(x=0, y=538, width=215, height=25)
        etiqueta22.bind("<Button-1>", lambda e: callback("https://gigamontorsec/"))

        etiqueta23 = tk.Label(root, text='PEER NODE 3', fg='White',
                        bg='steel blue', font=("Eras Demi ITC", 17, 'bold'))
        etiqueta23.place(x=0, y=563, width=215, height=25)
        etiqueta23.bind("<Button-1>", lambda e: callback("https://gigamontorsec/"))

        etiqueta24 = tk.Label(root, text='SEARCH HEAD', fg='White',
                        bg='steel blue', font=("Eras Demi ITC", 17, 'bold'))
        etiqueta24.place(x=0, y=588, width=215, height=25)
        etiqueta24.bind("<Button-1>", lambda e: callback("https://gigamontorsec/"))

        def callback(url):
                webbrowser.open_new(url)

        def my_mainloop():
                global contador

                def Stop2():       
                        global contador
                        global mute2
                        mute2 = 1
                        contador = contador -1
                        pass
                def Stop3():      
                        global contador
                        global mute3
                        mute3 = 1
                        contador = contador -1
                        pass
                def Stop4():    
                        global contador
                        global mute4
                        mute4 = 1
                        contador = contador -1
                        pass
                def Stop5():   
                        global contador
                        global mute5
                        mute5 = 1
                        contador = contador -1
                        pass
                def Stop6():   
                        global contador
                        global mute6
                        mute6 = 1
                        contador = contador -1
                        pass
                def Stop7():     
                        global contador
                        global mute7
                        mute7 = 1
                        contador = contador -1
                        pass
                def Stop8():        
                        global contador
                        global mute8
                        mute8 = 1
                        contador = contador -1
                        pass
                def Stop9():         
                        global contador
                        global mute9
                        mute9 = 1
                        contador = contador -1
                        pass
                def Stop10():     
                        global contador
                        global mute10
                        mute10 = 1
                        contador = contador -1
                        pass
                def Stop11():     
                        global contador
                        global mute11
                        mute11 = 1
                        contador = contador -1
                        pass
                def Stop12():  
                        global contador
                        global mute12
                        mute12 = 1
                        contador = contador -1
                        pass
                def Stop13():  
                        global contador
                        global mute13
                        mute13 = 1
                        contador = contador -1
                        pass
                def Stop14():
                        global contador
                        global mute14
                        mute14 = 1
                        contador = contador -1
                        pass
                def Stop15():            
                        global contador
                        global mute15
                        mute15 = 1
                        contador = contador -1
                        pass
                def Stop16():            
                        global contador
                        global mute16
                        mute16 = 1
                        contador = contador -1
                        pass
                def Stop17():            
                        global contador
                        global mute17
                        mute17 = 1
                        contador = contador -1
                        pass
                def Stop18():            
                        global contador
                        global mute18
                        mute18 = 1
                        contador = contador -1
                        pass
                def Stop19():            
                        global contador
                        global mute19
                        mute19 = 1
                        contador = contador -1
                        pass
                
                def Stop20():            
                        global contador
                        global mute20
                        mute20 = 1
                        contador = contador -1
                        pass
                def Stop21():            
                        global contador
                        global mute21
                        mute21 = 1
                        contador = contador -1
                        pass
                def Stop22():            
                        global contador
                        global mute22
                        mute22 = 1
                        contador = contador -1
                        pass
                def Stop23():            
                        global contador
                        global mute23
                        mute23 = 1
                        contador = contador -1
                        pass
                def Stop24():            
                        global contador
                        global mute23
                        mute23 = 1
                        contador = contador -1
                        pass
                
                boton2 = tk.Button(root, image=img, command=Stop2).place(x=222, y=40)
                boton3 = tk.Button(root, image=img, command=Stop3).place(x=222, y=65)
                boton4 = tk.Button(root, image=img, command=Stop4).place(x=222, y=90)
                boton5 = tk.Button(root, image=img, command=Stop5).place(x=222, y=115)
                boton6 = tk.Button(root, image=img, command=Stop6).place(x=222, y=140)
                boton7 = tk.Button(root, image=img, command=Stop7).place(x=222, y=165)
                boton8 = tk.Button(root, image=img, command=Stop8).place(x=222, y=190)
                boton9 = tk.Button(root, image=img, command=Stop9).place(x=222, y=215)
                boton10 = tk.Button(root, image=img, command=Stop10).place(x=222, y=240)
                boton11 = tk.Button(root, image=img, command=Stop11).place(x=222, y=265)
                boton12 = tk.Button(root, image=img, command=Stop12).place(x=222, y=290)
                boton13 = tk.Button(root, image=img, command=Stop13).place(x=222, y=315)
                boton14 = tk.Button(root, image=img, command=Stop14).place(x=222, y=340)
                boton15 = tk.Button(root, image=img, command=Stop15).place(x=222, y=365)
                boton16 = tk.Button(root, image=img, command=Stop16).place(x=222, y=390)
                boton17 = tk.Button(root, image=img, command=Stop17).place(x=222, y=415)
                boton18 = tk.Button(root, image=img, command=Stop18).place(x=222, y=440)
                boton19 = tk.Button(root, image=img, command=Stop19).place(x=222, y=465)
                boton20 = tk.Button(root, image=img, command=Stop20).place(x=222, y=490)
                boton21 = tk.Button(root, image=img, command=Stop21).place(x=222, y=515)
                boton22 = tk.Button(root, image=img, command=Stop22).place(x=222, y=540)
                boton23 = tk.Button(root, image=img, command=Stop23).place(x=222, y=565)
                boton23 = tk.Button(root, image=img, command=Stop23).place(x=222, y=590)
                
                #2
                def SMO():
                        global mute2
                        global contador
                        if mute2 == 1:
                                try:
                                        r_g = requests.get('https://10.164.210.29/', verify=False)
                                        url = (b"https://10.164.210.29")
                                        if r_g.status_code == 200:
                                                etiqueta2.config(bg='Green')
                                                mute2 = 0
                                                os.system("cls")
                                                pass
                                except:
                                        etiqueta2.config(bg='darkgoldenrod1')
                                        pass
                        else:         
                                try:
                                        r_g = requests.get('https://10.164.210.29/', verify=False)
                                        url = (b"https://10.164.210.29/fsum/")
                                        if r_g.status_code == 200:
                                                etiqueta2.config(bg='Green')
                                                
                                                alive = 'Up'
                                                value = r_g.status_code
                                                encrypt = base64.b64encode(url)
                                                date = datetime.datetime.now()
                                                file = open('log.txt', 'a')
                                                file.write(str(encrypt) + " " + str(date) +
                                                        " status: " + str(alive)  + " Appliance: " + "SMO" + "\n")
                                                file.close()
                                                os.system("cls")
                                                pass
                                except requests.exceptions.ConnectionError:
                                        contador = contador + 1
                                        etiqueta2.config(bg='red4')
                                        url = (b"https://10.164.210.29/")
                                        alive = 'Down'
                                        encrypt = base64.b64encode(url)
                                        date = datetime.datetime.now()
                                        file = open('log.txt', 'a')
                                        file.write(str(encrypt) + " " + str(date) +
                                                " status: " + str(alive) + " Appliance: " + "SMO" + "\n")
                                        file.close()
                                        os.system("cls")
                                        pass
                #3
                def SMO_DR():
                        global mute3
                        global contador
                        if mute3 == 1:
                                try:
                                        r_g = requests.get('https://10.164.210.38/', verify=False)
                                        url = (b"https://10.164.210.38/")
                                        if r_g.status_code == 200:
                                                etiqueta3.config(bg='Green')
                                                mute3 = 0
                                                os.system("cls")
                                                pass
                                except:
                                        etiqueta3.config(bg='darkgoldenrod1')
                                        pass
                        else:         
                                try:
                                        r_g = requests.get('https://10.164.210.38/', verify=False)
                                        url = (b"https://10.164.210.38/")
                                        if r_g.status_code == 200:
                                                etiqueta3.config(bg='Green')
                                                
                                                alive = 'Up'
                                                value = r_g.status_code
                                                encrypt = base64.b64encode(url)
                                                date = datetime.datetime.now()
                                                file = open('log.txt', 'a')
                                                file.write(str(encrypt) + " " + str(date) +
                                                        " status: " + str(alive)  + " Appliance: " + "SMO DR" + "\n")
                                                file.close()
                                                os.system("cls")
                                                pass
                                except requests.exceptions.ConnectionError:
                                        contador = contador + 1
                                        etiqueta3.config(bg='red4')
                                        url = (b"https://10.164.210.38/")
                                        alive = 'Down'
                                        encrypt = base64.b64encode(url)
                                        date = datetime.datetime.now()
                                        file = open('log.txt', 'a')
                                        file.write(str(encrypt) + " " + str(date) +
                                                " status: " + str(alive)  + " Appliance: " + "SMO DR" + "\n")
                                        file.close()
                                        os.system("cls")
                                        pass
                #4
                def CHALCO():
                        global mute4
                        global contador
                        if mute4 == 1:
                                try:
                                        r_g = requests.get('https://10.157.2.30/', verify=False)
                                        url = (b"https://10.157.2.30/fsum/")
                                        if r_g.status_code == 200:
                                                etiqueta4.config(bg='Green')
                                                mute4 = 0
                                                os.system("cls")
                                                pass
                                except:
                                        etiqueta4.config(bg='darkgoldenrod1')
                                        pass
                        else:         
                                try:
                                        r_g = requests.get('https://10.157.2.30/', verify=False)
                                        url = (b"https://10.157.2.30/fsum/")
                                        if r_g.status_code == 200:
                                                etiqueta4.config(bg='Green')
                                                
                                                alive = 'Up'
                                                value = r_g.status_code
                                                encrypt = base64.b64encode(url)
                                                date = datetime.datetime.now()
                                                file = open('log.txt', 'a')
                                                file.write(str(encrypt) + " " + str(date) +
                                                        " status: " + str(alive)  + " Appliance: " + "CHALCO" + "\n")
                                                file.close()
                                                os.system("cls")
                                                pass
                                except requests.exceptions.ConnectionError:
                                        contador = contador + 1
                                        etiqueta4.config(bg='red4')
                                        url = (b"https://10.157.2.30/")
                                        alive = 'Down'
                                        encrypt = base64.b64encode(url)
                                        date = datetime.datetime.now()
                                        file = open('log.txt', 'a')
                                        file.write(str(encrypt) + " " + str(date) +
                                                " status: " + str(alive)  + " Appliance: " + "CHALCO" + "\n")
                                        file.close()
                                        os.system("cls")
                                        pass
                #5
                def CHALCO_DR():
                        global mute5
                        global contador
                        if mute5 == 1:
                                try:
                                        r_g = requests.get('https://10.157.2.38/', verify=False)
                                        url = (b"https://10.157.2.38/")
                                        if r_g.status_code == 200:
                                                etiqueta5.config(bg='Green')
                                                mute5 = 0
                                                os.system("cls")
                                                pass
                                except:
                                        etiqueta5.config(bg='darkgoldenrod1')
                                        pass
                        else:         
                                try:
                                        r_g = requests.get('https://10.157.2.38/', verify=False)
                                        url = (b"https://10.157.2.38/")
                                        if r_g.status_code == 200:
                                                etiqueta5.config(bg='Green')
                                                alive = 'Up'
                                                value = r_g.status_code
                                                encrypt = base64.b64encode(url)
                                                date = datetime.datetime.now()
                                                file = open('log.txt', 'a')
                                                file.write(str(encrypt) + " " + str(date) +
                                                        " status: " + str(alive)  + " Appliance: " + "CHALCO DR" +  "\n")
                                                file.close()
                                                os.system("cls")
                                                pass
                                except requests.exceptions.ConnectionError:
                                        contador = contador + 1
                                        etiqueta5.config(bg='red4')
                                        url = (b"https://10.157.2.38/")
                                        alive = 'Down'
                                        encrypt = base64.b64encode(url)
                                        date = datetime.datetime.now()
                                        file = open('log.txt', 'a')
                                        file.write(str(encrypt) + " " + str(date) +
                                                " status: " + str(alive)  + " Appliance: " + "CHALCO DR" +  "\n")
                                        file.close()
                                        os.system("cls")
                                        pass
                #6
                def SANTA_BARBARA():
                        global mute6
                        global contador
                        if mute6 == 1:
                                try:
                                        r_g = requests.get('https://10.164.234.30/', verify=False)
                                        url = (b"https://10.164.234.30/")
                                        if r_g.status_code == 200:
                                                etiqueta6.config(bg='Green')
                                                mute6 = 0
                                                os.system("cls")
                                                pass
                                except:
                                        etiqueta6.config(bg='darkgoldenrod1')
                                        pass
                        else:         
                                try:
                                        r_g = requests.get('https://10.164.234.30/', verify=False)
                                        url = (b"https://10.164.234.30/")
                                        if r_g.status_code == 200:
                                                etiqueta6.config(bg='Green')
                                                
                                                alive = 'Up'
                                                value = r_g.status_code
                                                encrypt = base64.b64encode(url)
                                                date = datetime.datetime.now()
                                                file = open('log.txt', 'a')
                                                file.write(str(encrypt) + " " + str(date) +
                                                        " status: " + str(alive)  + " Appliance: " + "SANTA BARBARA" +  "\n")
                                                file.close()
                                                os.system("cls")
                                                pass
                                except requests.exceptions.ConnectionError:
                                        contador = contador + 1
                                        etiqueta6.config(bg='red4')
                                        url = (b"https://10.164.234.30/")
                                        alive = 'Down'
                                        encrypt = base64.b64encode(url)
                                        date = datetime.datetime.now()
                                        file = open('log.txt', 'a')
                                        file.write(str(encrypt) + " " + str(date) +
                                                " status: " + str(alive)  + " Appliance: " + "SANTA BARBARA" +  "\n")
                                        file.close()
                                        os.system("cls")
                                        pass
                #7
                def SANTA_BARBARA_DR():
                        global mute7
                        global contador
                        if mute7 == 1:
                                try:
                                        r_g = requests.get('https://10.164.234.38/', verify=False)
                                        url = (b"https://10.164.234.38/")
                                        if r_g.status_code == 200:
                                                etiqueta7.config(bg='Green')
                                                mute7 = 0
                                                os.system("cls")
                                                pass
                                except:
                                        etiqueta7.config(bg='darkgoldenrod1')
                                        pass
                        else:         
                                try:
                                        r_g = requests.get('https://10.164.234.38/', verify=False)
                                        url = (b"https://10.164.234.38/")
                                        if r_g.status_code == 200:
                                                etiqueta7.config(bg='Green')
                                                
                                                alive = 'Up'
                                                value = r_g.status_code
                                                encrypt = base64.b64encode(url)
                                                date = datetime.datetime.now()
                                                file = open('log.txt', 'a')
                                                file.write(str(encrypt) + " " + str(date) +
                                                        " status: " + str(alive)  + " Appliance: " + "SANTA BARBARA DR" +  "\n")
                                                file.close()
                                                os.system("cls")
                                                pass
                                except requests.exceptions.ConnectionError:
                                        contador = contador + 1
                                        etiqueta7.config(bg='red4')
                                        url = (b"https://10.164.234.38/")
                                        alive = 'Down'
                                        encrypt = base64.b64encode(url)
                                        date = datetime.datetime.now()
                                        file = open('log.txt', 'a')
                                        file.write(str(encrypt) + " " + str(date) +
                                                " status: " + str(alive)  + " Appliance: " + "SANTA BARBARA DR" +  "\n")
                                        file.close()
                                        os.system("cls")
                                        pass
                #8
                def CUAUTITLAN():
                        global mute8
                        global contador
                        if mute8 == 1:
                                try:
                                        r_g = requests.get('https://10.164.243.30/', verify=False)
                                        url = (b"https://10.164.243.30/")
                                        if r_g.status_code == 200:
                                                etiqueta8.config(bg='Green')
                                                mute8 = 0
                                                os.system("cls")
                                                pass
                                except:
                                        etiqueta8.config(bg='darkgoldenrod1')
                                        pass
                        else:         
                                try:
                                        r_g = requests.get('https://10.164.243.30/', verify=False)
                                        url = (b"https://10.164.243.30/")
                                        if r_g.status_code == 200:
                                                etiqueta8.config(bg='Green')
                                                
                                                alive = 'Up'
                                                value = r_g.status_code
                                                encrypt = base64.b64encode(url)
                                                date = datetime.datetime.now()
                                                file = open('log.txt', 'a')
                                                file.write(str(encrypt) + " " + str(date) +
                                                        " status: " + str(alive)   + " Appliance: " + "CUAUTITLAN" + "\n")
                                                file.close()
                                                os.system("cls")
                                                pass
                                except requests.exceptions.ConnectionError:
                                        contador = contador + 1
                                        etiqueta8.config(bg='red4')
                                        url = (b"https://10.164.243.30/")
                                        alive = 'Down'
                                        encrypt = base64.b64encode(url)
                                        date = datetime.datetime.now()
                                        file = open('log.txt', 'a')
                                        file.write(str(encrypt) + " " + str(date) +
                                                " status: " + str(alive)   + " Appliance: " + "CUAUTITLAN" + "\n")
                                        file.close()
                                        os.system("cls")
                                        pass
                #9
                def CUAUTITLAN_DR():
                        global mute9
                        global contador
                        if mute9 == 1:
                                try:
                                        r_g = requests.get('https://10.164.243.38/', verify=False)
                                        url = (b"https://10.164.243.38/")
                                        if r_g.status_code == 200:
                                                etiqueta9.config(bg='Green')
                                                mute9 = 0
                                                os.system("cls")
                                                pass
                                except:
                                        etiqueta9.config(bg='darkgoldenrod1')
                                        pass
                        else:         
                                try:
                                        r_g = requests.get('https://10.164.243.38/', verify=False)
                                        url = (b"https://10.164.243.38/")
                                        if r_g.status_code == 200:
                                                etiqueta9.config(bg='Green')
                                                
                                                alive = 'Up'
                                                value = r_g.status_code
                                                encrypt = base64.b64encode(url)
                                                date = datetime.datetime.now()
                                                file = open('log.txt', 'a')
                                                file.write(str(encrypt) + " " + str(date) +
                                                        " status: " + str(alive)    + " Appliance: " + "CUAUTITLAN DR" +  "\n")
                                                file.close()
                                                os.system("cls")
                                                pass
                                except requests.exceptions.ConnectionError:
                                        contador = contador + 1
                                        etiqueta9.config(bg='red4')
                                        url = (b"https://10.164.243.38/")
                                        alive = 'Down'
                                        encrypt = base64.b64encode(url)
                                        date = datetime.datetime.now()
                                        file = open('log.txt', 'a')
                                        file.write(str(encrypt) + " " + str(date) +
                                                " status: " + str(alive)    + " Appliance: " + "CUAUTITLAN DR" +  "\n")
                                        file.close()
                                        os.system("cls")
                                        pass

#10
                def MANAGER():
                        global mute10
                        global contador
                        if mute10 == 1:
                                try:
                                        r_g = requests.get('https://148.250.80.219/', verify=False)
                                        url = (b"https://148.250.80.219/")
                                        if r_g.status_code == 200:
                                                etiqueta10.config(bg='Green')
                                                mute10 = 0
                                                os.system("cls")
                                                pass
                                except:
                                        etiqueta10.config(bg='darkgoldenrod1')
                                        pass
                        else:         
                                try:
                                        r_g = requests.get('https://148.250.80.219/', verify=False)
                                        url = (b"https://148.250.80.219/")
                                        if r_g.status_code == 200:
                                                etiqueta10.config(bg='Green')
                                                alive = 'Up'
                                                value = r_g.status_code
                                                encrypt = base64.b64encode(url)
                                                date = datetime.datetime.now()
                                                file = open('log.txt', 'a')
                                                file.write(str(encrypt) + " " + str(date) +
                                                        " status: " + str(alive)    + " Appliance: " + "MANAGER" +  "\n")
                                                file.close()
                                                os.system("cls")
                                                pass
                                except requests.exceptions.ConnectionError:
                                        contador = contador + 1
                                        etiqueta10.config(bg='red4')
                                        url = (b"https://148.250.80.219/")
                                        alive = 'Down'
                                        encrypt = base64.b64encode(url)
                                        date = datetime.datetime.now()
                                        file = open('log.txt', 'a')
                                        file.write(str(encrypt) + " " + str(date) +
                                                " status: " + str(alive)    + " Appliance: " + "MANAGER" +  "\n")
                                        file.close()
                                        os.system("cls")
                                        pass
#11
                def AZCAPOTZALCO():
                        global mute11
                        global contador
                        if mute11 == 1:
                                try:
                                        r_g = requests.get('https://148.250.31.133/', verify=False)
                                        url = (b"https://148.250.31.133/")
                                        if r_g.status_code == 200:
                                                etiqueta11.config(bg='Green')
                                                mute11 = 0
                                                os.system("cls")
                                                pass
                                except:
                                        etiqueta11.config(bg='darkgoldenrod1')
                                        pass
                        else:         
                                try:
                                        r_g = requests.get('https://148.250.31.133/', verify=False)
                                        url = (b"https://148.250.31.133/")
                                        if r_g.status_code == 200:
                                                etiqueta11.config(bg='Green')
                                                
                                                alive = 'Up'
                                                value = r_g.status_code
                                                encrypt = base64.b64encode(url)
                                                date = datetime.datetime.now()
                                                file = open('log.txt', 'a')
                                                file.write(str(encrypt) + " " + str(date) +
                                                        " status: " + str(alive)    + " Appliance: " + "AZCAPOTZALCO" +  "\n")
                                                file.close()
                                                os.system("cls")
                                                pass
                                except requests.exceptions.ConnectionError:
                                        contador = contador + 1
                                        etiqueta11.config(bg='red4')
                                        url = (b"https://148.250.31.133/")
                                        alive = 'Down'
                                        encrypt = base64.b64encode(url)
                                        date = datetime.datetime.now()
                                        file = open('log.txt', 'a')
                                        file.write(str(encrypt) + " " + str(date) +
                                                " status: " + str(alive)    + " Appliance: " + "AZCAPOTZALCO" +  "\n")
                                        file.close()
                                        os.system("cls")
                                        pass
#12
                def AZCAPOTZALCO_DR():
                        global mute12
                        global contador
                        if mute12 == 1:
                                try:
                                        r_g = requests.get('https://148.250.31.134/', verify=False)
                                        url = (b"https://148.250.31.134/")
                                        if r_g.status_code == 200:
                                                etiqueta12.config(bg='Green')
                                                mute12 = 0
                                                os.system("cls")
                                                pass
                                except:
                                        etiqueta12.config(bg='darkgoldenrod1')
                                        pass
                        else:         
                                try:
                                        r_g = requests.get('https://148.250.31.134/', verify=False)
                                        url = (b"https://148.250.31.134/")
                                        if r_g.status_code == 200:
                                                etiqueta12.config(bg='Green')
                                                
                                                alive = 'Up'
                                                value = r_g.status_code
                                                encrypt = base64.b64encode(url)
                                                date = datetime.datetime.now()
                                                file = open('log.txt', 'a')
                                                file.write(str(encrypt) + " " + str(date) +
                                                        " status: " + str(alive)    + " Appliance: " + "AZCAPOTZALCO DR" +  "\n")
                                                file.close()
                                                os.system("cls")
                                                pass
                                except requests.exceptions.ConnectionError:
                                        contador = contador + 1
                                        etiqueta12.config(bg='red4')
                                        url = (b"https://148.250.31.134/")
                                        alive = 'Down'
                                        encrypt = base64.b64encode(url)
                                        date = datetime.datetime.now()
                                        file = open('log.txt', 'a')
                                        file.write(str(encrypt) + " " + str(date) +
                                                " status: " + str(alive)    + " Appliance: " + "AZCAPOTZALCO DR" +  "\n")
                                        file.close()
                                        os.system("cls")
                                        pass
#13
                def TOREO():
                        global mute13
                        global contador
                        if mute13 == 1:
                                try:
                                        r_g = requests.get('https://148.250.181.95/', verify=False)
                                        url = (b"https://148.250.181.95/")
                                        if r_g.status_code == 200:
                                                etiqueta13.config(bg='Green')
                                                mute13 = 0
                                                os.system("cls")
                                                pass
                                except:
                                        etiqueta13.config(bg='darkgoldenrod1')
                                        pass
                        else:         
                                try:
                                        r_g = requests.get('https://148.250.181.95/', verify=False)
                                        url = (b"https://148.250.181.95/")
                                        if r_g.status_code == 200:
                                                etiqueta13.config(bg='Green')
                                                
                                                alive = 'Up'
                                                value = r_g.status_code
                                                encrypt = base64.b64encode(url)
                                                date = datetime.datetime.now()
                                                file = open('log.txt', 'a')
                                                file.write(str(encrypt) + " " + str(date) +
                                                        " status: " + str(alive)    + " Appliance: " + "TOREO" +  "\n")
                                                file.close()
                                                os.system("cls")
                                                pass
                                except requests.exceptions.ConnectionError:
                                        contador = contador + 1
                                        etiqueta13.config(bg='red4')
                                        url = (b"https://148.250.181.95/")
                                        alive = 'Down'
                                        encrypt = base64.b64encode(url)
                                        date = datetime.datetime.now()
                                        file = open('log.txt', 'a')
                                        file.write(str(encrypt) + " " + str(date) +
                                                " status: " + str(alive)    + " Appliance: " + "TOREO" +  "\n")
                                        file.close()
                                        os.system("cls")
                                        pass
                def TOREO_DR():
                        global mute14
                        global contador
                        if mute14 == 1:
                                try:
                                        r_g = requests.get('https://148.250.181.115/', verify=False)
                                        url = (b"https://148.250.181.115/")
                                        if r_g.status_code == 200:
                                                etiqueta14.config(bg='Green')
                                                mute14 = 0
                                                os.system("cls")
                                                pass
                                except:
                                        etiqueta14.config(bg='darkgoldenrod1')
                                        pass
                        else:         
                                try:
                                        r_g = requests.get('https://148.250.181.115/', verify=False)
                                        url = (b"https://148.250.181.115/")
                                        if r_g.status_code == 200:
                                                etiqueta14.config(bg='Green')
                                                
                                                alive = 'Up'
                                                value = r_g.status_code
                                                encrypt = base64.b64encode(url)
                                                date = datetime.datetime.now()
                                                file = open('log.txt', 'a')
                                                file.write(str(encrypt) + " " + str(date) +
                                                        " status: " + str(alive)    + " Appliance: " + "TOREO_DR" +  "\n")
                                                file.close()
                                                os.system("cls")
                                                pass
                                except requests.exceptions.ConnectionError:
                                        contador = contador + 1
                                        etiqueta14.config(bg='red4')
                                        url = (b"https://148.250.181.115/")
                                        alive = 'Down'
                                        encrypt = base64.b64encode(url)
                                        date = datetime.datetime.now()
                                        file = open('log.txt', 'a')
                                        file.write(str(encrypt) + " " + str(date) +
                                                " status: " + str(alive)    + " Appliance: " + "TOREO_DR" +  "\n")
                                        file.close()
                                        os.system("cls")
                                        pass

#15
                def GIGA_AZC():
                        global mute15
                        global contador
                        if mute15 == 1:
                                try:
                                        r_g = requests.get('https://gigamonazcsec/', verify=False)
                                        url = (b"https://gigamonazcsec.mx.wal-mart.com/")
                                        if r_g.status_code == 200:
                                                etiqueta15.config(bg='Green')
                                                mute15 = 0
                                                os.system("cls")
                                                pass
                                except:
                                        etiqueta15.config(bg='darkgoldenrod1')
                                        pass
                        else:         
                                try:
                                        r_g = requests.get('https://gigamonazcsec/', verify=False)
                                        url = (b"https://gigamonazcsec.mx.wal-mart.com/")
                                        if r_g.status_code == 200:
                                                etiqueta15.config(bg='Green')
                                                
                                                alive = 'Up'
                                                value = r_g.status_code
                                                encrypt = base64.b64encode(url)
                                                date = datetime.datetime.now()
                                                file = open('log.txt', 'a')
                                                file.write(str(encrypt) + " " + str(date) +
                                                        " status: " + str(alive) + " Appliance: " + "GIGA AZC" +  "\n")
                                                file.close()
                                                os.system("cls")
                                                pass
                                except requests.exceptions.ConnectionError:
                                        contador = contador + 1
                                        etiqueta15.config(bg='red4')
                                        url = (b"https://gigamonazcsec/")
                                        alive = 'Down'
                                        encrypt = base64.b64encode(url)
                                        date = datetime.datetime.now()
                                        file = open('log.txt', 'a')
                                        file.write(str(encrypt) + " " + str(date) +
                                                " status: " + str(alive) + " Appliance: " + "GIGA AZC" +  "\n")
                                        file.close()
                                        os.system("cls")
                                        pass
                #16
                def GIGA_TOREO():
                        global mute16
                        global contador
                        if mute16 == 1:
                                try:
                                        r_g = requests.get('https://gigamontorsec/', verify=False)
                                        url = (b"https://gigamontorsec.mx.wal-mart.com/")
                                        if r_g.status_code == 200:
                                                etiqueta16.config(bg='Green')
                                                mute16 = 0
                                                os.system("cls")
                                                pass
                                except:
                                        etiqueta16.config(bg='darkgoldenrod1')
                                        pass
                        else:         
                                try:
                                        r_g = requests.get('https://gigamontorsec/', verify=False)
                                        url = (b"https://gigamontorsec.mx.wal-mart.com/")
                                        if r_g.status_code == 200:
                                                etiqueta16.config(bg='Green')
                                                
                                                alive = 'Up'
                                                value = r_g.status_code
                                                encrypt = base64.b64encode(url)
                                                date = datetime.datetime.now()
                                                file = open('log.txt', 'a')
                                                file.write(str(encrypt) + " " + str(date) +
                                                        " status: " + str(alive) + " Appliance: " + "GIGA TOREO" + "\n")
                                                file.close()
                                                os.system("cls")
                                                pass
                                except requests.exceptions.ConnectionError:
                                        contador = contador + 1
                                        etiqueta16.config(bg='red4')
                                        url = (b"https://gigamontorsec/")
                                        alive = 'Down'
                                        encrypt = base64.b64encode(url)
                                        date = datetime.datetime.now()
                                        file = open('log.txt', 'a')
                                        file.write(str(encrypt) + " " + str(date) +
                                                " status: " + str(alive) + " Appliance: " + "GIGA TOREO" + "\n")
                                        file.close()
                                        os.system("cls")
                                        pass
                #17
                def TRIPWIRE():
                        global mute17
                        global contador
                        if mute17 == 1:
                                try:
                                        r_g = requests.get('https://mxnts1167/', verify=False)
                                        url = (b"https://mxnts1167/")
                                        if r_g.status_code == 200:
                                                etiqueta17.config(bg='Green')
                                                mute17 = 0
                                                os.system("cls")
                                                pass
                                except:
                                        etiqueta17.config(bg='darkgoldenrod1')
                                        pass
                        else:         
                                try:
                                        r_g = requests.get('https://mxnts1167/', verify=False)
                                        url = (b"https://mxnts1167/")
                                        if r_g.status_code == 200:
                                                etiqueta17.config(bg='Green')
                                                alive = 'Up'
                                                value = r_g.status_code
                                                encrypt = base64.b64encode(url)
                                                date = datetime.datetime.now()
                                                file = open('log.txt', 'a')
                                                file.write(str(encrypt) + " " + str(date) +
                                                        " status: " + str(alive)     + " Appliance: " + "TRIPWIRE" +   "\n")
                                                file.close()
                                                os.system("cls")
                                                pass
                                except requests.exceptions.ConnectionError:
                                        contador = contador + 1
                                        etiqueta17.config(bg='red4')
                                        url = (b"https://mxnts1167/")
                                        alive = 'Down'
                                        encrypt = base64.b64encode(url)
                                        date = datetime.datetime.now()
                                        file = open('log.txt', 'a')
                                        file.write(str(encrypt) + " " + str(date) +
                                                " status: " + str(alive)     + " Appliance: " + "TRIPWIRE" +   "\n")
                                        file.close()
                                        os.system("cls")
                                        pass
                #18
                def SPLUNK_AZC():
                        global mute18
                        global contador
                        if mute18 == 1:
                                try:
                                        r_g = requests.get('https://mxnts1167/', verify=False)
                                        url = (b"https://mxnts1167/")
                                        if r_g.status_code == 200:
                                                etiqueta18.config(bg='Green')
                                                mute18 = 0
                                                os.system("cls")
                                                pass
                                except:
                                        etiqueta18.config(bg='darkgoldenrod1')
                                        pass
                        else:         
                                try:
                                        r_g = requests.get('https://mxnts1167/', verify=False)
                                        url = (b"https://mxnts1167/")
                                        if r_g.status_code == 200:
                                                etiqueta18.config(bg='Green')
                                                
                                                alive = 'Up'
                                                value = r_g.status_code
                                                encrypt = base64.b64encode(url)
                                                date = datetime.datetime.now()
                                                file = open('log.txt', 'a')
                                                file.write(str(encrypt) + " " + str(date) +
                                                        " status: " + str(alive)     + " Appliance: " + "SPLUNK AZC" +   "\n")
                                                file.close()
                                                os.system("cls")
                                                pass
                                except requests.exceptions.ConnectionError:
                                        contador = contador + 1
                                        etiqueta18.config(bg='red4')
                                        url = (b"https://mxnts1167/")
                                        alive = 'Down'
                                        encrypt = base64.b64encode(url)
                                        date = datetime.datetime.now()
                                        file = open('log.txt', 'a')
                                        file.write(str(encrypt) + " " + str(date) +
                                                " status: " + str(alive)     + " Appliance: " + "SPLUNK AZC" +   "\n")
                                        file.close()
                                        os.system("cls")
                                        pass
                #19
                def SPLUNK_TOREO():
                        global mute19
                        global contador
                        if mute19 == 1:
                                try:
                                        r_g = requests.get('https://mxnts1167/', verify=False)
                                        url = (b"https://mxnts1167/")
                                        if r_g.status_code == 200:
                                                etiqueta19.config(bg='Green')
                                                mute19 = 0
                                                os.system("cls")
                                                pass
                                except:
                                        etiqueta19.config(bg='darkgoldenrod1')
                                        pass
                        else:         
                                try:
                                        r_g = requests.get('https://mxnts1167/', verify=False)
                                        url = (b"https://mxnts1167/")
                                        if r_g.status_code == 200:
                                                etiqueta19.config(bg='Green')
                                                
                                                alive = 'Up'
                                                value = r_g.status_code
                                                encrypt = base64.b64encode(url)
                                                date = datetime.datetime.now()
                                                file = open('log.txt', 'a')
                                                file.write(str(encrypt) + " " + str(date) +
                                                        " status: " + str(alive) + " Appliance: " + "SPLUNK TOREO" +   "\n")
                                                file.close()
                                                os.system("cls")
                                                pass
                                except requests.exceptions.ConnectionError:
                                        contador = contador + 1
                                        etiqueta19.config(bg='red4')
                                        url = (b"https://mxnts1167/")
                                        alive = 'Down'
                                        encrypt = base64.b64encode(url)
                                        date = datetime.datetime.now()
                                        file = open('log.txt', 'a')
                                        file.write(str(encrypt) + " " + str(date) +
                                                " status: " + str(alive)     + " Appliance: " + "SPLUNK TOREO" +   "\n")
                                        file.close()
                                        os.system("cls")
                                        pass
                #20
                def MASTER_NODE():
                        global mute20
                        global contador
                        if mute20 == 1:
                                try:
                                        r_g = requests.get('https://mxnts1167/', verify=False)
                                        url = (b"https://mxnts1167/")
                                        if r_g.status_code == 200:
                                                etiqueta20.config(bg='Green')
                                                mute20 = 0
                                                os.system("cls")
                                                pass
                                except:
                                        etiqueta20.config(bg='darkgoldenrod1')
                                        pass
                        else:         
                                try:
                                        r_g = requests.get('https://mxnts1167/', verify=False)
                                        url = (b"https://mxnts1167/")
                                        if r_g.status_code == 200:
                                                etiqueta20.config(bg='Green')
                                                alive = 'Up'
                                                value = r_g.status_code
                                                encrypt = base64.b64encode(url)
                                                date = datetime.datetime.now()
                                                file = open('log.txt', 'a')
                                                file.write(str(encrypt) + " " + str(date) +
                                                        " status: " + str(alive)     + " Appliance: " + "MASTER NODE" +   "\n")
                                                file.close()
                                                os.system("cls")
                                                pass
                                except requests.exceptions.ConnectionError:
                                        contador = contador + 1
                                        etiqueta20.config(bg='red4')
                                        url = (b"https://mxnts1167/")
                                        alive = 'Down'
                                        encrypt = base64.b64encode(url)
                                        date = datetime.datetime.now()
                                        file = open('log.txt', 'a')
                                        file.write(str(encrypt) + " " + str(date) +
                                                " status: " + str(alive)     + " Appliance: " + "MASTER NODE" +   "\n")
                                        file.close()
                                        os.system("cls")
                                        pass

                #21
                def PEER_NODE1():
                        global mute21
                        global contador
                        if mute21 == 1:
                                try:
                                        r_g = requests.get('https://mxnts1167/', verify=False)
                                        url = (b"https://mxnts1167/")
                                        if r_g.status_code == 200:
                                                etiqueta21.config(bg='Green')
                                                mute21 = 0
                                                os.system("cls")
                                                pass
                                except:
                                        etiqueta21.config(bg='darkgoldenrod1')
                                        pass
                        else:         
                                try:
                                        r_g = requests.get('https://mxnts1167/', verify=False)
                                        url = (b"https://mxnts1167/")
                                        if r_g.status_code == 200:
                                                etiqueta21.config(bg='Green')
                                                alive = 'Up'
                                                value = r_g.status_code
                                                encrypt = base64.b64encode(url)
                                                date = datetime.datetime.now()
                                                file = open('log.txt', 'a')
                                                file.write(str(encrypt) + " " + str(date) +
                                                        " status: " + str(alive)     + " Appliance: " + "PEER NODE 1" +   "\n")
                                                file.close()
                                                os.system("cls")
                                                pass
                                except requests.exceptions.ConnectionError:
                                        contador = contador + 1
                                        etiqueta21.config(bg='red4')
                                        url = (b"https://mxnts1167/")
                                        alive = 'Down'
                                        encrypt = base64.b64encode(url)
                                        date = datetime.datetime.now()
                                        file = open('log.txt', 'a')
                                        file.write(str(encrypt) + " " + str(date) +
                                                " status: " + str(alive)     + " Appliance: " + "PEER NODE 1" +   "\n")
                                        file.close()
                                        os.system("cls")
                                        pass
                #22
                def PEER_NODE2():
                        global mute22
                        global contador
                        if mute22 == 1:
                                try:
                                        r_g = requests.get('https://mxnts1167/', verify=False)
                                        url = (b"https://mxnts1167/")
                                        if r_g.status_code == 200:
                                                etiqueta22.config(bg='Green')
                                                mute22 = 0
                                                os.system("cls")
                                                pass
                                except:
                                        etiqueta22.config(bg='darkgoldenrod1')
                                        pass
                        else:         
                                try:
                                        r_g = requests.get('https://mxnts1167/', verify=False)
                                        url = (b"https://mxnts1167/")
                                        if r_g.status_code == 200:
                                                etiqueta22.config(bg='Green')
                                                alive = 'Up'
                                                value = r_g.status_code
                                                encrypt = base64.b64encode(url)
                                                date = datetime.datetime.now()
                                                file = open('log.txt', 'a')
                                                file.write(str(encrypt) + " " + str(date) +
                                                        " status: " + str(alive)     + " Appliance: " + "PEER NODE 2" +   "\n")
                                                file.close()
                                                os.system("cls")
                                                pass
                                except requests.exceptions.ConnectionError:
                                        contador = contador + 1
                                        etiqueta22.config(bg='red4')
                                        url = (b"https://mxnts1167/")
                                        alive = 'Down'
                                        encrypt = base64.b64encode(url)
                                        date = datetime.datetime.now()
                                        file = open('log.txt', 'a')
                                        file.write(str(encrypt) + " " + str(date) +
                                                " status: " + str(alive)     + " Appliance: " + "PEER NODE 2" +   "\n")
                                        file.close()
                                        os.system("cls")
                                        pass
                #23
                def PEER_NODE3():
                        global mute23
                        global contador
                        if mute23 == 1:
                                try:
                                        r_g = requests.get('https://mxnts1167/', verify=False)
                                        url = (b"https://oser503721.mx.wal-mart.com:8000/en-US/account/login?return_to=%2Fen-US%2F/")
                                        if r_g.status_code == 200:
                                                etiqueta23.config(bg='Green')
                                                mute23 = 0
                                                os.system("cls")
                                                pass
                                except:
                                        etiqueta23.config(bg='darkgoldenrod1')
                                        pass
                        else:         
                                try:
                                        r_g = requests.get('https://mxnts1167/', verify=False)
                                        url = (b"https://mxnts1167/")
                                        if r_g.status_code == 200:
                                                etiqueta23.config(bg='Green')
                                                alive = 'Up'
                                                value = r_g.status_code
                                                encrypt = base64.b64encode(url)
                                                date = datetime.datetime.now()
                                                file = open('log.txt', 'a')
                                                file.write(str(encrypt) + " " + str(date) +
                                                        " status: " + str(alive)     + " Appliance: " + "PEER NODE 3" +   "\n")
                                                file.close()
                                                os.system("cls")
                                                pass
                                except requests.exceptions.ConnectionError:
                                        contador = contador + 1
                                        etiqueta23.config(bg='red4')
                                        url = (b"https://mxnts1167/")
                                        alive = 'Down'
                                        encrypt = base64.b64encode(url)
                                        date = datetime.datetime.now()
                                        file = open('log.txt', 'a')
                                        file.write(str(encrypt) + " " + str(date) +
                                                " status: " + str(alive)     + " Appliance: " + "PEER NODE 3" +   "\n")
                                        file.close()
                                        os.system("cls")
                                        pass
                #24
                def SEARCH_HEAD():
                        global mute24
                        global contador
                        if mute24 == 1:
                                try:
                                        r_g = requests.get('https://mxnts1167/', verify=False)
                                        url = (b"https://mxnts1167/")
                                        if r_g.status_code == 200:
                                                etiqueta24.config(bg='Green')
                                                mute24 = 0
                                                os.system("cls")
                                                pass
                                except:
                                        etiqueta24.config(bg='darkgoldenrod1')
                                        pass
                        else:         
                                try:
                                        r_g = requests.get('https://mxnts1167/', verify=False)
                                        url = (b"https://mxnts1167/")
                                        if r_g.status_code == 200:
                                                etiqueta24.config(bg='Green')
                                                alive = 'Up'
                                                value = r_g.status_code
                                                encrypt = base64.b64encode(url)
                                                date = datetime.datetime.now()
                                                file = open('log.txt', 'a')
                                                file.write(str(encrypt) + " " + str(date) +
                                                        " status: " + str(alive)     + " Appliance: " + "SEARCH HEAD" +   "\n")
                                                file.close()
                                                os.system("cls")
                                                pass
                                except requests.exceptions.ConnectionError:
                                        contador = contador + 1
                                        etiqueta24.config(bg='red4')
                                        url = (b"https://mxnts1167/")
                                        alive = 'Down'
                                        encrypt = base64.b64encode(url)
                                        date = datetime.datetime.now()
                                        file = open('log.txt', 'a')
                                        file.write(str(encrypt) + " " + str(date) +
                                                " status: " + str(alive)     + " Appliance: " + "SEARCH HEAD" +   "\n")
                                        file.close()
                                        os.system("cls")
                                        pass

                thread2 = threading.Thread(target=SMO)
                thread2.start()
                thread3 = threading.Thread(target=SMO_DR)
                thread3.start()
                thread4 = threading.Thread(target=CHALCO)
                thread4.start()
                thread5 = threading.Thread(target=CHALCO_DR)
                thread5.start()
                thread6 = threading.Thread(target=SANTA_BARBARA)
                thread6.start()
                thread7 = threading.Thread(target=SANTA_BARBARA_DR)
                thread7.start()
                thread8 = threading.Thread(target=CUAUTITLAN)
                thread8.start()
                thread9 = threading.Thread(target=CUAUTITLAN_DR)
                thread9.start()
                thread10 = threading.Thread(target=MANAGER)
                thread10.start()
                thread11 = threading.Thread(target=AZCAPOTZALCO)
                thread11.start()
                thread12 = threading.Thread(target=AZCAPOTZALCO_DR)
                thread12.start()
                thread13 = threading.Thread(target=TOREO)
                thread13.start()
                thread14 = threading.Thread(target=TOREO_DR)
                thread14.start()
                thread15 = threading.Thread(target=GIGA_AZC)
                thread15.start()
                thread16 = threading.Thread(target=GIGA_TOREO)
                thread16.start()
                thread17 = threading.Thread(target=TRIPWIRE)
                thread17.start()
                thread18 = threading.Thread(target=SPLUNK_AZC)
                thread18.start()
                thread19 = threading.Thread(target=SPLUNK_TOREO)
                thread19.start()
                thread20 = threading.Thread(target=MASTER_NODE)
                thread20.start()
                thread21 = threading.Thread(target=PEER_NODE1)
                thread21.start()
                thread22 = threading.Thread(target=PEER_NODE2)
                thread22.start()
                thread23 = threading.Thread(target=PEER_NODE3)
                thread23.start()
                thread24 = threading.Thread(target=SEARCH_HEAD)
                thread24.start()
                if  contador >= 1:
                        mixer.init()
                        mixer.music.load("sound.wav")
                        mixer.music.play()
                        pass
                contador = 0

                root.after(50000, my_mainloop)

        if __name__ == '__main__':
                root.after(0000, my_mainloop)
                root.mainloop()
else:
        print('Password incorrect')
        time.sleep(2)
