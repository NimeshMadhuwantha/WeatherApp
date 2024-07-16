from tkinter import *

from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import *
import requests
import pytz
from PIL import Image, ImageTk
import time

class weatherClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("700x400+325+150")
        self.root.title("Weather App")
        self.root.resizable(False,False)
        self.root.config(bg='white',bd=1)

        self.photo_image=ImageTk.PhotoImage(file="weather.jpg")
        self.lbl_photo_image=Label(self.root,image=self.photo_image,bd=0).place(x=0,y=0)


        self.var_city=StringVar()
        self.var_txtcity=StringVar()
        self.var_latitude=StringVar()
        self.var_tempreture=StringVar()
        self.var_humidity=StringVar()
        self.var_pressure=StringVar()
        self.var_wind=StringVar()
        self.var_des=StringVar()
        self.var_localtime=StringVar()

        self.var_textcity=Label(self.root,text="",font=("times 30 bold"),fg='black',bg="#08f7f7",justify=CENTER)
        self.var_textcity.place(x=0,y=70)

        self.var_latitude=Label(self.root,text="",font=("times 12 bold"),fg='black',bg="#08f7f7",justify=CENTER)
        self.var_latitude.place(x=0,y=70)

        self.var_tempreture=Label(self.root,text="",font=("times 40 bold"),fg='black',bg="#08f7f7",justify=CENTER)
        self.var_tempreture.place(x=20,y=150)

        self.var_localtime=Label(self.root,text="",font=("times 15 bold"),fg='black',bg="#08f7f7",justify=CENTER)
        self.var_localtime.place(x=165,y=220,width=150)

        self.var_des=Label(self.root,text="",font=("times 14 bold"),fg='black',bg="#08f7f7",justify=CENTER)
        self.var_des.place(x=80,y=330)

        self.var_wind=Label(self.root,text="",font=("times 14 bold"),fg='black',bg="#08f7f7",justify=CENTER)
        self.var_wind.place(x=220,y=330)

        self.var_humidity=Label(self.root,text="",font=("times 14 bold"),fg='black',bg="#08f7f7",justify=CENTER)
        self.var_humidity.place(x=300,y=330)

        self.var_pressure=Label(self.root,text="",font=("times 14 bold"),fg='black',bg="#08f7f7",justify=CENTER)
        self.var_pressure.place(x=400,y=330)


        #lable

        label1=Label(self.root,text="DESCRIPTION",font=("times 10 bold"),fg='white',bg="#4c7b7b").place(x=80,y=307)
        label2=Label(self.root,text="WIND",font=("times 10 bold"),fg='white',bg="#4c7b7b").place(x=220,y=307)
        label3=Label(self.root,text="HUMIDITY",font=("times 10 bold"),fg='white',bg="#4c7b7b").place(x=300,y=307)
        label4=Label(self.root,text="PRESSURE",font=("times 10 bold"),fg='white',bg="#4c7b7b").place(x=400,y=307)
        

        textfield=Entry(self.root,textvariable=self.var_city,justify=CENTER,width=15,font=("times 25 bold"),bg='#545a5a',fg='white',bd=0)
        textfield.place(x=383,y=35,width=225)
        textfield.focus()



if __name__=="__main__":
    root=Tk()
    obj=weatherClass(root)
    root.mainloop()



