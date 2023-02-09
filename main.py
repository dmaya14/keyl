import random
import threading
import time
import os
import txtstr
from win10toast import ToastNotifier
from tkinter import *
from tkinter import filedialog
import customtkinter
import tkinter
from datetime import datetime
import shutil


#Iniciar variables
txtstr.__init__()
toast = ToastNotifier()
textk = ""
textt=""


FOLDERNAME = "settings.txt"
try:
    os.remove(FOLDERNAME)
    txtstr.newtxt(FOLDERNAME)
except:
    pass

try:
    txtstr.newtxt(FOLDERNAME)
except:
    pass

#Funciones
def createkey():
    #GET TIME
    timename = str(datetime.now())
    #DELETE SECONDS
    timename = timename.split(".")
    #CONVERT TO STRING
    timename = str(timename[0])
    #DIVIDE SPACE FOR EDITING TEXT
    timename = timename.split(" ")
    #ADD INDICATORS
    timename = "d" + str(timename[0]) + "-t" + str(timename[1])
    #FINAL VAR
    timename = str(timename.replace(":","-"))

    namekeyy = "key" + timename

    keydirsave = filedialog.askdirectory(title="Select your folder for save your KEY")
    txtstr.newkey(namekeyy)
    tomovena = namekeyy + ".key"
    shutil.move(tomovena,keydirsave)


def selectyourkey():
    keydir = filedialog.askopenfile(filetypes=[("KeyL Files", "*.key")],title="Select your key")

    #GET ONLY THE NAME
    keydirs = str(keydir)
    keydirs = keydirs.split("'")
    keydir = keydirs[1]

    lines = txtstr.readlines(FOLDERNAME)
    try:
        text = keydir + "\n" + lines[1]

    except:
        text = keydir + "\n"
    txtstr.write(FOLDERNAME,text,False)

    #USE TAG
    dirkeyt.configure(state=NORMAL)
    dirkeyt.delete('1.0', END)
    dirkeyt.insert("0.0",keydir)
    dirkeyt.configure(state=DISABLED)


    return keydir

def readdir():
    directory = txtstr.readlines(FOLDERNAME)
    return directory

def selectyourtxt():
    lines = txtstr.readlines(FOLDERNAME)
    txtdir = filedialog.askopenfile(filetypes=[("TXT Files", "*.txt")],title="Select your file")
    print(txtdir)
    #GET ONLY THE NAME
    txtdir = str(txtdir)
    txtdir = txtdir.split("'")
    txtdir = txtdir[1]
    print(txtdir)

    try:
        text = lines[0]  +txtdir
    except:
        text = "\n" + txtdir

    txtstr.write(FOLDERNAME,text,False)

    #USE TAG
    dirtextt.configure(state=NORMAL)
    dirtextt.delete('1.0', END)
    dirtextt.insert("0.0",txtdir)
    dirtextt.configure(state=DISABLED)


def repair():
    os.remove(FOLDERNAME)
    txtstr.newtxt(FOLDERNAME)
    #CLEAN TAG
    dirkeyt.configure(state=NORMAL)
    dirkeyt.delete('1.0', END)
    dirkeyt.insert("0.0","")
    dirkeyt.configure(state=DISABLED)
    #CLEAN TAG
    dirtextt.configure(state=NORMAL)
    dirtextt.delete('1.0', END)
    dirtextt.insert("0.0","")
    dirtextt.configure(state=DISABLED)


def addconsole(text):
    console.configure(state=NORMAL,fg_color="#242424")
    console.delete("1.0",END)
    console.insert("0.0",str(text))
    console.configure(state=DISABLED,fg_color="#242424")

def encrypt():
    encryptbt.place(x=3000,y=3000)
    def run():
        lines=readdir()
        txtfile = lines[1]
        keyfile = lines[0]
        keyfile = keyfile.replace("\n","")
        timess = int(timetoen.get("1.0", "end"))
        print(timess)
        print(type(timess))

        if timess > 30:
            timess = 30
        if timess < 30:
            timess = timess

        addconsole("ENCRYPTING..... WAIT")
        time.sleep(4)
        txtstr.encrypt(txtfile,keyfile,timess)
        toast.show_toast("Your file is encrypted","KeyL",duration=5,icon_path="icono.ico",threaded = True)
        encryptbt.place(x=880,y=515)
        addconsole("READY...")
        time.sleep(2)
        addconsole("")


    t=threading.Thread(target=run)
    t.start()


