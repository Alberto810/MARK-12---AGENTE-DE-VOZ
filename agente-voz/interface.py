import tkinter as tk
from threading import Thread
from main import ouvir_microfone


class Interface:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Assistente Jarvis")
        self.root.geometry("400x300")

        self.label = tk.Label(self.root, text="🤖 Assistente parado", font=("Arial", 14))
        self.label.pack(pady=20)

        self.botao = tk.Button(self.root, text="Iniciar", command=self.iniciar)
        self.botao.pack(pady=10)

    def loop_voz(self):
        self.label.config(text="🎤 Ouvindo...")
        while True:
            if ouvir_microfone():
                break

    def iniciar(self):
        Thread(target=self.loop_voz, daemon=True).start()

    def executar(self):
        self.root.mainloop()