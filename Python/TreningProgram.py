import random
from typing import Dict, List, Union

class WorkoutGenerator:
    def __init__(self):
        # Initialize exercise dictionaries with descriptions
        self.exercises = {
            'chest': {
                "Dumbbell press": "Ligg på en benk og press manualene oppover fra brystet.",
                "Incline dumbbell press": "Utfør en dumbbell press på en skråbenk.",
                "Chest flyes": "Ligg på en benk og før manualene i en bred bevegelse.",
                "Cable chest flyes": "Stå i et kabelapparat og trekk kabelene sammen."
            },
            'triceps': {
                "Triceps pushdown": "Bruk et kabelapparat for å skyve stangen nedover.",
                "Skullcrushers": "Ligg på en benk med en vektstang eller manualer.",
                "Overhead extensions": "Hold en manual med begge hender over hodet.",
                "Diamond push-up": "Push-up med hendene i diamantform.",
                "Bench dip": "Senk kroppen ned fra en benk.",
                "Triceps kickback": "Strekk armen bak deg med manual.",
                "Single-arm pushdown": "Triceps pushdown med én arm."
            },
            'shoulders': {
                "Lateral raise": "Hev manualene ut til siden til skulderhøyde.",
                "Front raise": "Hev manualene fremover til skulderhøyde.",
                "Reverse flyes": "Løft manualene ut til sidene for bakre del.",
                "Cable lateral raise": "Bruk kabel for lateral raises.",
                "Seated lateral raise": "Sitt på benk og hev manualene ut.",
                "Upright row": "Trekk stang eller manualer opp mot brystet."
            },
            'back': {
                "Barbell row": "Bøy deg fremover og trekk en vektstang mot magen.",
                "Dumbbell row": "Ettarms roing med manual.",
                "Lat pulldown": "Trekk stang ned mot brystet.",
                "Back extensions": "Løft overkroppen på benk."
            },
            'biceps': {
                "Dumbbell curl": "Curl manualene mot skuldrene.",
                "Hammer curl": "Curl med håndflatene mot hverandre.",
                "Cable curl": "Curl med kabelapparat.",
                "Preacher curl": "Curl på preacher-benk.",
                "Concentration curl": "Isolert curl med én arm.",
                "Spider curl": "Curl liggende på skråbenk.",
                "Incline curl": "Curl på skråbenk."
            },
            'legs': {
                "Barbell squat": "Knebøy med stang.",
                "Romanian deadlift": "Strak markløft.",
                "Bulgarian split squats": "Utfall med bakre fot på benk.",
                "Leg press": "Press i leg press maskin.",
                "Leg extensions": "Isolert quadriceps øvelse.",
                "Leg curls": "Isolert hamstring øvelse.",
                "Calf raises": "Stående tåhev."
            },
            'core': {
                "Crunches": "Klassisk mageøvelse.",
                "Russian twists": "Rotasjon av overkroppen.",
                "Leg raises": "Løft av strake bein.",
                "Hanging leg raises": "Hengende beinløft.",
                "Planke": "Statisk kjerneøvelse.",
                "Ab wheel": "Rulle ut og inn med ab-wheel."
            }
        }
        
        # Define workout splits
        self.splits = {
            'push': ['chest', 'triceps', 'shoulders'],
            'pull': ['back', 'biceps'],
            'legs': ['legs'],
            'upper': ['chest', 'back', 'shoulders', 'triceps', 'biceps'],
            'full': ['chest', 'back', 'shoulders', 'triceps', 'biceps', 'legs', 'core']
        }
        
        # Define training goals
        self.goals = {
            'styrke': {'reps': '4-6', 'sets': '4-5', 'rest': '2-3 min'},
            'volum': {'reps': '8-12', 'sets': '3-4', 'rest': '1-2 min'},
            'utholdenhet': {'reps': '15-20', 'sets': '3', 'rest': '30-60 sek'}
        }

    def get_exercises(self, split: str, num_exercises: int = 3) -> Dict[str, List[str]]:
        """Generate exercises for given split"""
        workout = {}
        
        if split not in self.splits:
            return {}
            
        for muscle in self.splits[split]:
            exercises = list(self.exercises[muscle].keys())
            count = min(num_exercises, len(exercises))
            workout[muscle] = random.sample(exercises, count)
            
        return workout

    def calculate_1rm(self, weight: float, reps: int) -> float:
        """Calculate theoretical 1 rep max using Brzycki formula"""
        if reps < 1 or weight < 0:
            return 0
        return round(weight * (36 / (37 - reps)), 1)

    def generate_program(self) -> None:
        """Generate complete workout program based on user input"""
        print("\n=== Treningsprogram Generator ===")
        print("1. Lag treningsprogram")
        print("2. Beregn 1RM (one rep max)")
        
        choice = input("\nVelg alternativ (1/2): ")
        
        if choice == '1':
            print("\nTilgjengelige splits:")
            for split in self.splits.keys():
                print(f"- {split}")
            
            split = input("\nVelg split: ").lower()
            if split not in self.splits:
                print("Ugyldig split!")
                return
                
            print("\nTreningsmål:")
            for goal in self.goals.keys():
                print(f"- {goal}")
                
            goal = input("\nVelg mål: ").lower()
            if goal not in self.goals:
                print("Ugyldig mål!")
                return
                
            workout = self.get_exercises(split)
            
            print("\n=== Ditt Treningsprogram ===")
            for muscle, exercises in workout.items():
                print(f"\n{muscle.upper()}:")
                for ex in exercises:
                    print(f"- {ex}")
                    print(f"  {self.exercises[muscle][ex]}")
                    
            goal_info = self.goals[goal]
            print(f"\nAnbefalt oppsett for {goal}:")
            print(f"Sett: {goal_info['sets']}")
            print(f"Reps: {goal_info['reps']}")
            print(f"Pause: {goal_info['rest']}")
            
        elif choice == '2':
            weight = float(input("\nVekt (kg): "))
            reps = int(input("Antall reps: "))
            rm = self.calculate_1rm(weight, reps)
            print(f"\nEstimert 1RM: {rm} kg")
        
        else:
            print("Ugyldig valg!")

if __name__ == "__main__":
    generator = WorkoutGenerator()
    generator.generate_program()