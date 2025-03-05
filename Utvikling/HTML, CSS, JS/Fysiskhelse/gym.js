/* Øvelseslister */
const Chest = ["Dumbbell press", "Incline dumbbell press", "Chest flyes", "Cable chest flyes"];
const Triceps = ["Triceps pushdown", "Skullcrushers", "Overhead triceps extensions", "Diamond push-up", "Bench dip", "Triceps kickback", "Single-arm triceps pushdown"];
const Skuldre = ["Lateral raise", "Front raise", "Reverse flyes", "Cable lateral raise", "Seated lateral raise", "Upright row"];
const Push = ["Barbell bench press", "Dips", "Military press"];
const Biceps = ["Dumbbell biceps curl", "Hammer curl", "Standing cable curl", "Preacher curl", "Concentration curl", "Spider curl", "Incline dumbbell curl"];
const Forearm = ["Wrist curl", "Reverse wrist curl", "Reverse curl", "Cable wrist curl", "Wrist roller"];
const Back = ["Barbell row", "Dumbbell row", "Lat pulldown", "Kettlebell/dumbbell back extensions"];
const Arms = ["Chin-ups"];
const Pull = ["Pull-ups", "Deadlift"];
const Hamstring = ["Leg curl", "Reverse hyperextensions", "Hamstring kickbacks"];
const Quads = ["Leg extensions", "Bulgarian split squats", "Step-ups", "Pistol squats", "Leg press"];
const Calves = ["Standing calf raise", "Seated calf raise", "Calf raise på leg press"];
const Legs = ["Barbell squat", "Romanian deadlift", "Lunges (Med vekt)"];
const Core = ["Crunches", "Russian twists", "Leg raises", "Hanging leg raises", "Planke", "Sykling", "Jogging"];

/* Start treningsprogram */
function startProgram() {
    document.getElementById("programSection").style.display = "block";
    document.getElementById("styrkeSection").style.display = "none";
}

/* Start styrkeberegning */
function beregnStyrke() {
    document.getElementById("programSection").style.display = "none";
    document.getElementById("styrkeSection").style.display = "block";
}

/* Funksjon for å velge øvelser */
function velgOvelser(ovelsesliste, antall) {
    let ovelser = [];
    for (let i = 0; i < antall; i++) {
        let randomIndex = Math.floor(Math.random() * ovelsesliste.length);
        ovelser.push(ovelsesliste[randomIndex]);
    }
    return ovelser;
}

/* Lag treningsprogram basert på brukerens valg */
function lagProgram() {
    const muskelvalg = document.getElementById("muskelgruppe").value;
    const mal = document.getElementById("treningsmal").value;
    let ovelser = [];

    /* Velge øvelser basert på muskelgruppe */
    if (muskelvalg === "push") {
        ovelser = velgOvelser(Chest, 2).concat(velgOvelser(Triceps, 2), velgOvelser(Skuldre, 2), velgOvelser(Push, 1));
    } else if (muskelvalg === "pull") {
        ovelser = velgOvelser(Back, 2).concat(velgOvelser(Biceps, 2), velgOvelser(Pull, 1));
    } else if (muskelvalg === "legs") {
        ovelser = velgOvelser(Quads, 2).concat(velgOvelser(Hamstring, 2), velgOvelser(Calves, 2));
    } else if (muskelvalg === "arms") {
        ovelser = velgOvelser(Biceps, 2).concat(velgOvelser(Triceps, 2), velgOvelser(Forearm, 1), velgOvelser(Arms, 1));
    } else if (muskelvalg === "upperbody") {
        ovelser = velgOvelser(Chest, 1).concat(velgOvelser(Back, 1), velgOvelser(Skuldre, 1), velgOvelser(Triceps, 1), velgOvelser(Biceps, 1));
    } else if (muskelvalg === "core") {
        ovelser = velgOvelser(Core, 4);
    } else if (muskelvalg === "fullbody") {
        ovelser = velgOvelser(Chest, 1).concat(velgOvelser(Back, 1), velgOvelser(Skuldre, 1), velgOvelser(Biceps, 1), velgOvelser(Triceps, 1), velgOvelser(Quads, 1), velgOvelser(Hamstring, 1)).concat(velgOvelser(Core, 2));
    }

    let reps, sett;
    if (mal === "styrke") {
        reps = "4-8 reps";
        sett = "3-4 sett";
    } else if (mal === "volum") {
        reps = "8-12 reps";
        sett = "3-5 sett";
    } else if (mal === "utholdenhet") {
        reps = "15+ reps";
        sett = "3-6 sett";
    }

    /* Vis treningsprogram */
    const programResult = document.getElementById("programResult");
    programResult.innerHTML = "<ul>" + ovelser.map(ovelse => `<li>${ovelse}</li>`).join('') + "</ul>";
    programResult.innerHTML += `<p>Reps og sett: ${reps}, ${sett}</p>`;
}

/*Beregner styrke*/
function beregnStyrkeResultat() {
    const vekt = parseInt(document.getElementById("vekt").value);
    const reps = parseInt(document.getElementById("reps").value);
    const styrkeøkning = vekt * (1 + (reps * 0.03333333333333333));
    document.getElementById("styrkeResultat").innerHTML = `Styrken etter ${reps} repetisjoner med ${vekt} kg er: ${styrkeøkning.toFixed(2)} kg`;
}
