#Finn mapper med navn B

Get-ChildItem -Path "D:\Backup" -Directory -Recurse | Where-Object {$_.CreationTime -ge (Get-Date "2022.01.01") -and $_.Name -like "B*"}

#Gjennomgang:

Get-ChildItem -Path "D:\Backup" -Directory -Recurse | Where-Object {$_.CreationTime -ge (Get-Date "2022.01.01") -and $_.Name -like "B*"}