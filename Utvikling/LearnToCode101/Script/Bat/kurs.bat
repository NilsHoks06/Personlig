@echo off
::Lag en fil som heter VG2 med undermappene:
:: Brukerstøtte
:: Driftsstøtte
:: Norsk
:: Samfunssfag
:: Utvikling
:: Yrkesfagligfordypning

cd C:\Users\nil2612\OneDrive - Telemark fylkeskommune\

mkdir VG2

cd C:\Users\nil2612\OneDrive - Telemark fylkeskommune\VG2\ 

mkdir Brukerstotte 
mkdir Driftsstotte
mkdir Norsk 
mkdir Samfunnsfag 
mkdir Utvikling
mkdir Yrkesfagligfordypning

::Brukerstøtte
cd C:\Users\nil2612\OneDrive - Telemark fylkeskommune\VG2\Brukerstotte\
mkdir Oppgaver Ekstraoppgaver Presentasjoner

::Driftstøtte
cd C:\Users\nil2612\OneDrive - Telemark fylkeskommune\VG2\Driftsstotte\
mkdir Oppgaver Ekstraoppgaver Presentasjoner

::Norsk
cd C:\Users\nil2612\OneDrive - Telemark fylkeskommune\VG2\Norsk\
mkdir Oppgaver Ekstraoppgaver Presentasjoner

::Samfunnsfag
cd C:\Users\nil2612\OneDrive - Telemark fylkeskommune\VG2\Samfunnsfag\
mkdir Oppgaver Ekstraoppgaver Presentasjoner

::Utvikling
cd C:\Users\nil2612\OneDrive - Telemark fylkeskommune\VG2\Utvikling\
mkdir Ovelser Oppgaver Ekstraoppgaver Personlig
cd C:\Users\nil2612\OneDrive - Telemark fylkeskommune\VG2\Utvikling\Personlig\
mkdir Python HTML CSS JavaScript PHP


::Yrkesfagligfordypning
cd C:\Users\nil2612\OneDrive - Telemark fylkeskommune\VG2\Yrkesfagligfordypning\
mkdir Oppgaver Ekstraoppgaver Presentasjoner

echo "Du har nå opprettet mappen VG2 med undermapper."
echo %time%
timeout 5 > NUL

::Laget av Nils Martin Hoksrud