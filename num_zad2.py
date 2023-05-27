import numpy as np

def zad1():
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    print(a*b)

def zad2():
    a = np.arange(9).reshape((3, 3))
    b = np.arange(16).reshape((4, 4))
    print(a.min(axis=0))
    print(a.min(axis=1))
    print(b.min(axis=0))
    print(b.min(axis=1))

def zad3():
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    print(np.dot(a, b))

def zad4():
    a = np.array([4, 5, 6])
    b = np.array([1.2, 2.3, 3.4])
    print(a*b)

def zad5():
    b = np.arange(6).reshape(2, 3)
    a = np.sin(b)
    print(a)

def zad6():
    a = np.arange(6).reshape(2, 3)
    b = np.cos(a)
    print(b)

def zad7():
    b = np.arange(6).reshape(2, 3)
    a = np.sin(b)

    a = np.arange(6).reshape(2, 3)
    b = np.cos(a)
    print(a+b)

def zad8():
    a = np.arange(9).reshape(3, 3)
    for i in a:
        print(i)

def zad9():
    a = np.arange(9).reshape(3, 3)
    for i in a.flat:
        print(i)

def zad10():
    a = np.arange(81)
    a1 = a.reshape(9, 9)
    a2 = a.reshape(1, 81)
    a3 = a.reshape(81, 1)
    a4 = a.reshape(3, 27)
    a5 = a.reshape(27, 3)

    print(a1)
    print('')
    print(a2)
    print('')
    print(a3)
    print('')
    print(a4)
    print('')
    print(a5)
    print('')

def zad11():
    a = np.arange(12)
    b = a.reshape(3, 4)
    c = a.reshape(4, 3)
    d = a.reshape(2, 6)

    print(a)
    print(b.ravel())
    print(c.ravel())
    print(d.ravel())
