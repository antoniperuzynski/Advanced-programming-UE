from models.czlowiek import Czlowiek
from models.dieta import Dieta
from datetime import datetime


class Zamowienie:

    _zamowienie_id: int
    _date: datetime
    _diety: list[Dieta]
    _status: str
    _czlowiek: Czlowiek

    def __init__(self):
        pass

    @property
    def zamowienie_id(self):
        return self._zamowienie_id

    @zamowienie_id.setter
    def zamowienie_id(self, zamowienie_id: int):
        self._zamowienie_id = zamowienie_id

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date: datetime):
        self._date = date

    @property
    def diety(self):
        return self._diety

    @diety.setter
    def diety(self, diety: list[Dieta]):
        self._diety = diety

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status: str):
        self._status = status

    @property
    def czlowiek(self):
        return self._czlowiek

    @czlowiek.setter
    def czlowiek(self, czlowiek: czlowiek):
        self._czlowiek = czlowiek

    def __str__(self) -> str:
        return '%s(%s)' % (
            type(self).__name__,
            ', '.join('%s' % vars(self)[item] for item in vars(self))
        )

    def calculate_total_price(self):
        total_price = 0.0
        for p in self._diety:
            total_price += p.price
        return round(total_price, 2)

    def calculate_total_kcal(self):
        total_kcal = 0.0
        for p in self._diety:
            total_kcal += p.kalorie
        return round(total_kcal, 2)
