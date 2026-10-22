import tkinter as tk

def close_program():
    after_id = None
    global after_id
    if after_id is not None:
        canvas.after_cancel(after_id)
        after_id = None
    canvas.tag_unbind("button", "<Enter>")
    canvas.tag_unbind("button", "<Leave>")
    window.quit()      