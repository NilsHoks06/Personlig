#Automatiser Sikkerhetskopi
#POWERSHELL ISE

if ((Get-Date -Format dddd) -eq "Monday"){

Copy-Item -Path "" -Recurse -Destination "" -Force}

#Gjennomgang:

if ((Get-Date -format dddd) -eq "Onsdag"){Copy-Item -path "C:\Data\" -destination "D:\Backup\" -recurse -force}