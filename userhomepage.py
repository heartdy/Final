
import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter.font import BOLD
import tkinter.messagebox
import sys
import os
import time
from PIL import Image,ImageTk

window2 = Tk()
window2.title("Booking Room")
window2.geometry("1079x720+500+150")
window2.iconbitmap('C:\Classroombooking-main\Education_KKU_Thai_Emblem.ico')
label=Label(window2,text="User",font=50)
label.pack(side=TOP,fill=X)
canvas = Canvas(window2, width = 1079, height = 720)
canvas.place(x=0,y=0,relwidth=1,relheight=1)
img = PhotoImage(file=r"C:\Classroombooking-main\images\งานออกแบบที่ไม่มีชื่อ.png")
canvas.create_image(0,0,anchor=NW,image=img)
img2 = PhotoImage(file="C:\Classroombooking-main\images\DDDDD.png")
canvas.create_image(830,150,anchor=NW,image=img2)
img3 = PhotoImage(file="C:\Classroombooking-main\images\Line_group_Guide.png")
canvas.create_image(790,340,anchor=NW,image=img3)

canvas.create_text(551,102,text='ยินดีต้อนรับสู่ระบบจองห้องเรียน',font=("MiPancake",40,BOLD),fill="#5D8D73")
canvas.create_text(550,100,text='ยินดีต้อนรับสู่ระบบจองห้องเรียน',font=("MiPancake",40,BOLD),fill="#D4E6C4")

canvas.create_text(351,182,text='เลือกห้องที่ต้องการจอง   ',font=("MiPancake",30,BOLD),fill="#5D8D73")
canvas.create_text(350,180,text='เลือกห้องที่ต้องการจอง   ',font=("MiPancake",30,BOLD),fill="#D4E6C4")

canvas.create_text(351,262,text='เลือกเวลาเริ่มที่ต้องการจอง',font=("MiPancake",30,BOLD),fill="#5D8D73")
canvas.create_text(350,260,text='เลือกเวลาเริ่มที่ต้องการจอง',font=("MiPancake",30,BOLD),fill="#D4E6C4")

canvas.create_text(351,342,text='เลือกเวลาที่ต้องการออก  ',font=("MiPancake",30,BOLD),fill="#5D8D73")
canvas.create_text(350,340,text='เลือกเวลาที่ต้องการออก  ',font=("MiPancake",30,BOLD),fill="#D4E6C4")

canvas.create_text(351,422,text='ดูห้องว่างก่อนจองนะครับ  ',font=("MiPancake",30,BOLD),fill="#5D8D73")
canvas.create_text(350,420,text='ดูห้องว่างก่อนจองนะครับ  ',font=("MiPancake",30,BOLD),fill="#D4E6C4")

list1 = ["2201","2202","2203","2204","2205","2206","2207","2208"]
listroom = StringVar(window2)
listroom = ttk.Combobox(window2, values=list1 , width=20 ,font=('MiPancake',14,BOLD),foreground="#567ACE",justify="center",state="readonly")
listroom.set("เลือกห้องที่ต้องการ")
listroom.place(x=580,y=160)

list2 = ["08:00","09:00","10:00","11:00","13:00","14:00","15:00","16:00","17:00","18:00","19:00"]
listStart = StringVar(window2)
listStart = ttk.Combobox(window2, values=list2 , width=20 ,font=('MiPancake',14,BOLD),foreground="#567ACE",justify="center",state="readonly")
listStart.set("เลือกเวลาเริ่มที่ต้องการ")
listStart.place(x=580,y=240)

list3 = ["09:00","10:00","11:00","12:00","14:00","15:00","16:00","17:00","18:00","19:00","20:00"]
listFinish = StringVar(window2)
listFinish = ttk.Combobox(window2, values=list3 , width=20 ,font=('MiPancake',14,BOLD),foreground="#567ACE",justify="center",state="readonly")
listFinish.set("เลือกเวลาออกที่ต้องการ")
listFinish.place(x=580,y=320)

def BookingSaved() :
    if listStart.get() < listFinish.get() :
        if listroom.get() != "เลือกห้องที่ต้องการ" and listStart.get() != "เลือกเวลาเริ่มที่ต้องการ" and listFinish.get() != "เลือกเวลาออกที่ต้องการ" :
            if listStart.get() <= "11:00" and listFinish.get() <= "12:00":

                if "Available" == listFinish[0] :
                    pass
                else :
                    tkinter.messagebox.showinfo("ED KKU Room reservation","จองไม่สำเร็จนะครับ \nโปรดเช็คข้อมูลห้องว่างอีกครั้ง")
            elif listStart.get() >= "13:00" and listFinish.get() > "13:00":
                
                if "Available" != listFinish[0] :
                    tkinter.messagebox.showinfo("ED KKU Room reservation","จองสำเร็จแล้วนะครับ \nอย่าลืมปิดไฟปิดแอร์ก่อนออกจากห้องด้วยนะครับ")
                else :
                    tkinter.messagebox.showinfo("ED KKU Room reservation","จองไม่สำเร็จนะครับ \nโปรดเช็คข้อมูลห้องว่างอีกครั้ง")
            else :
                tkinter.messagebox.showinfo("ED KKU Room reservation","สามารถจองช่วงเช้าได้ถึง 12:00")
        else :
            print("Error")
            tkinter.messagebox.showinfo("ED KKU Room reservation","จองไม่สำเร็จนะครับ \nโปรดกรอกข้อมูลให้ครบท้วน")
    else :
        tkinter.messagebox.showinfo("ED KKU Room reservation","จองไม่สำเร็จนะครับ \nโปรดกรอกเวลาให้ถูกต้อง")

def ShowTable() :
    Userpage = "C:\Classroombooking-main\ShowBookedTable.py"
    os.system(Userpage)

def logout() :
    window2.destroy()
    Return = "C:\Classroombooking-main\login.py"
    os.system(Return)

def CheckTimeOut() :
    pass
logo = PhotoImage(file="C:\Classroombooking-main\images\Show_table_button.png")
logo2 = PhotoImage(file="C:\Classroombooking-main\images\Refresh_button.png")
logo3= PhotoImage(file="C:\Classroombooking-main\images\Save_booking_Button1.png")
logo4 = PhotoImage(file="C:\Classroombooking-main\images\log_out_button.png")
img4 = PhotoImage(file="C:\Classroombooking-main\images\Guide_User.png")
btn = Button(window2,image=logo,bg="#D9598C",command=ShowTable).place(x=580,y=400)
btn = Button(window2,image=logo2,bg="#567ACE",command=CheckTimeOut).place(x=580,y=480)
btn = Button(window2,image=logo3,bg="#B7D3E9",command=BookingSaved).place(x=580,y=560)
btn = Button(window2,image=logo4,bg="#FF1616",command=logout).place(x=950,y=70)
canvas.create_image(50,440,anchor=NW,image=img4)
window2.resizable(False, False)
window2.mainloop()
