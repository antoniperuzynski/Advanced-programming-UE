from models.czlowiek import Czlowiek


class Dietetyk(Czlowiek):

    def __init__(self, firstname: str, lastname: str, phone_number: str,
                 address: str, dietetyk_staz: str):
        super().__init__(firstname, lastname, phone_number, address)
        self.dietetyk_staz = dietetyk_staz

    @property
    def dietetyk_number(self):
        return self.dietetyk_staz

    def __str__(self) -> str:
        return '%s(%s)' % (
            type(self).__name__,
            ', '.join('%s' % vars(self)[item] for item in vars(self))
        )
