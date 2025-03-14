import tkinter as tk
from tkinter import messagebox

class Styrkekalkulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Holy Lifts")
        self.root.geometry("700x1000") 

        # Knapper som viser forskjellige deler av programmet
        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack(pady=10)

        # Knapp for styrkekalkulator
        self.add_button = tk.Button(root, text="Styrkekalkulator", command=self.open_kalkulator)
        self.add_button.pack(pady=5)

        # Knapp for treningsprogram
        self.treningsprogram_button = tk.Button(root, text="Treningsprogram", command=self.open_treningsprogram)
        self.treningsprogram_button.pack(pady=5)

    def open_kalkulator(self):
        kalkulator_vindu = tk.Toplevel(self.root)  # Åpner et nytt vindu
        kalkulator_vindu.title("Styrkekalkulator")
        kalkulator_vindu.geometry("400x400")

        label = tk.Label(kalkulator_vindu, text="Skriv inn vekt (kg):")
        label.pack(pady=10)

        weight_entry = tk.Entry(kalkulator_vindu, width=20)
        weight_entry.pack(pady=5)

        label2 = tk.Label(kalkulator_vindu, text="Skriv inn antall repetisjoner:")
        label2.pack(pady=10)

        reps_entry = tk.Entry(kalkulator_vindu, width=20)
        reps_entry.pack(pady=5)

        def calculate_strength():
            try:
                weight = float(weight_entry.get())
                reps = int(reps_entry.get())
                strength = weight * reps  # Dette kan endres for mer kompleks kalkulasjon
                messagebox.showinfo("Resultat", f"Din styrke score er: {strength}")
            except ValueError:
                messagebox.showerror("Feil", "Vennligst fyll ut gyldige verdier.")

        calculate_button = tk.Button(kalkulator_vindu, text="Beregn Styrke", command=calculate_strength)
        calculate_button.pack(pady=20)

    def open_treningsprogram(self):
        treningsprogram_vindu = tk.Toplevel(self.root)  # Åpner et nytt vindu
        treningsprogram_vindu.title("Treningsprogram")
        treningsprogram_vindu.geometry("400x400")

        label = tk.Label(treningsprogram_vindu, text="Velg treningsnivå:")
        label.pack(pady=10)

        nivåvalg = tk.StringVar(treningsprogram_vindu)

        nivåvalg.set("Nybegynner")  # Default valg

        nivå_menu = tk.OptionMenu(treningsprogram_vindu, nivåvalg, "Nybegynner", "Moderat", "Avansert")
        nivå_menu.pack(pady=10)

        def vis_program():
            nivå = nivåvalg.get()
            messagebox.showinfo("Treningsprogram", f"Treningsprogram for nivå: {nivå}")
        
        vis_program_button = tk.Button(treningsprogram_vindu, text="Vis Program", command=vis_program)
        vis_program_button.pack(pady=20)

# Oppretter hovedvinduet
if __name__ == "__main__":
    root = tk.Tk()
    app = Styrkekalkulator(root)
    root.mainloop()
