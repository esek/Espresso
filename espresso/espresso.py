#!/usr/bin/env python
import espresso.datahandler as dh
import espresso.nfchandler as nfc

# Om denna filen körs direkt, gör detta. Om denna fil modul importeras görs ingetd
def main():
    """Denna metod körs då 'espresso' körs i kommandotolken.
    """
    nfc.test()