def decrypt():
    decryptbt.place(x=3000,y=3000)
    def run():
        lines=readdir()
        txtfile = lines[1]
        keyfile = lines[0]
        keyfile = keyfile.replace("\n","")
        timess = int(timetoen.get("1.0", "end"))
        print(timess)
        print(type(timess))

        if timess > 30:
            timess = 30
        if timess < 30:
            timess = timess

        addconsole("DECRYPTING..... WAIT")
        time.sleep(4)
        try:
            txtstr.decrypt(txtfile,keyfile,timess)
            toast.show_toast("Your file is decrypted","KeyL",duration=5,icon_path="icono.ico",threaded = True)
            decryptbt.place(x=880,y=475)
            addconsole("READY...")
            time.sleep(2)
            addconsole("")
        except:
            addconsole("INVALID TOKEN OR TIMES NUMBER")
            toast.show_toast("INVALID TOKEN OR TIMES NUMBER","KeyL",duration=5,icon_path="icono.ico",threaded = True)
            time.sleep(3)
            decryptbt.place(x=880,y=475)
            addconsole("")
        


    t=threading.Thread(target=run)
    t.start()




#window
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")
app = customtkinter.CTk()
app.geometry("1100x580")
app.title("KeyL - By Pingüi")
app.iconbitmap("icono.ico")
app.resizable(False,False)
logo_label = customtkinter.CTkLabel(app, text="KeyL, encrypt and decrypt your files", font=customtkinter.CTkFont(size=30, weight="bold"))
logo_label.pack(pady=28)

name_label = customtkinter.CTkLabel(app, text="By Pingüi Maya", font=customtkinter.CTkFont(size=15, weight="normal"))
name_label.pack()
name_label.place(x=480,y=65)


#createyourkeyoption
createakey = customtkinter.CTkButton(app,text="Create your KEY to encrypt and decrypt your files",command=createkey)
#createakey.pack(side=tkinter.LEFT)
createakey.place(x=390,y=110)


#SELECT YOUR KEY DIR, BUTTON VIDEOS DIR, TEXTBOX DIRECTORY VIDEOS
indiconelabel = customtkinter.CTkLabel(app, text="1. Choose your KEY", font=customtkinter.CTkFont(size=22))

indiconelabel.pack(side=tkinter.LEFT)
indiconelabel.place(x=30,y=170)
#indiconelabel.place(anchor=tkinter.W)

videosdirbt = customtkinter.CTkButton(app,text="Change", command=selectyourkey)
videosdirbt.pack(side=tkinter.LEFT)
videosdirbt.place(x=30,y=220)

dirs=readdir()

try:
    textk = dirs[0]

except:
    textk = ""

dirkeyt = customtkinter.CTkTextbox(app, height=20,width=800)
dirkeyt.insert("0.0",textk)
dirkeyt.pack(side=tkinter.LEFT)
dirkeyt.place(x=180,y=220)
dirkeyt.configure(state=DISABLED)



processindic = customtkinter.CTkLabel(app, text="2. Choose the TXT file", font=customtkinter.CTkFont(size=22))
processindic.pack(side=tkinter.LEFT)
processindic.place(x=30,y=320)


processdir = customtkinter.CTkButton(app,text="Change",command=selectyourtxt)
processdir.pack(side=tkinter.LEFT)
processdir.place(x=30,y=360)


dirs=readdir()
try:
    textt = dirs[1]

except:
    textt=""



dirtextt = customtkinter.CTkTextbox(app, height=20,width=800)
dirtextt.insert("0.0",textt)
dirtextt.pack(side=tkinter.LEFT)
dirtextt.place(x=180,y=360)
dirtextt.configure(state=DISABLED)


#REPAIR APP
repairbt = customtkinter.CTkButton(app,text="REPAIR",command=repair)
repairbt.pack(side=tkinter.LEFT)
repairbt.place(x=20,y=535)
repairbt.configure(fg_color="#242424")

#TEXTBOX CONSOLE
console = customtkinter.CTkTextbox(app,height=20,width=800)
console.insert("0.0","")
console.pack(side=tkinter.LEFT)
console.place(x=170,y=465)
console.configure(state=DISABLED,fg_color="#242424")

#DECRYPT BUTTON
encryptbt = customtkinter.CTkButton(app,text="ENCRYPT", command=encrypt)
encryptbt.pack(side=tkinter.TOP)
encryptbt.place(x=880,y=515)

#ENCRYPT BUTTON
decryptbt = customtkinter.CTkButton(app,text="DECRYPT", command=decrypt)
decryptbt.pack(side=tkinter.TOP)
decryptbt.place(x=880,y=475)

#TIME TO ENCRYPT
timetoen = customtkinter.CTkTextbox(app,height=40,width=40)
timetoen.insert("0.0","14")
timetoen.pack(side=tkinter.LEFT)
timetoen.place(x=800,y=485)
timetoen.configure(state=NORMAL)

#TEXT TIME
textime = customtkinter.CTkLabel(app, text="3. Select the number of times:", font=customtkinter.CTkFont(size=18))
textime.pack(side=tkinter.LEFT)
textime.place(x=550,y=485)

app.mainloop()






