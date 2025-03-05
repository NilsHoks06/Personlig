#Bytt navn på bilder

Get-ChildItem -Path "D:\Bilder\" "*.png" | Rename-Item -NewName {$_.Name -replace "image", "sommar"}