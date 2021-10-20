# Zadanie 1
print("Zadanie 1")
def welcome (name: str, surname: str) -> str:
    return 'Czesc ' + name + ' ' + surname
zmienna1=welcome('Antek','Peruzynski')
print (zmienna1)

# Zadanie 2
print("Zadanie 2")
def mnozenie (a: int, b: int) -> int :
    return a*b
print(mnozenie(4,3))

# Zadanie 3
print("Zadanie 3")
def parzysta(a: int) -> bool:
    return  a%2==0
x=parzysta(9)

if x==True:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")

# Zadanie 4
print("Zadanie 4")
def suma2(a: int, b: int, c:int) -> bool:
    return  a+b >= c
print(suma2(2,3,6))

# Zadanie 5
print("Zadanie 5")
def list(a: int, lista: list) -> bool:
    return a in lista
print(list(3,[2,3,7,1,6]))

# Zadanie 6
print("Zadanie 6")
def connectlist(tab1: list, tab2: list) -> list:

    tab3=tab1+tab2
    unikatoweliczby=set(tab3)
    endtab=[]
    for i in unikatoweliczby:
        endtab.append(i**3)
    return endtab
print(connectlist([1,2,3,4,5],[5,6,7,8,9]))