from abc import ABC, abstractmethod
import math

class Forma(ABC):# classe astratta padre
    @abstractmethod
    def area(self): # calcola l'area 
        pass

    @abstractmethod
    def perimetro(self): # calcola il perimetro
        pass

class Cerchio(Forma): # classe cerchio
    def __init__(self, raggio):
        self.raggio = raggio

    def area(self):
        return math.pi * (self.raggio ** 2)

    def perimetro(self):
        return 2 * math.pi * self.raggio

class Rettangolo(Forma): # classe rettangolo
    def __init__(self, base, altezza):
        self.base = base
        self.altezza = altezza

    def area(self):
        return self.base * self.altezza

    def perimetro(self):
        return 2 * (self.base + self.altezza)

class Triangolo(Forma): # classe triangolo
    def __init__(self, lato1, lato2, lato3):
        self.lato1 = lato1
        self.lato2 = lato2
        self.lato3 = lato3
    
    def perimetro(self):
        return self.lato1 + self.lato2 + self.lato3
    
    def area(self):
        s = self.perimetro() / 2
        return math.sqrt(s * (s - self.lato1) * (s - self.lato2) * (s - self.lato3)) # formula di Erone

forme = []

# Funzioni per la gestione delle forme
def crea_forma():
    print("Scegli una forma:")
    print("1. Cerchio")
    print("2. Rettangolo")
    print("3. Triangolo")
    scelta = int(input("Inserisci il numero della forma: "))
    
    match scelta:
        case 1:
            raggio = float(input("Inserisci il raggio del cerchio: "))
            forma = Cerchio(raggio)
            forme.append(forma)
        case 2:
            base = float(input("Inserisci la base del rettangolo: "))
            altezza = float(input("Inserisci l'altezza del rettangolo: "))
            forma = Rettangolo(base, altezza)
            forme.append(forma)
        case 3:
            lato1 = float(input("Inserisci il primo lato del triangolo: "))
            lato2 = float(input("Inserisci il secondo lato del triangolo: "))
            lato3 = float(input("Inserisci il terzo lato del triangolo: "))
            forma = Triangolo(lato1, lato2, lato3)
            forme.append(forma)
        case _:
            print("Scelta non valida.")
            return

def mostra_forme():
    if not forme:
        print("Nessuna forma presente.")
        return
    for forma in forme:
        print(f"Forma: {forma.__class__.__name__}, Area: {forma.area()}, Perimetro: {forma.perimetro()}")

def perimetro_maggiore():
    if not forme:
        print("Nessuna forma presente.")
        return
    max_perimetro = max(forma.perimetro() for forma in forme)
    for forma in forme:
        if forma.perimetro() == max_perimetro:
            print(f"Forma con perimetro maggiore: {forma.__class__.__name__}, Perimetro: {max_perimetro}")

def menu():
    while True:
        print("\nMenu:")
        print("1. Crea forma")
        print("2. Mostra forme")
        print("3. Forma con perimetro maggiore")
        print("4. Esci")
        
        scelta = input("Scegli un'opzione: ").strip()
        
        match scelta:
            case "1":
                crea_forma()
            case "2":
                mostra_forme()
            case "3":
                perimetro_maggiore()
            case "4":
                print("Uscita dal programma.")
                break
            case _:
                print("Opzione non valida. Riprova.")

menu()