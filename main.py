import math

def z1():
    a = math.e ** 10
    print(a)

    b = pow(math.log1p(5+math.sin(8)**2), 1/6)
    print(b)

    c = math.floor(3.55)
    print(c)

    d = math.ceil(4.80)
    print(d)

def z2():
    firstname = "ANTON"
    secondname = "YANCHUK"
    print(secondname.capitalize() + " " + firstname.capitalize())

def z3():
    song = "la la la"
    x = song.count('la')
    print(x)

def z4():
    abc = "Qwerty"
    print(abc[1], abc[-1])

def z5():
    z5 = "Qaz Wsc"
    print(z5.split())

def z6():
    z6s = "Edc"
    z6f = 14.413
    z6 = 5414315
    fin = "{} {:f} {:X}".format(z6s, z6f, z6)
    print(fin)

def z7():
    dct = {
        "http": "HyperText Transfer Protocol",
        "url": "Uniform Resource Locator",
        "HTML": "HyperText Markup Language",
        "API": "Application Programming Interface"
    }
    print(dct.items())
def z8():
    games = {
        "Portal": "The cake is a lie",
        "GTA SA": "Ah shit, here we go again",
        "God Of War": "Boy"
    }
    print(len(games))

def z9():
    n = str(input())
    j = 0
    for i in n:
        if i == "a":
            j += 1
    print(j)

def z10():
    a = int(input("Enter number: "))
    b = int(input("Enter number: "))
    c = int(input("Enter number: "))

    if a >= b and a >= c:
        print(a)
    elif b >= a and b >= c:
        print(b)
    else:
        print(c)

def z11():
    lst = [1, 2, 3, 4, 5, 1.1, 2.2, 3.3, 4.4, 5.5]
    print([i ** 2 for i in lst])

def z12():
    lst = []
    j = 0
    while j != 10:
        a = int(input("Enter number: "))
        j += 1
        if a % 2 == 0:
            lst.append(a)

    print(lst)

