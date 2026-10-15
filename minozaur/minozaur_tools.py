import tkinter as tk
from PIL import Image, ImageTk

# Definicje metod:
color_level = 0.0 #dla hover 0 - biały, 1 - niebieski
after_id = None
ALPHA = 140          
panel_images = []

def close_program():
    global after_id
    if after_id is not None:
        canvas.after_cancel(after_id)
        after_id = None
    canvas.tag_unbind("button", "<Enter>")
    canvas.tag_unbind("button", "<Leave>")
    window.quit()           



def hex_to_rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))

def mix_colors(c1, c2, t):
    a, b = hex_to_rgb(c1), hex_to_rgb(c2)
    return "#%02x%02x%02x" % tuple(round(x + (y - x) * t) for x, y in zip(a, b))


# półprzezroczyste okienko pod tekstem definicja 
def add_panel(text_id, pad=10):
    x1, y1, x2, y2 = canvas.bbox(text_id)     
    x1, y1, x2, y2 = x1 - pad, y1 - pad, x2 + pad, y2 + pad

    width = int(x2 - x1)
    height = int(y2 - y1)

    pic = Image.new("RGBA", (width, height), (0, 0, 0, ALPHA))
    photo = ImageTk.PhotoImage(pic)
    panel_images.append(photo)

    panel_id = canvas.create_image(x1, y1, image=photo, anchor="nw")
    canvas.tag_lower(panel_id, text_id)       
    return panel_id


def fade(target):
    global color_level, after_id
    if after_id is not None:
        canvas.after_cancel(after_id)
        after_id = None

    if color_level < target:
        color_level += 0.1
    elif color_level > target:
        color_level -= 0.1
    color_level = max(0.0, min(1.0, color_level))

    canvas.itemconfig("zamknij", fill=mix_colors("#FFFFFF", "#90E0EF", color_level))

    if abs(color_level - target) > 0.05:
        after_id = canvas.after(20, lambda: fade(target))

# Utworzenie głównego okna + canvas:

window = tk.Tk()
window.title("Minozaur Tools")
window.resizable(False, False)

canvas = tk.Canvas(
    window,
    width=850,
    height=850,
    highlightthickness=0
)

canvas.pack()


# Grafika tła:

background_screen = tk.PhotoImage(file="minozaur.png")

canvas.create_image(
    0,
    -100,
    image=background_screen,
    anchor="nw"
)


# Tytuł programu:
canvas.create_text(
    400,
    50,
    text="Minozaur Tools",
    font=("Arial", 30, "bold"),
    fill="white"
)


# Menu:

menu_text = canvas.create_text(
    180,
    420,
    text="Wybierz operację:",
    font=("Arial", 16, "bold"),
    fill="white"
)
add_panel(menu_text)

# Przycisk zamknięcia:

close_text = canvas.create_text(
    180,
    465,
    text="Zamknij program",
    font=("Arial", 11, "bold"),
    fill="white",
    tags="zamknij"
)
close_panel = add_panel(close_text)

canvas.itemconfig(close_panel, tags = "zamknij_panel")

canvas.addtag_withtag("button", close_text)
canvas.addtag_withtag("button", close_panel)

canvas.tag_bind("button", "<Button-1>", lambda event: close_program())
canvas.tag_bind("button", "<Enter>", lambda event: fade(1.0))
canvas.tag_bind("button", "<Leave>", lambda event: fade(0.0))


# Główna pętla programu:

window.protocol("WM_DELETE_WINDOW", close_program)

window.mainloop()
window.destroy() 