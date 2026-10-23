from PIL import Image, ImageTk


color_level = 0.0   # dla hover: 0 - biały, 1 - niebieski
after_id = None
ALPHA = 140          
panel_images = []


def hex_to_rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))

def mix_colors(c1, c2, t):
    a, b = hex_to_rgb(c1), hex_to_rgb(c2)
    return "#%02x%02x%02x" % tuple(round(x + (y - x) * t) for x, y in zip(a, b))


def add_panel(canvas, text_id, pad=10):
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


def fade(canvas, target):
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
        after_id = canvas.after(20, lambda: fade(canvas, target))

def stop_animation(canvas):
    global after_id
    if after_id is not None:
        canvas.after_cancel(after_id)
        after_id = None

def create_menu_option(canvas: tk.Canvas,
                        height: int,
                        text: str,
                        *operations: Callable,
                        on_close):
    menu_text = canvas.create_text(
        180,
        420,
        text="Wybierz operację:",
        font=("Arial", 16, "bold"),
        fill="white"
    )
    add_panel(canvas, menu_text)

    #Przycisk zamknięcia
    close_text = canvas.create_text(
        180,
        465,
        text="Zamknij program",
        font=("Arial", 11, "bold"),
        fill="white",
        tags="zamknij"
    )

    close_panel = add_panel(canvas, close_text)
    canvas.itemconfig(close_panel, tags = "zamknij_panel")

    canvas.addtag_withtag("button", close_text)
    canvas.addtag_withtag("button", close_panel)

    canvas.tag_bind("button", "<Button-1>", lambda event: on_close())
    canvas.tag_bind("button", "<Enter>", lambda event: fade(canvas, 1.0))
    canvas.tag_bind("button", "<Leave>", lambda event: fade(canvas, 0.0))
