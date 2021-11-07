# Zadanie 3

class Property:
    def __init__(self, area: str, rooms: int, price: float, address: str) -> None:
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self) -> str:
        return f"""
        Area: {self.area}
        Rooms: {self.rooms}
        Price: {self.price}
        AdDress: {self.address} 
        """


class House(Property):
    def __init__(self, area: str, rooms: int, price: float, address: str, plot: int) -> None:
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self) -> str:
        return f"""
        Area: {self.area}
        Rooms: {self.rooms}
        Price: {self.price}
        Address: {self.address} 
        Plot: {self.plot}
        """


class Flat(Property):
    def __init__(self, area: str, rooms: int, price: float, address: str, floor: int) -> None:
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self) -> str:
        return f"""
        Area: {self.area}
        Rooms: {self.rooms}
        Price: {self.price}
        Address: {self.address} 
        Floor: {self.floor}
        """


House1 = House('100 m2', 4, 123041, 'Bytom 3 Maja 3', 3)
Flat1 = Flat('52 m2', 2, 123041, 'Bytom 3 Maja 3', 3)
print(House1)
print(Flat1)
