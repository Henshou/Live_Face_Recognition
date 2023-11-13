import customtkinter as ctk 
import subprocess

def run_reference() :
    ui.destroy()
    subprocess.call(["python","Reference_image.py"])

def run_recognition() :
    ui.destroy()
    subprocess.call(["python","Face_Recognition.py"])

def exit_ui():
    ui.destroy()

ui = ctk.CTk()
screen_w=ui.winfo_screenwidth()
screen_h=ui.winfo_screenheight()
ui.geometry(f"{screen_w}x{screen_h}+{0}+{0}")
ctk.set_default_color_theme("dark-blue")
ui.title("Home")


text = ctk.StringVar(value="Live Face Recognition")
label = ctk.CTkLabel(master=ui,
                               textvariable=text,
                               width=200,
                               height=100,
                               font=("Arial",48),
                               fg_color=("transparent"),
                               text_color=("white"),
                               corner_radius=8)
label.place(relx=0.5, rely=0.2, anchor=ctk.CENTER)

button = ctk.CTkButton(master=ui,
                                 width=200,
                                 height=100,
                                 text="Take Image",
                                 command=run_reference)
button.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

button1 = ctk.CTkButton(master=ui,
                                 width=200,
                                 height=100,
                                 text="Unlock With Face Recognition",
                                 command=run_recognition)
button1.place(relx=0.5, rely=0.7, anchor=ctk.CENTER)


button2= ctk.CTkButton(master=ui,
                                 width=100,
                                 height=50,
                                 text="Exit",
                                 command=exit_ui)
button2.place(relx=0.95, rely=0.95, anchor=ctk.SE)


ui.mainloop()