import tkinter as tk
from PIL import Image, ImageTk
from pathlib import Path


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


# Utworzenie głównego okna + canvas:
def create_window():
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
    img_path = Path(__file__).resolve().parent/"img"/"minozaur.png"
    window.background_screen = tk.PhotoImage(file= str(img_path))

    canvas.create_image(
        0,
        -100,
        image=window.background_screen,
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

    return(windows, canvas)