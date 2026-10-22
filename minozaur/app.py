from src.create_window import create_window
from src.create_menu_option import create_menu_option
from src.close_window import close_window
from src.menu_operations.close_program import close_program

window, canvas = create_window()


create_menu_option(canvas, lambda: close_program(window, canvas))

window.protocol("WM_DELETE_WINDOW", lambda: close_program(window, canvas))

window.mainloop()
window.destroy()