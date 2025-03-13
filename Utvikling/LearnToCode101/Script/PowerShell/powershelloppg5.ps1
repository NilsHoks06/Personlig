#List opp PDF filer opprettet før 17 august 2019

Get-ChildItem -Path "" *.pdf -file | Where-Object {$_.CreationTime -ge (Get-Date 2019.08.17)} | Select-Object Name, CreationTime
