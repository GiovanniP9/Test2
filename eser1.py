
class Veicolo: #classe veicolo, classe padre
    def __init__(self, marca, anno, targa, revisione):
        self._marca = marca
        self._anno = anno
        self._targa = targa
        self._revisione = revisione
    
    def get_marca(self):
        return self._marca
    def set_marca(self, marca):
        self._marca = marca
    def get_anno(self):
        return self._anno
    def set_anno(self, anno):
        self._anno = anno
    def get_targa(self):
        return self._targa
    def set_targa(self, targa):
        self._targa = targa
    def get_revisione(self):
        return self._revisione
    def set_revisione(self, revisione):
        self._revisione = revisione
    
    def descrivi(self): # classe da sovrascrivere
        pass

class Auto(Veicolo):# classe auto
    def __init__(self, marca, anno, targa, revisione, porte):
        super().__init__(marca, anno, targa, revisione)
        self.__porte = porte
    
    def get_porte(self):
        return self.__porte
    def set_porte(self, porte):
        self.__porte = porte
    
    def descrivi(self):
        return f"Auto: {self.get_marca()}, {self.get_anno()}, {self.get_targa()}, {self.get_revisione()}, {self.get_porte()} porte"  
        
class Moto(Veicolo):# classe moto
    def __init__(self, marca, anno, targa, revisione, cilindrata):
        super().__init__(marca, anno, targa, revisione)
        self.__cilindrata = cilindrata
    
    def get_cilindrata(self):
        return self.__cilindrata
    def set_cilindrata(self, cilindrata):
        self.__cilindrata = cilindrata
    
    def descrivi(self):
        return f"Moto: {self.get_marca()}, {self.get_anno()}, {self.get_targa()}, {self.get_revisione()}, {self.get_cilindrata()} cc"
    
class Camion(Veicolo):# classe camion
    def __init__(self, marca, anno, targa, revisione, carico):
        super().__init__(marca, anno, targa, revisione)
        self.__carico = carico
        
    def get_carico(self):
        return self.__carico
    def set_carico(self, carico):
        self.__carico = carico
    def descrivi(self):
        return f"Camion: {self.get_marca()}, {self.get_anno()}, {self.get_targa()}, {self.get_revisione()}, {self.get_carico()} kg"
    
#Lista di veicoli
veicoli = []

#Creazione di un'auto
def crea_veicolo():
    print("Crea un veicolo")
    tipo = input("Tipo (auto/moto/camion): ").strip().lower()
    marca = input("Marca: ").strip()
    
    try: # Controllo se l'anno è un intero
        anno = int(input("Anno: ").strip())
        targa = input("Targa: ").strip()
        revisione = input("Revisione (sì/no): ").strip().lower()
        revisione = True if revisione == "sì" else False
    except ValueError:
        print("Inserimenti non validi. Riprova.")
        return
    
    if tipo == "auto": 
        try: # Controllo se il numero di porte è un intero
            porte = int(input("Numero di porte: ").strip())
            veicolo = Auto(marca, anno, targa, revisione, porte)
        except ValueError:
            print("Inserimenti non validi. Riprova.")
            return
    elif tipo == "moto":
        try:# Controllo se la cilindrata è un intero
            cilindrata = int(input("Cilindrata: ").strip())
            veicolo = Moto(marca, anno, targa, revisione, cilindrata)
        except ValueError:
            print("Inserimenti non validi. Riprova.")
            return
    elif tipo == "camion":
        try:# Controllo se il carico è un intero
            carico = int(input("Carico: ").strip())
            veicolo = Camion(marca, anno, targa, revisione, carico)
        except ValueError:
            print("Inserimenti non validi. Riprova.")
            return
    else:
        print("Tipo di veicolo non valido. Riprova.")
        return
    veicoli.append(veicolo)

# Funzione per mostrare i veicoli
def mostra_veicoli():
    if not veicoli:
        print("Nessun veicolo presente.")
        return
    for veicolo in veicoli:
        print(veicolo.descrivi())
        
# Funzione per il menu principale
def menu():
    while True:
        print("\nMenu:")
        print("1. Crea veicolo")
        print("2. Mostra veicoli")
        print("3. Esci")
        
        scelta = input("Scegli un'opzione: ").strip()
        
        if scelta == "1":
            crea_veicolo()
        elif scelta == "2":
            mostra_veicoli()
        elif scelta == "3":
            break
        else:
            print("Opzione non valida. Riprova.")
menu()