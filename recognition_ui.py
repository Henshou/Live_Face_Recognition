import customtkinter as ctk
import subprocess

def run_recognition() :
    ui.destroy()
    subprocess.call(["python","Face_Recognition.py"])


ui = ctk.CTk()
screen_w=ui.winfo_screenwidth()
screen_h=ui.winfo_screenheight()
ui.geometry(f"{screen_w}x{screen_h}+{0}+{0}")
ctk.set_default_color_theme("dark-blue")
ui.title("Face Recognition")

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
                                 height=50,
                                 border_width=0,
                                 corner_radius=8,
                                 text="Unlock With Face Recognition",
                                 command=run_recognition)
button.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

ui.mainloop()