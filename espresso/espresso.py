#!/usr/bin/env python
import espresso.datahandler as dh
import espresso.nfchandler as nfc
import espresso.mail as mail
import datetime

# Om denna filen körs direkt, gör detta. Om denna fil modul importeras görs ingetd
def main():
    """Denna metod körs då 'espresso' körs i kommandotolken.
    """
    try: 
        while True:
        """ Detta är huvudloopen. Körs hela tiden.
        """
        read_cups = ncf.read()  # Läser in från läsaren
        add_cups(read_cups)
        if mail.is_time_to_send_mail():
            # Lägg till inläsning av JSON
            mail.send_mail(json_file)
    except Exception e:     # Bara starta
        print(str(e))
        main()

def add_cups(read_cup):
    """ Lägger till inlästa koppar
    """

def add_local_cup(date=datetime.datetime.now()):
    """Backup för hur många koppar kaffe som druckits, 
    noterar i lokal .txt-fil
    """
    date_string = date.strftime('%Y-%m-%d')

    with open("./data/backup.txt", "r+") as bu:     # r+ ANNARS FLIPPAR DEN UT
        """Vi kollar om sista raden är dagens datum, 
        annars lägger vi till det
        """

        line_list = bu.readlines()
        
        if not line_list:   # Om vår lista är tom
            line_list.append(date_string + ": " + "1")
            bu.write("".join(line_list))
        else:
            last_line = line_list[-1]   # Sista elementet har index -1

            if date_string in last_line:
                last_line_list = last_line.split()
                new_number = int(last_line_list[-1]) + 1   # Nya nummret är ordet längst till höger på sista raden + 1
                last_line_list[-1] = " " + str(new_number)   # Skapar en ny sista rad med nya antalet kaffe
                new_last_line = "".join(last_line_list)
                line_list[-1] = new_last_line   # Lägger in nya sista raden bland alla rader
            else:
                line_list.append("\n" + date_string + ": " + "1")
            
            # Dessa två rader raderar hela filen så vi kan skriva den nya
            bu.seek(0)
            bu.truncate()

            bu.write("".join(line_list))  # Lägger in alla rader på nytt
    bu.close()