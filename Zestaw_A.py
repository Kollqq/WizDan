import math
def zad1():
    try:
        a = int(input("Enter a: "))
        b = int(input("Enter b: "))
    except:
        if type(a) or type(b) != int:
            print("a and b must be INT")

    c = a ** 2 + a * b + b ** 2
    with open("zadanie1.txt", "w") as file:
        file.write(str(c))

def zad2(list1, list2):
    list3 = []
    for i in range(len(list1)):
        a = list1[i] + list2[i]
        list3.append(a)
    print(list3)

def zad3():
    with open("C:\\Users\\anton\\OneDrive\\Desktop\\Мусорка\\tekst.txt", "r", encoding="utf-8") as file:
        a = file.read(100)
        b = file.read(35)
        list1 = []
        for ch in b:
            if ch.isupper():
                list1.append(ch)
        if sum(1 for ch in b if ch.isupper()) != 0:
            print(list1 ,sum(1 for ch in b if ch.isupper()))
        else:
            print("Oops..")

def zad4():
    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    a = 4
    list2 = [i for i in list1 if i > a]
    print(list2)

def zad5():
    a = pow(pow(math.e, 3)+pow(math.cos(39), 2), 1/5)+pow(2/7, 3)+ math.pi
    print("%.2f" % a)

zad5()