import pyautogui
import tkinter as tk
from tkinter import ttk
import ScreenShot

intro_text = """This is HandTex, an image-to-LaTeX source code application!\n
Take a screenshot or upload a file, and HandTex will convert it 
into LaTeX source code. Currently, HandTex works best with digital 
versions of documents, where the text is clear and well-defined. 
While it may not perform as accurately on handwritten or low-quality 
images, it's a powerful tool for converting neatly formatted 
documents into LaTeX with ease!
"""

def callback(img):
    img.save("a.png")
    message_label.config(text="Processing screenshot")

def cancel_callback():
    message_label.config(text="Quit Screenshot")

def take_screenshot():
    ScreenShot.screen_shot(root, callback, cancel_callback)

width, height = pyautogui.size()

window_dim = (width // 3, height // 4)

root = tk.Tk()
root.title("HandTex")
root.geometry(f"{window_dim[0]}x{window_dim[1]}")

style = ttk.Style()
style.configure("TButton", foreground="black")

ttk.Label(root, text=intro_text).grid(rowspan=1)
message_label = ttk.Label(root, text="Welcome!")
message_label.grid(column=0, row=1)
test = ttk.Button(root, text="Take ScreenShot", style="TButton", command=take_screenshot)
test.grid(column=0, row=2)
quit = ttk.Button(root, text="Quit", style="TButton", command=root.destroy)
quit.grid(column=0, row=3)

root.focus_force()
root.mainloop()
