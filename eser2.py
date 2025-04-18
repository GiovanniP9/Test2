import mysql.connector

class Database:
    def __init__(self):
        self.conn = None
        self.cursor = None
    
    #metodo per connettersi al database
    def connetti_db(self, nome_db):
        self.crea_database(nome_db)
        self.conn = mysql.connector.connect(
            host="localhost",
            user = "root",
            password = "GiFeTe251098?", #mettere la password del proprio database
            database = nome_db
        )
        self.cursor = self.conn.cursor()
        self.crea_tabella()
    
    def crea_database(self, nome_db):
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="GiFeTe251098?", #mettere la password del proprio database
        )
        cursor = conn.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {nome_db}")
        conn.close()
    
    def crea_tabella(self):  
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS utenti (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(255) NOT NULL,
                password VARCHAR(255) NOT NULL
            );
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS contatti (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(255),
                telefono VARCHAR(20),
                email VARCHAR(255),
                id_utente INT,
                FOREIGN KEY (id_utente) REFERENCES utenti(id)
            );
        """)
        self.conn.commit()

class Utente:
    def __init__(self, db:Database):
        # Inizializza l'oggetto utente con il database passato come parametro
        self.db = db
        self.id = None
        self.nome = None
    #metodo per registrare un utente   
    def registra(self):
        print("Registrazione utente")
        self.nome = input("Nome: ")
        password = input("Password: ")
        self.db.cursor.execute("INSERT INTO utenti (nome, password) VALUES (%s, %s)", (self.nome, password))
        self.db.conn.commit()
        print("Registrazione completata.")
    #metodo per il login di un utente    
    def login(self):
        print("Login utente")
        self.nome = input("Nome: ")
        password = input("Password: ")
        self.db.cursor.execute("SELECT id FROM utenti WHERE nome = %s AND password = %s", (self.nome, password))
        result = self.db.cursor.fetchone()
        if result:
            self.id = result[0]
            print("Login effettuato.")
            return True
        else:
            print("Nome o password errati.")
            return False

class Rubrica:
    def __init__(self, db:Database, utente:Utente):
        # Inizializza l'oggetto rubrica con il database e l'utente passato come parametro
        self.db = db
        self.utente = utente
    
    #metodo per aggiungere un contatto alla rubrica
    def aggiungi_contatto(self):
        if not self.utente.id:
            print("Devi effettuare il login prima di aggiungere un contatto.")
            return
        
        nome = input("Nome contatto: ")
        telefono = input("Telefono contatto: ")
        email = input("Email contatto: ")
        
        self.db.cursor.execute("INSERT INTO contatti (nome, telefono, email, id_utente) VALUES (%s, %s, %s, %s)", (nome, telefono, email, self.utente.id))
        self.db.conn.commit()
        print("Contatto aggiunto.")
    
    #metodo per visualizzare i contatti della rubrica
    def visualizza_contatti(self):
        if not self.utente.id:
            print("Devi effettuare il login prima di visualizzare i contatti.")
            return
        
        self.db.cursor.execute("SELECT nome, telefono, email FROM contatti WHERE id_utente = %s", (self.utente.id,))
        contatti = self.db.cursor.fetchall()
        
        if not contatti:
            print("Nessun contatto trovato.")
            return
        
        for contatto in contatti:
            print(f"Nome: {contatto[0]}, Telefono: {contatto[1]}, Email: {contatto[2]}")
    #metodo per eliminare un contatto dalla rubrica
    def elimina_contatto(self):
        if not self.utente.id:
            print("Devi effettuare il login prima di eliminare un contatto.")
            return
        
        nome = input("Nome contatto da eliminare: ")
        
        self.db.cursor.execute("DELETE FROM contatti WHERE nome = %s AND id_utente = %s", (nome, self.utente.id))
        self.db.conn.commit()
        print("Contatto eliminato.")
    #metodo per modificare un contatto della rubrica
    def modifica_contatto(self):
        if not self.utente.id:
            print("Devi effettuare il login prima di modificare un contatto.")
            return
        
        nome = input("Nome contatto da modificare: ")
        
        self.db.cursor.execute("SELECT id FROM contatti WHERE nome = %s AND id_utente = %s", (nome, self.utente.id))
        result = self.db.cursor.fetchone()
        
        if not result:
            print("Contatto non trovato.")
            return
        
        id_contatto = result[0]
        
        nuovo_nome = input("Nuovo nome contatto: ")
        nuovo_telefono = input("Nuovo telefono contatto: ")
        nuova_email = input("Nuova email contatto: ")
        
        self.db.cursor.execute("UPDATE contatti SET nome = %s, telefono = %s, email = %s WHERE id = %s", (nuovo_nome, nuovo_telefono, nuova_email, id_contatto))
        self.db.conn.commit()
        print("Contatto modificato.")

def menu():
    nome_db = input("Inserisci il nome del database: ")
    db = Database()
    db.connetti_db(nome_db)
    utente = Utente(db)
    
    print("Benvenuto nella rubrica!")
    while True:
        print("\nMenu:")
        print("1. Registrati")
        print("2. Login")
        
        scelta = input("Scegli un'opzione: ").strip()
        
        match scelta:
            case "1":
                utente.registra()
            case "2":
                if utente.login():
                    rubrica = Rubrica(db, utente)
                    while True:
                        print("\nMenu Rubrica:")
                        print("1. Aggiungi contatto")
                        print("2. Visualizza contatti")
                        print("3. Elimina contatto")
                        print("4. Modifica contatto")
                        print("5. Logout")
                        
                        scelta_rubrica = input("Scegli un'opzione: ").strip()
                        
                        match scelta_rubrica:
                            case "1":
                                rubrica.aggiungi_contatto()
                            case "2":
                                rubrica.visualizza_contatti()
                            case "3":
                                rubrica.elimina_contatto()
                            case "4":
                                rubrica.modifica_contatto()
                            case "5":
                                break
            case "3":
                print("uscita.")
                break
        
menu()
