# Zadanie 2a
names = ['Antoni', 'Karolina', 'Asia', 'Irek', 'Martyna']


def listofname(eachname):
    for name in eachname:
        print(name)


print('Zadanie 2a')
listofname(names)

# Zadanie 2b1
listofnumber = [1, 2, 3, 4, 5]


def numbers(list2):
    for it in range(len(list2)):
        list2[it] = list2[it] * 2
    return list2


print('Zadanie 2b1')
print(numbers(listofnumber))

# Zadanie 2b2
listofnumber2 = [1, 2, 3, 4, 5]


def numbers2(list3):
    return [2 * tmp for tmp in list3]


print('Zadanie 2b2')
print(numbers2(listofnumber2))

# Zadanie 2c
list4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('Zadanie 2c')
for i in range(len(list4)):
    if list4[i] % 2 == 0:
        print(list4[i])

# Zadanie 2d
print('Zadanie 2d')
list5 = [2 * i + 1 for i in range(10)]
print(list5)
for i in range(len(list5)):
    if i % 2 == 1:
        print(list5[i])
