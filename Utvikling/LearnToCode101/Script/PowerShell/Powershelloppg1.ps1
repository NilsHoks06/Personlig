#Vis de 5 nyeste feilmeldinger i systemloggen 

get-eventlog -logname system -newest 5 | select-object entrytype, message, source