from tkinter import *
from gtts import gTTS
from playsound import playsound
from tkinter.messagebox import showinfo
import os

def popup_showinfo():
    showinfo("Error", "Hello there, Please insert the text!")

def Text_to_speech():
    message = entry_field.get()
    if message == "":
      popup_showinfo()
      return
    speech = gTTS(text = message)
    print()
    speech.save('test.mp3')
    playsound('test.mp3')
    os.remove("./test.mp3")

def Exit():
    root.destroy()

def Reset():
    Msg.set("")

root = Tk()
root.geometry("350x300") 
root.configure(bg='gray11')
root.title("CODEWITHFRED - Let's Text to Speech")

Label(root, text = "Insert Text, Output Speech", font = "helvetica 20 bold", bg='gray11',foreground="white").pack()
Label(text ="@Codewithfred", font = 'helvetica 15 bold', bg ='midnightblue' , width = '20',foreground="orchid1").pack(side = 'bottom')
Msg = StringVar()
Label(root,text ="Enter Text", font = 'helvetica 15 bold', bg='gray11',foreground="white").place(x=118,y=60)
entry_field = Entry(root, textvariable = Msg ,width ='50')
entry_field.place(x=20,y=100)

Button(root, text = "PLAY", font = 'helvetica 15 bold' , command = Text_to_speech ,width = '4').place(x=20,y=140)

Button(root, font = 'helvetica 15 bold',text = 'EXIT', width = '4' , command = Exit, bg = 'OrangeRed1').place(x=135, y = 140)

Button(root, font = 'helvetica 15 bold',text = 'RESET', width = '6' , command = Reset).place(x=243, y = 140)

root.mainloop()