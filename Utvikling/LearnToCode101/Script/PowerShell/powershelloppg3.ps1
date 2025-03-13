#Vis tjenester som starter manuelt og har "Update" i displaynavnet

Get-Service | Where-Object {$_.DisplayName -match "Update" -And $_.StartType -eq "Manual"} | Select-Object DisplayName, StartType