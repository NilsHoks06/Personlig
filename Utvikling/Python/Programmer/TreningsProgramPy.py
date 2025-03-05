import random

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

Bruker = input("Vil du beregne styrke eller lage program? ").lower()

if Bruker in ["lag program", "2", "program", "lage program", "lag", "lage"]:
    # Velger et bestemt antall tilfeldige øvelser
    def velg_ovelser(ovelsesliste, antall):
        return [random.choice(ovelsesliste) for _ in range(antall)]

    # Brukerinput for muskelgruppe
    muskelvalg = input("Hvilke muskelgruppe vil du trene? (Push/Pull/Legs/Armer/UpperBody/Core/FullBody): ").lower()

    # Velg øvelser basert på muskelgruppen
    if muskelvalg == "push":
        chest_ovelser = velg_ovelser(Chest, 2)
        triceps_ovelser = velg_ovelser(Triceps, 2)
        skuldre_ovelser = velg_ovelser(Skuldre, 2)
        push_ovelser = velg_ovelser(Push, 1)
        ovelser = chest_ovelser + triceps_ovelser + skuldre_ovelser + push_ovelser

    elif muskelvalg == "pull":
        back_ovelser = velg_ovelser(Back, 2)
        biceps_ovelser = velg_ovelser(Biceps, 2)
        pull_ovelser = velg_ovelser(Pull, 1)
        ovelser = back_ovelser + biceps_ovelser + pull_ovelser

    elif muskelvalg in ["legs", "bein"]:
        quads_ovelser = velg_ovelser(Quads, 2)
        hamstring_ovelser = velg_ovelser(Hamstring, 2)
        calves_ovelser = velg_ovelser(Calves, 2)
        ovelser = quads_ovelser + hamstring_ovelser + calves_ovelser

    elif muskelvalg in ["armer", "arms"]:
        biceps_ovelser = velg_ovelser(Biceps, 2)
        triceps_ovelser = velg_ovelser(Triceps, 2)
        forearm_ovelser = velg_ovelser(Forearm, 1)
        arms_ovelser = velg_ovelser(Arms, 1)
        ovelser = biceps_ovelser + triceps_ovelser + forearm_ovelser + arms_ovelser

    elif muskelvalg in ["upperbody", "upper body", "overkropp"]:
        chest_ovelser = velg_ovelser(Chest, 1)
        back_ovelser = velg_ovelser(Back, 1)
        skuldre_ovelser = velg_ovelser(Skuldre, 1)
        triceps_ovelser = velg_ovelser(Triceps, 1)
        biceps_ovelser = velg_ovelser(Biceps, 1)
        ovelser = chest_ovelser + back_ovelser + skuldre_ovelser + triceps_ovelser + biceps_ovelser

    elif muskelvalg in ["core", "kjerne"]:
        ovelser = velg_ovelser(Core, 4)

    elif muskelvalg in ["fullbody", "full body", "full kropp", "fullkropp"]:
        fullbody_ovelser = velg_ovelser(Chest, 1) + velg_ovelser(Back, 1) + velg_ovelser(Skuldre, 1) + velg_ovelser(Biceps, 1) + velg_ovelser(Triceps, 1) + velg_ovelser(Quads, 1) + velg_ovelser(Hamstring, 1)
        ovelser = fullbody_ovelser + velg_ovelser(Core, 2)

    else:
        print("Ugyldig muskelgruppe. Prøv igjen.")
        ovelser = []

    # Velg mål for treningen
    if ovelser:
        mal = input("Hva er målet ditt? (Styrke/Volum/Utholdenhet): ").lower()

        if mal == "styrke":
            reps, sett = "4-8 reps", "3-4 sett"
        elif mal == "volum":
            reps, sett = "8-12 reps", "3-5 sett"
        elif mal == "utholdenhet":
            reps, sett = "15+ reps", "3-6 sett"
        else:
            print("Ugyldig mål. Prøv igjen.")
            reps, sett = None, None

        # Print av treningsprogram
        if reps and sett:
            print("\nDitt treningsprogram:")
            for ovelse in ovelser:
                print(f"- {ovelse}")
            print(f"\nSett og reps:\n{reps}, {sett}")

elif Bruker in ["styrke", "beregn", "beregne", "beregne styrke", "beregn styrke"]:
    def beregn_styrke(vekt, reps):
        styrkeøkning = vekt * (1 + (reps * 0.03333333333333333))
        return styrkeøkning

    # Eksempel: 6 reps med 100 kg på benk
    vekt = int(input("Hvor mye vekt tok du? "))
    reps = int(input("Hvor mange reps tok du? "))
    resultat = beregn_styrke(vekt, reps)
    print(f"Styrken etter {reps} repetisjoner med {vekt} kg er: {resultat} kg")

#Laget av Nils Martin Hoksrud