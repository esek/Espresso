import pyodbc

# Importerar våra lösenord, servernamn m.m.
secrets_file = open("../secrets/secrets.txt", "r") # Läser in vår fil med hemligheter
driver = secrets_file.read(0)
server = secrets_file.read(1)
database = secrets_file.read(2)
uid = secrets_file.read(3)
pwd = secrets_file.read(4)
secrets_file.close()

# String med detaljer om anslutning, använder variabler från ../secrets/
connection_string = "DRIVER={0};SERVER={1};DATABASE={2};UID={3};PWD={4};charset=utf8mb4;".format(driver, server, database, uid, pwd)

class Datahandler:
    """Klass att hantera uppkoppling med databasen och hantera queries
    """

    def __init__(self):
        pass # Vi vill inte göra ngt

    def establish_connection(self): 
        """Försöker skapa en connection med databasen
        """
        try:
            self.cnxn = pyodbc.connect(connection_string)
        except Exception as e:
           raise e
    
    