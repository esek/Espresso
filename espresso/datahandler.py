import pyodbc
import datetime

# Importerar våra lösenord, servernamn m.m.
with open("./secrets/secrets.txt", "r") as sf: # Läser in vår fil med hemligheter
    driver = sf.read(0)     # Läser texten en rad i taget
    server = sf.read(1)
    database = sf.read(2)
    uid = sf.read(3)
    pwd = sf.read(4)
    table = sf.read(5)

# String med detaljer om anslutning, använder variabler från ../secrets/
connection_string = "DRIVER={0};SERVER={1};DATABASE={2};UID={3};PWD={4};charset=utf8mb4;".format(driver, server, database, uid, pwd)

def establish_connection(): 
    """Försöker skapa en connection med databasen och returnerar den
    """
    try:
        return pyodbc.connect(connection_string)    # Sök diod
    except Exception as e:
        raise e
    
def add_cup(card_id, timestamp=datetime.datetime.now()):  # Default är att vi sätter dagens datum och tiden nu
    """Lägger till en kopp i form av timestamp i date i databasen med id=card_id
    Kastar exceptions om SQL inte vill.
    """
    
    sql_query =  "INSERT INTO ? (CARD_ID, TIMESTAMP) VALUES (?, ?)"  # Vår query. ? är för sanitering

    try:
        connection = establish_connection()    # Lesgo
        crs = connection.cursor()  # crs == cursorn som utför vad vi vill
        crs.execute(sql_query, table, card_id, timestamp)    # Utför vår (saniterade) query
        connection.commit()   # Commitar det som gjordes av crs.
    except Exception as e:
        raise e

    connection.close()    # Stänger vår connection