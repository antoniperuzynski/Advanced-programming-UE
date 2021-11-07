# Zadanie 2
import datetime
from A_lab_3_zad1 import Student
from typing import List


class Library:
    def __init__(
        self, city: str, street: str, zip_code: str, open_hours: str, phone: str
    ):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f"""
        City: {self.city}, Zip code: ({self.zip_code}), Street: {self.street}, 
        Open hour: {self.open_hours}, 
        Phone number: {self.phone}
        """


class Employee:
    def __init__(
        self,
        first_name: str,
        last_name: str,
        hire_date: datetime.date,
        birth_date: datetime.date,
        city: str,
        street: str,
        zip_code: str,
        phone: str,
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return f"""
        First name: {self.first_name}
        Last name: {self.last_name}
        Birth date: {self.birth_date}
        Hire date: {self.hire_date}
        City: {self.city}, Zip code: ({self.zip_code}), Street: {self.street}, 
        Phone number: {self.phone}
        """


class Book:
    def __init__(
        self,
        library: Library,
        publication_date: datetime.date,
        author_name: str,
        author_surname: str,
        number_of_pages: int,
    ):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return f"""
        Author name: {self.author_name}, author surname: {self.author_surname}, \n 
        Publication date: {self.publication_date}, \n
        Number of pages: {self.number_of_pages}, \n
        Located in: {self.library.__str__()}
        """


class Order:
    def __init__(
        self,
        employee: Employee,
        student: Student,
        books: List[Book],
        order_date: datetime.date,
    ):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        orderedbooks = "; ".join(
            [" ".join(book.__str__().replace("\n", "").split()) for book in self.books]
        )

        return f"""
        Ordered by: {self.employee} 
        Student: {self.student}, \n
        Ordered books: {orderedbooks}. \n
        Date {self.order_date}
        """


Lib_1 = Library("Bytom", "Felinskiego 5", "41-923", "9:00 - 15:30", "+48 111 111 111")
Lib_2 = Library("Gliwice", "Strzody 12/2", "22-112", "8:00-17:30", "+48 222 111 000")

Book_1 = Book(Lib_1, datetime.date(1999, 1, 1), "Mateusz", "Grzesiak", 410)
Book_2 = Book(Lib_1, datetime.date(1998, 2, 2), "Marcin", "Iwuć", 420)
Book_3 = Book(Lib_1, datetime.date(1997, 3, 3), "Andrzej", "Sapkowski", 430)
Book_4 = Book(Lib_2, datetime.date(1996, 4, 4), "Richard", "Freyman", 440)
Book_5 = Book(Lib_2, datetime.date(1995, 5, 5), "Joanne", "Murray", 450)

Employee_1 = Employee(
    "Dawid",
    "Mucha",
    datetime.date(2021, 4, 1),
    datetime.date(1999, 12, 6),
    "Bytom",
    "Felinskiego 38",
    "41-923",
    "+48 600 700 800",
)
Employee_2 = Employee(
    "Marcin",
    "Krzesinski",
    datetime.date(2020, 1, 7),
    datetime.date(1999, 8, 9),
    "Gliwice",
    "Rynek 5",
    "40-200",
    "+48 100 200 300",
)
Employee_3 = Employee(
    "Kacper",
    "Gradek",
    datetime.date(2021, 7, 19),
    datetime.date(1999, 6, 24),
    "Zabrze",
    "Wolnosci 1",
    "42-111",
    "+48 400 500 600",
)

Student_1 = Student("Irek Sobstyl", 70)
Student_2 = Student("Sebastian Nowak", 80)
Student_3 = Student("Bartosz Kurek", 90)

Order_1 = Order(Employee_1, Student_1, [Book_1, Book_2, Book_3], datetime.datetime.now())
Order_2 = Order(Employee_3, Student_2, [Book_4, Book_5], datetime.datetime.now())

print(Order_1)
print(Order_2)
