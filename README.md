# Espresso

## Struktur

En NFC-läsare läser av LU-kortet, och visar kortets unika ID på en display. Därefter läggs tiden och datum koppen kaffe blippades till i dagens totala kaffeanvändning och en query i en buffert. Efter ett visst tidsintervall skickas tid och datum samt kort-id till ett table i sektionens SQL-databas. Varje kort-id har en UNIQUE rad i tabellen, tillsammans med en UNIQUE rad för Stil-ID (som från början är tom),samt koloumner för datum där tidpunkter för kaffe sparas.

Genom att gå in på sin användarsidan på eee.esek.se kan man "claima" ett kort-id. Då går man med på GDPR-trams och ens namn dyker upp i topplistan/man får tillgång till sin statistik. Man kan ej claima ett kort-id som redan används av någon annan.

Allt är kodat i Python, förutom där det inte behövs.

## Filer och program

Prelimenär updelning av kod. Samtlig kod finns i undermappen `espresso`. Här finns `__main__.py` också.

* NFC-hantering i `nfchandler.py`
* Buffer och hantering av totalt antal koppar kaffe i `cupcounter.py`.
* Kommunikation med databas och struktur på queries i `datahandler.py`
* Versionsnummer, requirements etc. finns i `setup.py`.
