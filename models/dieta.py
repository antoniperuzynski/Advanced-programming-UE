from datetime import datetime


class Dieta:

    def __init__(self, dieta_name: str, price: float,
                 last_modified: datetime, kalorie: float,
                 ):
        self._dieta_name = dieta_name
        self._price = price
        self._last_modified = last_modified
        self._kalorie = kalorie

    @property
    def dieta_name(self):
        return self._dieta_name

    @property
    def price(self):
        return self._price

    @property
    def last_modified(self):
        return self._last_modified

    @property
    def kalorie(self):
        return self._kalorie

    def __str__(self) -> str:
        return '%s(%s)' % (
            type(self).__name__,
            ', '.join('%s' % vars(self)[item] for item in vars(self))
        )

    def __repr__(self):
        return self.__str__()
