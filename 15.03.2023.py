import random
import math

def z1():

    A = [x-1 for x in range(1,11)]
    print(A)

    B = [4**x for x in range(8)]
    print(B)

    C = [x for x in B if x % 2 == 0]
    print(C)

def z2():

    list1 = [random.randint(1,100) for i in range(10)]
    list2 = [i for i in list1 if i % 2 == 0]

    print(list1)
    print(list2)

def z3():

    produtky = {
        "Apple": "sztuki",
        "Orange": "sztuki",
        "Banana": "sztuki",
        "Milk": "litra",
        "Solt": "kg"
    }

    list1 = [values for values, key in produtky.items() if key == "sztuki"]
    print(list1)

def z4(a,b,c):

    if c > a and c > b and a**2 + b**2 == c**2:
        return print("Jest")
    if b > a and b > c and c**2 + a**2 == b**2:
        return print("Jest")
    if a > c and a > b and c**2 + b**2 == a**2:
        return print("Jest")
    else:
        return print("Nie jest")

def z5(a = 30,b = 20,c = 10):

    return print(((a+b)/2)*c)

def z6(a = 1, b = 4, ile = 10):
    s = 1
    for i in range(1, ile+1):
        a *= b
        s *= a
    return print(s)

def z7(*s):
    sum = 1
    for i in s:
        sum *= i
    return print(sum)

def z8(**spisok):
    s = 0
    for i in spisok:
        s += spisok[i]
    return print(len(spisok), s)

def z9(a):
    try:
        print(math.sqrt(a))
    except:
        print("Error")
