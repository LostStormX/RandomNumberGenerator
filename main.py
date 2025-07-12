import random
import tkinter as tk
from tkinter import StringVar

# Creating the window
window = tk.Tk()

# Setting the windows title
window.title("Random Number Generator - 1.0.0")

# Scaling the window
window_width = 800
window_height = 400

# Centering Window
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

center_x = screen_width - screen_height
center_y = screen_height - window_width

window.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

# Setting Params
window.configure(background="#1e1e1e")
window.resizable(width=False, height=False)

# Creating the text labels
RANlabel = tk.Label(window, text="0", font=("Arial Bold", 60), foreground="white")
RANlabel.place(relx=0.5, rely=0.4, anchor="center")
RANlabel.configure(background="#1e1e1e")

MINlabel = tk.Label(window, text="Min", font=("Arial Bold", 12), foreground="white")
MINlabel.place(relx=0.45, rely=0.54, anchor="center")
MINlabel.configure(background="#1e1e1e")

MAXlabel = tk.Label(window, text="Max", font=("Arial Bold", 12), foreground="white")
MAXlabel.place(relx=0.55, rely=0.54, anchor="center")
MAXlabel.configure(background="#1e1e1e")

creditsLabel = tk.Label(window, text="Made by Storm", font=("Arial Bold", 10), foreground="grey", bg="#1e1e1e")
creditsLabel.place(relx=0.5, rely=0.9, anchor="center")

# Creating the textboxes
def modifiedText():
    print("Update")

minInput = StringVar()
maxInput = StringVar()

minInput.trace("w", lambda name, index, mode, sv=minInput: modifiedText())
maxInput.trace("w", lambda name, index, mode, sv=maxInput: modifiedText())


MAXtext_box = tk.Entry(window, width=5, font=("Arial Bold", 15), textvariable=maxInput, justify="center", bg="white", relief="flat", fg="Black")
MAXtext_box.place(relx=0.55, rely=0.6, anchor="center")
MAXtext_box.insert(tk.END, "0")

MINtext_box = (tk.Entry(window, width=5, font=("Arial Bold", 15), textvariable=minInput, justify="center"))
MINtext_box.place(relx=0.45, rely=0.6, anchor="center")
MINtext_box.insert(tk.END, "0")

def modifiedText():
    print("Update")


# Creating the button
def button_Clicked():
    result = random.randint(int(minInput.get()), int(maxInput.get()))
    RANlabel.config(text=result)

button = tk.Button(
    window,
    text="Randomize",
    font=("Arial Bold", 10),
    bg="green",
    fg="white",
    relief="flat",
    command=button_Clicked
)
button.place(relx=0.5, rely=0.7, anchor="center")

window.mainloop()

