import math
def z1():
    with open("C:\\Users\\anton\\Downloads\\tekst.txt", "r", encoding="utf-8") as file:
        a = file.read(70)
        b = file.read(40)
        if sum(1 for ch in b if ch == "A") != 0:
            print(sum(1 for ch in b if ch == "A"))
        else:
            print("Oops...")

def z2():
    list1 = [1, 2, 3, 4, 5.1, 6.2, 7.3, 8.4, 9.5]
    list2 = [i for i in list1 if type(i) == float]
    print(list1, list2)

def z3(list1):
    list2 = [i+list1[0] for i in list1]
    print(list1 + list2)

def z4():
    a = math.pow(math.sin(56), 2) + math.pow((4**2)/25 + math.log(85, 3), 1/4)
    print("%.2f" % a)

