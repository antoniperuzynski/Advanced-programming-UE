from models.czlowiek import Czlowiek


class Pacjent(Czlowiek):

    def __init__(self, firstname: str, lastname: str, phone_number: str,
                 address: str, pacjent_disease: str):
        super().__init__(firstname, lastname, phone_number, address)
        self.pacjent_disease = pacjent_disease

    @property
    def pacjent_number(self):
        return self.pacjent_disease

    def __str__(self) -> str:
        return '%s(%s)' % (
            type(self).__name__,
            ', '.join('%s' % vars(self)[item] for item in vars(self))
        )
