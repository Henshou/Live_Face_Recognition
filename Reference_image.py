import cv2
import time
import customtkinter as ctk
import subprocess

def capture(event=None):
    name = entry_name.get()
    ui.destroy()
    if name:
        cam = cv2.VideoCapture(0)
        desired_frame = 5
        currentframe = 0
        img_counter = 1
        frame_delay = 0.5

        while currentframe < desired_frame:
            ret, frame = cam.read()

            if ret:
                img_name = "C:/Users/Gerrard/Documents/Live_Face_Recognition/Images/{}_{}.jpg".format(name, img_counter)
                cv2.imwrite(img_name, frame)
                currentframe += 1
                img_counter += 1
                time.sleep(frame_delay)

        cam.release()

        try:
            subprocess.call(["python", "recognition_ui.py"])
        except Exception as e:
            print("An error occurred while executing 'recognition_ui.py':", str(e))

ui = ctk.CTk()
screen_w=ui.winfo_screenwidth()
screen_h=ui.winfo_screenheight()
ui.geometry(f"{screen_w}x{screen_h}+{0}+{0}")
ctk.set_default_color_theme("dark-blue")
ui.title("Capture Image")

label_name = ctk.CTkLabel(master=ui, text="Enter your name:")
label_name.place(relx=0.5, rely=0.4, anchor=ctk.CENTER)

entry_name = ctk.CTkEntry(master=ui)
entry_name.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)
entry_name.bind("<Return>", capture)

ui.mainloop()