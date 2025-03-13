#Vis liste over PDF-filer som er opprettet etter 20. juni 2019

Get-ChildItem -Path "C:\Users\nil2612\OneDrive - Telemark fylkeskommune" -Recurse -filter "*.pdf" | Where-Object {$_.CreationTime -ge (get-date 2019.06.20)}

get-childitem -path "C:\Users\nil2612\OneDrive - Telemark Fylkeskommune" -filter "*.pdf" -recurse | where-object {$_.CreationTime -ge (get-date 2019.06.20)} | select-object Name, CreationTime