import pyautogui
import tkinter as tk

# Center mouse in main window
def mouse_finder():
    x = int(pyautogui.size().width / 2) #+ 24
    y = int(pyautogui.size().height / 2) #+ 24
    pyautogui.moveTo(x, y)

window = tk.Tk()
window.title("Mouse Finder")
frame = tk.LabelFrame(window, text="")
texto_orientacao = tk.Label(frame, text="Mouse successfully recovered!")
botao = tk.Button(frame, text="Close", command=window.destroy)
texto_vazio = tk.Label(frame)

frame.pack(padx=10, pady=10)
texto_orientacao.pack(padx=10,pady=(30, 0))
botao.pack(padx=20,pady=(10, 0))
texto_vazio.pack(padx=0,pady=(10, 10))
mouse_finder()

window.eval('tk::PlaceWindow . center')
window.mainloop()

