import tkinter as tk
from src.create_menu_option import stop_animation

def close_window(window, canvas):
    stop_animation(canvas)
    canvas.tag_unbind("button", "<Enter>")
    canvas.tag_unbind("button", "<Leave>")
    window.quit()      