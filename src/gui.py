import tkinter as tk
from tkinter import messagebox
from src.scraper import capturar_temperatura
from src.excel import salvar_temperatura

def iniciar_gui():
    root = tk.Tk()
    root.title("Captador de Temperatura - São Paulo")

    def executar():
        temp = capturar_temperatura()
        salvar_temperatura(temp)
        messagebox.showinfo("Temperatura capturada", f"Temperatura atual: {temp}")

    btn = tk.Button(root, text="Buscar Previsão", command=executar, width=20, height=2)
    btn.pack(pady=30)

    root.mainloop()