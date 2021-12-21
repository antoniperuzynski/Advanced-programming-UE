from models.dieta import Dieta
from models.zamowienie import Zamowienie
from models.pacjent import Pacjent

from datetime import datetime

pacjent = Pacjent("antoni", "peruzynski", "123456", "13, Gliwice", "Otylosc")

dieta1 = Dieta("IFYM", 700, datetime(2021, 12, 9), 2500)
dieta2 = Dieta("Srodziemnomorska", 600, datetime(2021, 10, 12), 1800)
zamowienie = Zamowienie()
zamowienie.order_id = 1
zamowienie.client = pacjent
zamowienie.date = datetime(2021, 1, 13)
zamowienie.diety = [dieta1, dieta2]
zamowienie.status = "Dostarczone"

print(zamowienie)
