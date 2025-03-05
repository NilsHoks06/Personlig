#Finn txt filer først opprettet før 2020

Get-ChildItem -Path "" -Filter "*.txt" -Recurse | Where-Object {$_.CreationTime -lt (Get-Date "2020.01.01")}