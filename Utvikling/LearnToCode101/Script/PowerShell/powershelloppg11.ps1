#Sjekk Chrome versjon
{Get-Item "C:\Program Files\Google\Chrome\Application\chrome.exe"}.VersionInfo | Select-Object ProductVersion, FileVersion


#Gjennomgang:
#Get-item henter en singel fil/exe/mappe og versionInfo gir deg informasjon om programmet sin versjon.
{Get-Item "C:\Program Files\Google\Chrome\Application\chrome.exe"}.VersionInfo 
#Select-object velger ut egenskaper som navn i dette tilfelle er det ProductVersion og FileVersion
Select-Object ProductVersion, FileVersion