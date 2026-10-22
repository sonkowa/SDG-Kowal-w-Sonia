import tkinter as tk
from pathlib import Path

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


    return(window, canvas)