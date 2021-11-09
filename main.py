from typing import List


class Produkt:
    def __init__(self, nazwa: str, cena: float, wielkosc: float, dostepnosc: bool, marka: str):
        self.nazwa = nazwa
        self.cena = cena
        self.wielkosc = wielkosc
        self.dostepnosc = dostepnosc
        self.marka = marka

    @property
    def get_nazwa(self):
        return self.nazwa

    @property
    def get_cena(self):
        return self.cena

    @property
    def get_wielkosc(self):
        return self.wielkosc

    @property
    def get_dostepnosc(self):
        return self.dostepnosc

    @property
    def get_marka(self):
        return self.marka

    def __str__(self):
        return f"""
                       nazwa: {self.nazwa}
                       cena:{self.cena}
                       wielkosc: {self.wielkosc}
                       dostepnosc: {self.dostepnosc}
                       marka {self.marka}
                       """

class Magazyn:
    def __init__(self, wielkosc: int, miejscowosc, ulica, kodpocztowy, kraj):
        self.wielkosc = wielkosc
        self.miejscowosc = miejscowosc
        self.ulica = ulica
        self.kodpocztowy = kodpocztowy
        self.kraj = kraj

    def __str__(self):
        return f"""
                       wielkosc: {self.wielkosc}
                       miejscowosc:{self.miejscowosc}
                       ulica: {self.ulica}
                       kodpocztowy: {self.kodpocztowy}
                       kraj {self.kraj}
                       """

class KlientDetaliczny:
    def __init__(self, imie: str, nazwisko: str, wiek: int, adres: str, idklienta: int):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek
        self.adres = adres
        self.idklienta = idklienta

    def __str__(self):
        return f"""
                       imie: {self.imie}
                       nazwisko:{self.nazwisko}
                       wiek: {self.wiek}
                       adres: {self.adres}
                       idklienta {self.idklienta}
                       """

class Zamowienie:
    def __init__(self, idzamowienia: int, idklienta: int, produkty :List[Produkt], klient: KlientDetaliczny, ilosci: List[int]):
        self.idzamowienia = idzamowienia
        self.idklienta = idklienta
        self.produkty = produkty
        self.klient = klient
        self.ilosci = ilosci


    #@property
   # def idzamowienia(self, val: int) -> None:
    #    self.idzamowienia = val

   # @property
   # def idklienta(self, val: int) -> None:
     #   self.idklienta = val

   # @property
   # def klient(self, val: KlientDetaliczny) -> None:
     #   self.klient = val



    def __str__(self):
        orderedproducts = "; ".join(
            [" ".join(produkt.__str__().replace("\n", "").split()) for produkt in self.produkty]
        )

        ilosci = "; ".join(
            [" ".join(ilosc.__str__().replace("\n", "").split()) for ilosc in self.ilosci]
        )

        return f"""
                    idzamowienia: {self.idzamowienia}
                    idklienta:{self.idklienta}
                    produkt: {orderedproducts}
                    klient: {self.klient}
                    ilosci {ilosci}
                    """

    def wartosczamowienia(self):
        w=0
        for i in range(len(self.produkty)):
           w = w + self.produkty[i].cena * self.ilosci[i]
        return round(w,2)

    def jakiklient(self):
        return self.klient.adres

class KlientBieznesowy:
    def __init__(self, imie: str, nazwisko: str, adres: str, firma :str, idklientabiz: int):
        self.imie = imie
        self.nazwisko = nazwisko
        self.adres = adres
        self.firma = firma
        self.idklientabiz = idklientabiz

    def __str__(self):
        return f"""
                    Imie: {self.imie}
                    Nazwisko:{self.nazwisko}
                    Adres: {self.adres}
                    Firma: {self.firma}
                    IdKlientaBiznesowego: {self.idklientabiz}
                    """


Produkt1 = Produkt('ksiazka1', 10.5222, 11, 1, 'marka1')
Produkt2 = Produkt('ksiazka2', 20, 21, 1, 'marka2')
KlientDet1 = KlientDetaliczny('Imie1', 'nazwisko1', 70, 'Bytom', 1)
KlientBiz1 = KlientBieznesowy ('imie2', 'nazwisko2', 'adresbiznes', 'firmabiznes', 2)
Magazyn1 = Magazyn(200, 'miejscowoscmag', 'ulicamag', 111, 'kraj')
Zamowienie1 = Zamowienie (1, 1, [Produkt1,Produkt2], KlientBiz1, [1,2])
print(Zamowienie1)

#print(Zamowienie1.jakiklient())
#print(Zamowienie1.wartosczamowienia())



