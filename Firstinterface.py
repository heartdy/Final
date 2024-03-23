import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter.font import BOLD
import tkinter.messagebox
from PIL import Image,ImageTk
import sys
import os


window = Tk()
window.title("Booking Room")
window.geometry("1079x720+500+150")
window.iconbitmap("C:\Classroombooking-main\Education_KKU_Thai_Emblem.ico")
def JumpToRegister() :
    window.destroy()
    register = "C:\Classroombooking-main\register.py"
    os.system(register)
    
def JumpTologin() :
    window.destroy()
    Return = "C:\Classroombooking-main\login.py"
    os.system(Return)
logo = PhotoImage(file="C:\Classroombooking-main\images\Register_Button.png")
logo2 = PhotoImage(file="C:\Classroombooking-main\images\Login_Button.png")
canvas = Canvas(window, width = 1079, height = 720)
canvas.place(x=0,y=0,relwidth=1,relheight=1)
img = PhotoImage(file="C:\Classroombooking-main\images\งานออกแบบที่ไม่มีชื่อ.png")
img2 = PhotoImage(file="C:\Classroombooking-main\images\Guide.png")
canvas.create_image(0,0,anchor=NW,image=img)
canvas.create_text(551,102,text='Welcome to Classroom Booking',font=("MiPancake",40,BOLD),fill="white")
canvas.create_text(550,100,text='Welcome to Classroom Booking',font=("MiPancake",40,BOLD),fill="#FFAE80")

canvas.create_text(551,182,text='จัดทำโดย',font=("MiPancake",30,BOLD),fill="white")
canvas.create_text(550,180,text='จัดทำโดย',font=("MiPancake",30,BOLD),fill="#FFAE80")

canvas.create_text(551,242,text='นายเวชพิสิฐ ตรีพิพิธ 663450354-9',font=("MiPancake",30,BOLD),fill="white")
canvas.create_text(550,240,text='นายเวชพิสิฐ ตรีพิพิธ 663450354-9',font=("MiPancake",30,BOLD),fill="#FFAE80")


canvas.create_text(301,542,text='ลงทะเบียนสมาชิกใหม่',font=("MiPancake",30,BOLD),fill="white")
canvas.create_text(300,540,text='ลงทะเบียนสมาชิกใหม่',font=("MiPancake",30,BOLD),fill="#FF916C")

canvas.create_text(221,602,text='เข้าสู่ระบบ',font=("MiPancake",30,BOLD),fill="white")
canvas.create_text(220,600,text='เข้าสู่ระบบ',font=("MiPancake",30,BOLD),fill="#FF916C")

canvas.create_image(740,400,anchor=NW,image=img2)
mybutton = Button(window,image=logo,bg="#F1C3AB",command=JumpToRegister,padx=70,pady=7).place(x=550,y=520)
mybutton = Button(window,image=logo2,bg="#F1C3AB",command=JumpTologin,padx=70,pady=7).place(x=550,y=580)

window.resizable(False, False)
window.mainloop()
