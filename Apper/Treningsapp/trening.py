import random
import tkinter as tk
from tkinter import messagebox

class main:
    def __init__(self, root):
        self.root = root
        self.root.title ("Holy Lifts")
        self.root.geometry("700x1000")

        self.add_button = tk.Button(root, text="Styrkekalkulator", command=self.Styrkekalkulator)
        self.add_button.pack(pady=5)

    def Styrkekalkulator(self):
        styrke_kalkulator_vindu = tk.Toplevel(self.root)
        styrke_kalkulator_vindu.title("Styrkekalkulator")
        styrke_kalkulator_vindu.geometry("700x1000")
            
        label = tk.Label(styrke_kalkulator_vindu, text="Skriv inn vekt (kg):")
        label.pack(pady=10)
        vekt_entry = tk.Entry(styrke_kalkulator_vindu, width=20)
        vekt_entry.pack(pady=5)

        label = tk.Label(styrke_kalkulator_vindu, text="Skriv inn hvor mange reps:")
        label.pack(pady=10)
        reps_entry = tk.Entry(styrke_kalkulator_vindu, width=20)
        reps_entry.pack(pady=5)

        self.add_button = tk.Button(root, text="Kalkuler styrke", command=self.kalkulerStyrke)

        def kalkulerStyrke():
            try:
                vekt = float(vekt_entry.get())
                reps = float(reps_entry.get())
                styrkeøkning = vekt * (1 + (reps * 0.03333333333333333))
                



root = tk.Tk()
app = main(root)
root.mainloop()