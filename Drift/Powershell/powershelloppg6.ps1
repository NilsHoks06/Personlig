#Kopier filer basert på størrelse 1MB

Get-ChildItem -Path "C:\Bilder\" -Recurse | Where-Object {$_.Length -ge 1MB} | Copy-Item -Destination "C:\Bilde\"