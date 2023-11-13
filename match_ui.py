import customtkinter as ctk 
from PIL import Image
import subprocess

def return_home() :
    ui.destroy()
    subprocess.call(["python","Face_Recognition_App.py"])

ui = ctk.CTk()
screen_w=ui.winfo_screenwidth()
screen_h=ui.winfo_screenheight()

ui.geometry(f"{screen_w}x{screen_h}+{0}+{0}")
ctk.set_default_color_theme("dark-blue")
ui.title("Match")

text = ctk.StringVar(value="MATCH!")
img = ctk.CTkImage(dark_image=Image.open("checklist.png"),size=(200,200))

lab=ctk.CTkLabel(master=ui,
                               image=img,
                               text="",
                               width=100,
                               height=100,
                               corner_radius=8)
lab.place(relx=0.5, rely=0.3, anchor=ctk.CENTER)

label = ctk.CTkLabel(master=ui,
                               textvariable=text,
                               width=100,
                               height=50,
                               fg_color=("white", "gray75"),
                               text_color=("green"),
                               corner_radius=8)
label.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

button = ctk.CTkButton(master=ui,
                                 width=120,
                                 height=32,
                                 border_width=0,
                                 corner_radius=8,
                                 text="Return Home",
                                 command=return_home)
button.place(relx=0.5, rely=0.7, anchor=ctk.CENTER)


ui.mainloop()