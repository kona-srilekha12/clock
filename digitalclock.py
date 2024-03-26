import tkinter as tk
import time
root=tk.Tk()
root.title("digital clock")
#root.geometry("800x400")
def present_time():
    display_time=time.strftime("%I:%M:%S %p")
    digi.config(text=display_time)
    digi.after(200,present_time)
digi=tk.Label(root,font=("arial",150),bg="red",fg="white")
digi.pack()
present_time()
root.mainloop()