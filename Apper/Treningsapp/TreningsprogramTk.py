import random
import tkinter as tk
from tkinter import messagebox

# Øvelseslister
Chest = ["Dumbbell press", "Incline dumbbell press", "Chest flyes", "Cable chest flyes"]
Triceps = ["Triceps pushdown", "Skullcrushers", "Overhead triceps extensions", "Diamond push-up", "Bench dip", "Triceps kickback", "Single-arm triceps pushdown"]
Skuldre = ["Lateral raise", "Front raise", "Reverse flyes", "Cable lateral raise", "Seated lateral raise", "Upright row"]
Push = ["Barbell bench press", "Dips", "Military press"]

Biceps = ["Dumbbell biceps curl", "Hammer curl", "Standing cable curl", "Preacher curl", "Concentration curl", "Spider curl", "Incline dumbbell curl"]
Forearm = ["Wrist curl", "Reverse wrist curl", "Reverse curl", "Cable wrist curl", "Wrist roller"]
Back = ["Barbell row", "Dumbbell row", "Lat pulldown", "Kettlebell/dumbbell back extensions"]
Arms = ["Chin-ups"]
Pull = ["Pull-ups", "Deadlift"]

Hamstring = ["Leg curl", "Reverse hyperextensions", "Hamstring kickbacks"]
Quads = ["Leg extensions", "Bulgarian split squats", "Step-ups", "Pistol squats", "Leg press"]
Calves = ["Standing calf raise", "Seated calf raise", "Calf raise på leg press"]
Legs = ["Barbell squat", "Romanian deadlift", "Lunges (Med vekt)"]

Core = ["Crunches", "Russian twists", "Leg raises", "Hanging leg raises", "Planke", "Sykling", "Jogging"]

# Funksjon for å velge et bestemt antall tilfeldige øvelser
def velg_ovelser(ovelsesliste, antall):
    return [random.choice(ovelsesliste) for _ in range(antall)]

# Funksjon for å beregne styrkeøkning
def beregn_styrke(vekt, reps):
    styrkeøkning = vekt * (1 + (reps * 0.03333333333333333))
    return styrkeøkning

