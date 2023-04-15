import customtkinter
import datetime
import requests
from PIL import ImageTk, Image
from urllib.request import urlopen
from io import BytesIO
from PIL import Image, ImageTk
import json
import socket

apikey = ""

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk()
app.geometry("450x700")
app.title("Smart Thermostat")


def button_callback():
    #Sources
    #https://realpython.com/python-sockets/

    HOST = "172.20.10.4"  # Run ipconfig on this computer and grab ipv4 address
    PORT = 80  # The port used by the server (can be changed to anything not reserved)

    # initialize tcp connection
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(str(slider_1.get()).encode())
        s.sendall(b"\n")
    print(slider_1.get())
    c()
    
def b(value):
     costs_label.configure(text=str(slider_1.get()))
     label_9.configure(text = "")
     label_9.place(x=10, y=100)
     
def c():
   # label_9 = customtkinter.CTkLabel(master=frame_1, text="Temperature Set" ,text_color = "red", font = ("bold", 15))
    label_9.configure(text = "Temperature Set")
    label_9.place(x=10, y=100)



frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)

label_1 = customtkinter.CTkLabel(master=frame_1, text="Smart Thermostat" ,justify=customtkinter.LEFT)
label_1.pack(pady=10, padx=10)
label_9 = label_9 = customtkinter.CTkLabel(master=frame_1, text="" ,text_color = "red", font = ("bold", 15))
# Dates
dt = datetime.datetime.now()
date = customtkinter.CTkLabel(master=frame_1, text=dt.strftime('%A,'), font=("bold", 15))
date.place(x=5, y=200)
month = customtkinter.CTkLabel(master=frame_1, text=dt.strftime('%m %B'), font=("bold", 15))
month.place(x=100, y=200)
# Time
hour = customtkinter.CTkLabel(master=frame_1, text=dt.strftime('%I : %M %p'),
              font=("bold", 15))
hour.place(x=10, y=180)
costs_label2 = customtkinter.CTkLabel(master=frame_1,text="Temperature: ", font=("bold", 15))
costs_label2.pack()
costs_label = customtkinter.CTkLabel(master=frame_1,text="75.0", font = ("bold", 40))
costs_label.pack()

slider_1 = customtkinter.CTkSlider(master=frame_1, from_=60, to=90,command=b, hover=True, number_of_steps=30)
slider_1.pack(pady=10, padx=10)
slider_1.set(75)




button_1 = customtkinter.CTkButton(master=frame_1, text="Set Temperature",command=button_callback)
button_1.pack(pady=10, padx=10)


#weather

city_name = customtkinter.StringVar()
city_entry = customtkinter.CTkEntry(master=frame_1, textvariable=city_name, placeholder_text="Enter City", width=100)
city_entry.place(x = 10, y = 250)
  
  
def city_name():
  
    # API Call
    api_request = requests.get("https://api.openweathermap.org/data/2.5/weather?q="
                               + city_entry.get() + "&units=imperial&appid="+apikey)
  
    api = json.loads(api_request.content)
    print(api)
    # Temperatures
    y = api['main']
    current_temprature = y['temp']
    humidity = y['humidity']
    tempmin = y['temp_min']
    tempmax = y['temp_max']
  
    # Coordinates
    x = api['coord']
    # longtitude = x['lon']
    # latitude = x['lat']
  
    # map_widget = tkintermapview.CTkinterMapView(master=frame_1, width=300, height=200, corner_radius=0)
    # marker = map_widget.set_marker(longtitude, latitude, text=str(longtitude) + ", " + str(latitude))
    # map_widget.place(x=10, y = 700)

    # Country
    z = api['sys']
    country = z['country']
    citi = api['name']
  
    #weather icon

    wicon = api['weather'][0]['icon']
    print(wicon)

    url2 = "https://openweathermap.org/img/wn/04n@2x.png"  # replace with your API endpoint

    response = requests.get(url2)

    with open('weathericon2', 'wb') as f:
        f.write(response.content)

    img = Image.open('weathericon2')
    photo2 = ImageTk.PhotoImage(img)

    
    # Adding the received info into the screen
    lable_temp.configure(text=current_temprature)
    lable_humidity.configure(text=humidity)
    max_temp.configure(text=tempmax)
    min_temp.configure(text=tempmin)
    lable_country.configure(text=country)
    lable_citi.configure(text=citi)
    #label2.configure(image = photo2)
  


url = "https://openweathermap.org/img/wn/10d@2x.png"  # replace with your API endpoint

response = requests.get(url)

with open('weathericon2', 'wb') as f:
    f.write(response.content)

img = Image.open('weathericon2')
photo = ImageTk.PhotoImage(img)

# label2 = customtkinter.CTkLabel(master=frame_1, image=photo)
# label2.place(x = 200, y = 363)

# Search Bar and Button
city_nameButton = customtkinter.CTkButton(master=frame_1, text="Search", command=city_name, width = 70)
city_nameButton.place(x=120, y = 250)
  
  
# Country  Names and Coordinates
lable_citi = customtkinter.CTkLabel(master=frame_1, text="...", width=0, 
                    font=("bold", 15))
lable_citi.place(x=10, y=300)
  
lable_country = customtkinter.CTkLabel(master=frame_1, text="...", width=0, 
                       font=("bold", 15))
lable_country.place(x=135, y=300)
  

  
# Current Temperature
  
lable_thing = customtkinter.CTkLabel(master=frame_1, text="Current Outside Temp:", width=0, 
                   font=("Helvetica", 20))
lable_thing.place(x=18, y=360)
lable_temp = customtkinter.CTkLabel(master=frame_1, text="...", width=0, 
                   font=("Helvetica", 60))
lable_temp.place(x=18, y=390)
  
# Other temperature details
  
humi = customtkinter.CTkLabel(master=frame_1, text="Humidity: ", width=0, 
              font=("bold", 15))
humi.place(x=3, y=600)
  
lable_humidity = customtkinter.CTkLabel(master=frame_1, text="...", width=0,
                        font=("bold", 15))
lable_humidity.place(x=107, y=600)
  
  
maxi = customtkinter.CTkLabel(master=frame_1, text="Max. Temp.: ", width=0, 
              font=("bold", 15))
maxi.place(x=3, y=540)
  
max_temp = customtkinter.CTkLabel(master=frame_1, text="...", width=0, 
                  font=("bold", 15))
max_temp.place(x=128, y=540)
  
  
mini = customtkinter.CTkLabel(master=frame_1, text="Min. Temp.: ", width=0, 
              font=("bold", 15))
mini.place(x=3, y=570)
  
min_temp = customtkinter.CTkLabel(master=frame_1, text="...", width=0, 
                  font=("bold", 15))
min_temp.place(x=128, y=570)
  
  
# Note
note = customtkinter.CTkLabel(master=frame_1, text="All temperatures in degree Fahrenheit",
              font=("italic", 10))
note.place(x=95, y=640)



app.mainloop()