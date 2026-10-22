import tkinter as tk


ALPHA = 140          
panel_images = []


def hex_to_rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))

def mix_colors(c1, c2, t):
    a, b = hex_to_rgb(c1), hex_to_rgb(c2)
    return "#%02x%02x%02x" % tuple(round(x + (y - x) * t) for x, y in zip(a, b))





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



def create_menu_option():
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