# Tkinter GUI-applikasjon
class TreningsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Styrke Kalkulator og Treningsprogram")
        self.root.geometry("600x500")

        # Label og input for valg av handling (program eller beregn styrke)
        self.label_1 = tk.Label(root, text="Velg handling:")
        self.label_1.pack(pady=10)

        self.valg_var = tk.StringVar()
        self.valg_var.set("Velg en handling")

        self.program_button = tk.Radiobutton(root, text="Lag Treningsprogram", variable=self.valg_var, value="lag program", command=self.show_program_form)
        self.program_button.pack(pady=5)

        self.styrke_button = tk.Radiobutton(root, text="Beregn Styrke", variable=self.valg_var, value="beregn", command=self.show_styrke_form)
        self.styrke_button.pack(pady=5)

        # Resultat label
        self.result_label = tk.Label(root, text="Resultatet vises her.", font=("Arial", 12))
        self.result_label.pack(pady=20)

        self.input_frame = None  # Vi skal oppdatere denne med input feltene avhengig av hva som er valgt

    def show_program_form(self):
        if self.input_frame:
            self.input_frame.destroy()

        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack(pady=20)

        # Input for muskelgruppe
        self.muskelvalg_label = tk.Label(self.input_frame, text="Velg muskelgruppe (Push/Pull/Legs/Arms/Core/FullBody):")
        self.muskelvalg_label.grid(row=0, column=0, pady=5)

        self.muskelvalg_entry = tk.Entry(self.input_frame)
        self.muskelvalg_entry.grid(row=0, column=1, pady=5)

        # Input for treningsmål
        self.mal_label = tk.Label(self.input_frame, text="Velg mål (Styrke/Volum/Utholdenhet):")
        self.mal_label.grid(row=1, column=0, pady=5)

        self.mal_entry = tk.Entry(self.input_frame)
        self.mal_entry.grid(row=1, column=1, pady=5)

        self.generate_button = tk.Button(self.input_frame, text="Generer Treningsprogram", command=self.generer_treningsprogram)
        self.generate_button.grid(row=2, column=0, columnspan=2, pady=10)

    def generer_treningsprogram(self):
        muskelvalg = self.muskelvalg_entry.get().lower()
        mal = self.mal_entry.get().lower()

        if muskelvalg == "push":
            ovelser = velg_ovelser(Chest, 2) + velg_ovelser(Triceps, 2) + velg_ovelser(Skuldre, 2) + velg_ovelser(Push, 1)
        elif muskelvalg == "pull":
            ovelser = velg_ovelser(Back, 2) + velg_ovelser(Biceps, 2) + velg_ovelser(Pull, 1)
        elif muskelvalg in ["legs", "bein"]:
            ovelser = velg_ovelser(Quads, 2) + velg_ovelser(Hamstring, 2) + velg_ovelser(Calves, 2)
        elif muskelvalg in ["armer", "arms"]:
            ovelser = velg_ovelser(Biceps, 2) + velg_ovelser(Triceps, 2) + velg_ovelser(Forearm, 1) + velg_ovelser(Arms, 1)
        elif muskelvalg == "core":
            ovelser = velg_ovelser(Core, 4)
        elif muskelvalg == "fullbody":
            ovelser = velg_ovelser(Chest, 1) + velg_ovelser(Back, 1) + velg_ovelser(Skuldre, 1) + velg_ovelser(Biceps, 1) + velg_ovelser(Triceps, 1) + velg_ovelser(Quads, 1) + velg_ovelser(Hamstring, 1) + velg_ovelser(Core, 2)
        else:
            self.result_label.config(text="Ugyldig muskelgruppe.")
            return

        if mal == "styrke":
            reps, sett = "4-8 reps", "3-4 sett"
        elif mal == "volum":
            reps, sett = "8-12 reps", "3-5 sett"
        elif mal == "utholdenhet":
            reps, sett = "15+ reps", "3-6 sett"
        else:
            self.result_label.config(text="Ugyldig mål.")
            return

        result = "\nDitt treningsprogram:\n"
        result += "\n".join([f"- {ovelse}" for ovelse in ovelser])
        result += f"\n\nSett og reps:\n{reps}, {sett}"
        self.result_label.config(text=result)

    def show_styrke_form(self):
        if self.input_frame:
            self.input_frame.destroy()

        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack(pady=20)

        # Input for vekt
        self.vekt_label = tk.Label(self.input_frame, text="Hvor mye vekt tok du?")
        self.vekt_label.grid(row=0, column=0, pady=5)

        self.vekt_entry = tk.Entry(self.input_frame)
        self.vekt_entry.grid(row=0, column=1, pady=5)

        # Input for reps
        self.reps_label = tk.Label(self.input_frame, text="Hvor mange reps tok du?")
        self.reps_label.grid(row=1, column=0, pady=5)

        self.reps_entry = tk.Entry(self.input_frame)
        self.reps_entry.grid(row=1, column=1, pady=5)

        self.calculate_button = tk.Button(self.input_frame, text="Beregn Styrke", command=self.beregn_styrke)
        self.calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

    def beregn_styrke(self):
        try:
            vekt = float(self.vekt_entry.get())
            reps = float(self.reps_entry.get())
            resultat = beregn_styrke(vekt, reps)
            self.result_label.config(text=f"Styrken etter {reps} reps med {vekt} kg er: {resultat:.2f} kg")
        except ValueError:
            self.result_label.config(text="Vennligst skriv inn gyldige tall for vekt og reps.")

# Tkinter hovedvindu
root = tk.Tk()
app = TreningsApp(root)
root.mainloop()
