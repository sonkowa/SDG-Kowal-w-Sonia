from src.create_window import create_window
from src.create_menu_option import create_menu_option
from src.close_window import close_window
from src.menu_operations.close_program import close_program
from src.data_service import get_layer

def update_menu():
    canvas.delete("layer_status")

    if get_layer() is not None:
        canvas.create_text(
            180,
            380,
            text = "PLIK ZAŁADOWANY PRAWIDŁOWO"
            fill = "light green"
            tags = "layer_status"
        )


window, canvas = create_window()


create_menu_option(canvas, lambda: close_program(window, canvas))

window.protocol("WM_DELETE_WINDOW", lambda: close_program(window, canvas))

window.mainloop()
window.destroy()