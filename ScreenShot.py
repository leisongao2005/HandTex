import pyautogui
import tkinter as tk

class ScreenShot:  
    def __init__(self, root: tk.Tk, master: tk.Toplevel | tk.Tk, callback = None, cancel_callback = None):
        self.root = root
        self.master = master
        self.callback = callback
        self.cancel_callback = cancel_callback
        self.start_x = None
        self.start_y = None
        
        # selector display variables
        self.rect = None
        self.canvas = tk.Canvas(master, cursor="cross", background="black")
        self.canvas.pack(fill=tk.BOTH, expand=True)  
        self.canvas.config(bg=master["bg"])
        self.canvas.bind("<Button-1>", self.on_button_press)
        self.canvas.bind("<B1-Motion>", self.on_mouse_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_button_release)

    def on_button_press(self, event):
        self.start_x = event.x
        self.start_y = event.y
        self.rect = self.canvas.create_rectangle(self.start_x, self.start_y, self.start_x, self.start_y, outline='white', width=1)  
        self.root.bind("<Escape>", self.check_escape)

    def check_escape(self, event):
        if event.keysym == "Escape":
            self.root.unbind("<Escape>")
            self.canvas.delete(self.rect)
            self.root.after(1, self.cancel_callback())
            self.master.destroy()
        
    def on_mouse_drag(self, event):  
        self.canvas.coords(self.rect, self.start_x, self.start_y, event.x, event.y)

    def on_button_release(self, event):
        left = min(self.start_x, event.x)
        right = min(self.start_y, event.y)
        width = abs(self.start_x - event.x)
        height = abs(self.start_y - event.y)

        if width * height != 0:
            self.master.withdraw()
            self.master.deiconify()
            self.master.focus_force()
            img = pyautogui.screenshot(region=(left, right, width, height))
            self.root.after(1, self.callback(img))
        else:
            self.root.after(1, self.cancel_callback())
        
        self.canvas.delete(self.rect)
        self.master.destroy()
        

def screen_shot(root:tk.Tk, callback = None, cancel_callback = None):
    top = tk.Toplevel(root)
    top.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}+0+0")
    top.overrideredirect(True)
    top.lift()
    top.attributes("-topmost", True)
    top.attributes("-transparent", True)
    top.config(bg="systemTransparent")

    ScreenShot(root, top, callback, cancel_callback)