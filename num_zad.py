import numpy as np

def zad1():
    a = np.arange(4, 4*20+1, 4)
    print(a)

def zad2():
    a = np.arange(2, 5, 0.5)
    print(a)

    b = a.astype('int32')
    print(b)

def zad3(n):
    a = np.diag([2*i for i in range(n)])
    print(a)

    a = np.zeros((n*n), dtype="int32")
    for i in range(0, len(a)):
        a[i] = 2**i
    tab = a.reshape((n, n))
    return tab
def zad4(liczba, ilosc):
    c = np.logspace(1, ilosc, num=ilosc, base=liczba)
    return c

def zad5(n):
    a = np.arange(n, -1, -1)
    diag = np.diag(a, 2)

    return diag

def zad6():
    malina = np.array(list('malina'))
    mrowka = np.array(list('mrowka'))
    armata = np.array(list('armata'))
    armata = np.flip(armata)

def zad7(n):
    mac = np.zeros((n, n), dtype='int32')
    mac += np.diag([2 for _ in range(n)])
    for i in range(1, n):
        mac += np.diag([2+(2*i) for _ in range(n-1)], k=i)
        mac += np.diag([2+(2*i) for _ in range(n-1)], k=-i)
    print(mac)

zad7(3)

