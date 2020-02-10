#!/usr/bin/env python
import espresso.datahandler as dh
import espresso.nfchandler as nfc
import datetime

# Om denna filen körs direkt, gör detta. Om denna fil modul importeras görs ingetd
def main():
    """Denna metod körs då 'espresso' körs i kommandotolken.
    """
    add_local_cup()
    nfc.test()

def add_local_cup(date=datetime.datetime.now()):
    """Backup för hur många koppar kaffe som druckits, 
    noterar i lokal .txt-fil
    """
    date_string = date.strftime('%Y/%m/%d')

    with open("./data/backup.txt", "r+") as bu:     # r+ ANNARS FLIPPAR DEN UT
        """Vi kollar om sista raden är dagens datum, 
        annars lägger vi till det
        """
        line_list = bu.readlines()
        last_line_index = len(line_list) - 1
        
        if not line_list:   # Om vår lista är tom
            print("Första")
            line_list.append(date_string + ": " + "1")
            bu.truncate()
            bu.write("".join(line_list))
        else:
            last_line = line_list[last_line_index]   # Sista index är längden -1

            if date_string in last_line:
                print("Andra if")
                last_line_list = last_line.split()
                new_number = int(last_line_list[len(last_line_list) - 1]) + 1   # Nya nummret är ordet längst till höger på sista raden + 1
                last_line_list[len(last_line_list) - 1] = " " + str(new_number)   # Dödsline som bara adderar en kopp kaffe
                print(last_line_list)
                new_last_line = "".join(last_line_list)

                # Dessa två rader raderar den tidigare sista raden
                bu.seek(len(line_list) - 1)
                bu.truncate()

                bu.write(new_last_line)  # Skapar en ny rad med vårt nya värde
            else:
                print("Sista")
                line_list.append("\n" + date_string + ": " + "1")
                bu.write("".join(line_list))
    bu.close()