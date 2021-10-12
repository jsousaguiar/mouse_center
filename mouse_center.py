import pyautogui

# import tkinter as tk
# import ctypes


# CENTER MOUSE IN MAIN WINDOW
def mouse_finder():
    x = int(pyautogui.size().width / 2)
    y = int(pyautogui.size().height / 2)
    pyautogui.moveTo(x, y)


widht = int(pyautogui.size().width / 2 / 2.5)
height = int(pyautogui.size().height / 2 / 4)
size = f"{widht} x {height}"

mouse_finder()

# def Close():
#     tk.window.destroy()
#     tk.mainloop()


# CLOSE THE TERMINAL WINDOWS
# kernel32 = ctypes.WinDLL("kernel32")
# user32 = ctypes.WinDLL("user32")
# SW_HIDE = 0
# hWnd = kernel32.GetConsoleWindow()
# user32.ShowWindow(hWnd, SW_HIDE)

# CREATE AN INTERACTION WINDOW


# def create_window():
#     global window
#     size = "384x135"
#     window = tk.Tk()
#     window.eval("tk::PlaceWindow . center")
#     window.title("MOUSE FINDER")
#     window.geometry(size)  # Window size (width x height)
#     texto_orientacao = tk.Label(window, text="MOUSE SUCCESSFULLY RECOVERED!")
#     texto_orientacao.grid(column=0, row=0, padx=50, pady=20)
#     mouse_finder()
#     botao = tk.Button(window, text="CLOSE", command=Close)
#     botao.grid(column=0, row=1, padx=110, pady=10)
#     window.mainloop()


# create_window()
# print(size)
