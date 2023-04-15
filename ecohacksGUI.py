import customtkinter
import socket
customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk()
app.geometry("400x400")
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
    
def b(value):
     costs_label.configure(text="Temperature "+str(slider_1.get()))




frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)

label_1 = customtkinter.CTkLabel(master=frame_1, text="Smart Thermostat" ,justify=customtkinter.LEFT)
label_1.pack(pady=10, padx=10)



costs_label = customtkinter.CTkLabel(master=frame_1,text="Temperature: 75.0")
costs_label.pack()

slider_1 = customtkinter.CTkSlider(master=frame_1, from_=60, to=90,command=b, hover=True, number_of_steps=30)
slider_1.pack(pady=10, padx=10)
slider_1.set(75)




button_1 = customtkinter.CTkButton(master=frame_1, text="Set Temperature",command=button_callback)
button_1.pack(pady=10, padx=10)



app.mainloop()


