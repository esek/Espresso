# Espresso

## Struktur
En NFC-läsare läser av LU-kortet, och visar kortets unika ID på en display. Därefter läggs tiden och datum koppen kaffe blippades till i dagens totala kaffeanvändning och en query i en buffert. Efter ett visst tidsintervall skickas tid och datum samt kort-id till ett table i sektionens SQL-databas. Varje kort-id har en UNIQUE rad i tabellen, tillsammans med en UNIQUE rad för Stil-ID (som från början är tom),samt koloumner för datum där tidpunkter för kaffe sparas.

Genom att gå in på sin användarsidan på eee.esek.se kan man "claima" ett kort-id. Då går man med på GDPR-trams och ens namn dyker upp i topplistan/man får tillgång till sin statistik. Man kan ej claima ett kort-id som redan används av någon annan.