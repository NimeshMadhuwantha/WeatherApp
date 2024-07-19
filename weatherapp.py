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
        self.var_textcity.place(x=0,y=50)

        self.var_latitude=Label(self.root,text="",font=("times 12 bold"),fg='black',bg="#08f7f7",justify=CENTER)
        self.var_latitude.place(x=0,y=110)

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

        #search button

        self.search_icon=PhotoImage(file="searchbtn.png")
        self.myimage_icon=Button(self.root,image=self.search_icon,borderwidth=0,command=self.getweather,cursor='hand2',bg='#203243',activebackground='#203243')
        self.myimage_icon.place(x=612,y=40)

    def getweather(self):
        try:
            city=self.var_city.get()

            geolocator=Nominatim(user_agent='geopiExercises')
            location=geolocator.geocode(city)
            obj=TimezoneFinder()

            result = obj.timezone_at(lng=location.longitude,lat=location.latitude)
            self.var_textcity.config(text=f"{result}")
            self.var_latitude.config(text=f"{round(location.latitude,4)}°N,{round(location.longitude,4)}°E")

            #local time

            home=pytz.timezone(result)
            local_time=datetime.now(home)
            current_time=local_time.strftime("%I:%M:%p")

            #request date
            #api="https://api.openweathermap.org/data/2.5/weather?q="+ city + "&appid=2d3b475655aa2d47bfa802b7103caff8"
            api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=2d3b475655aa2d47bfa802b7103caff8"
            weather_data=requests.get(api).json()

            condition=weather_data['weather'][0]['main']
            description=weather_data['weather'][0]['description']
            temp=int(weather_data['main']['temp'] -273.15)
            pressure=weather_data['main']['pressure']
            humidity=weather_data['main']['humidity']
            wind=weather_data['wind']['speed']

            #maindata

            self.var_tempreture.config(text=f"{condition}\n{str(temp)}°C")
            self.var_localtime.config(text=f"{local_time}\n{current_time}")
            self.var_des.config(text=f"{description}")
            self.var_wind.config(text=f"{wind}")
            self.var_humidity.config(text=f"{humidity}")
            self.var_pressure.config(text=f"{pressure}")

            if condition =='Rain':
                print(condition=='Rain')
                self.weather_image=PhotoImage(file="rain.png")
                self.sign_image=Label(self.root,image=self.weather_image,bg='#203243',bd=0).place(x=450,y=100)
            elif condition == 'Clouds':
                self.weather_image=PhotoImage(file="cloudy.png")
                self.sign_image=Label(self.root,image=self.weather_image,bg='#203243',bd=0).place(x=450,y=100)
            elif condition == 'Clear':
                self.weather_image=PhotoImage(file="clear.png")
                self.sign_image=Label(self.root,image=self.weather_image,bg='#203243',bd=0).place(x=450,y=100)
            elif condition == 'Overcast':
                self.weather_image=PhotoImage(file="overcast.png")
                self.sign_image=Label(self.root,image=self.weather_image,bg='#203243',bd=0).place(x=450,y=100)
            elif condition == 'Smoke':
                self.weather_image=PhotoImage(file="smoke.png")
                self.sign_image=Label(self.root,image=self.weather_image,bg='#203243',bd=0).place(x=450,y=100)
            elif condition == 'Haze':
                self.weather_image=PhotoImage(file="haze.png")
                self.sign_image=Label(self.root,image=self.weather_image,bg='#203243',bd=0).place(x=450,y=100)
            elif condition == 'Mist':
                self.weather_image=PhotoImage(file="Mist.png")
                self.sign_image=Label(self.root,image=self.weather_image,bg='#203243',bd=0).place(x=450,y=100)
            elif condition == 'Snow':
                self.weather_image=PhotoImage(file="snow.png")
                self.sign_image=Label(self.root,image=self.weather_image,bg='#203243',bd=0).place(x=450,y=100)
                

            
        







        except Exception as e:
            messagebox.showerror("Weather app", "Invalid Entry.....!")
            print(e)

    

if __name__=="__main__":
    root=Tk()
    obj=weatherClass(root)
    root.mainloop()



