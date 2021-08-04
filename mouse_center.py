import pyautogui
import requests
from tkinter import *
from pyscreeze import center
import ctypes


# CENTER MOUSE IN MAIN WINDOW
def mouse_finder():
    x = int(pyautogui.size().width / 2)
    y = int(pyautogui.size().height / 2)
    pyautogui.moveTo(x, y)


def Close():
    window.destroy()


# CLOSE THE TERMINAL WINDOWS
kernel32 = ctypes.WinDLL("kernel32")
user32 = ctypes.WinDLL("user32")
SW_HIDE = 0
hWnd = kernel32.GetConsoleWindow()
user32.ShowWindow(hWnd, SW_HIDE)

# CREATE AN INTERACTION WINDOW


def create_window():
    global window
    window = Tk()
    window.eval("tk::PlaceWindow . center")
    window.title("MOUSE FINDER")
    window.geometry("300x100")  # Window size (width x height)
    texto_orientacao = Label(window, text="MOUSE SUCCESSFULLY RECOVERED!")
    texto_orientacao.grid(column=0, row=0, padx=50, pady=20)
    mouse_finder()
    botao = Button(window, text="CLOSE", command=Close)
    botao.grid(column=0, row=1, padx=110, pady=10)
    window.mainloop()


create_window()
