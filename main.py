# a = 'napis \ndrugi napis'
# print(a)
#
# b = 5
# c = 5.5
# print(b,c)
#
# d = 5+3j
# print(d)
#
# e = c+d
# print(e)
#
# f = c//b
# print(f)
#
# h = b**2
# print(h)
#
# i = b**1/2
# j = pow(b, 1/2)
# print(i)
# print(j)
#
# print(str(b) + ' = b + 2')
# print('b = b + 2')
#
# print(b)
# b += 2
# print(b)
#
# listy = ['a', 4, 5, 6, [1, 2, 3], 5.6]
# print(listy)
#
# listy.append(78)
# print(listy)
#
# listy.insert(1, 56)
# print(listy)
#
# listy.pop(0)
# print(listy)
#
# listy.remove(4)
# print(listy)
#
# listy.reverse()
# print(listy)
#
# lista1 = [5,3,2,9,1,-43,-5]
# lista1.sort()
# print(lista1)
#
# print(listy + lista1)

# slownik = {
#     'a': 2,
#     'b': 3,
#     3: 89,
#     4: 'ab'
# }
# print(slownik)
#
# print(slownik['a'])
# slownik['klucz'] = 'wartosc'
# print(slownik)
# slownik.pop('klucz')
# print(slownik)
# print(slownik.keys())
# print(slownik.values())
#
# print('a=%(zm)d' % {'zm': 12})
# napis = 'a={}, b={}'
# print(napis.format(12, 12))

# result = True
#
# while result:
#
#     a = int(input('Enter first number: '))
#     b = int(input('Enter second number: '))
#
#     if a == b:
#         print('first number = second number')
#         result = False
#     elif a < b:
#         print('first number < second number')
#     else:
#         print('first number > second number')

# a = int(input('Enter a: '))
# b = int(input('Enter b: '))
# c = int(input('Enter c: '))
# d = int(input('Enter d: '))
#
# if (a > b) & (c > d):
#     print('a > b and c > d')
# else:
#     print('a < b and c < d')

# list = [1, 2, 3, 4, 5, [9,76,43], 'dsf']

# for i in range(1,6,1):
#     print('1')
# else:
#     print('The End')

# for i in list:
#     print(i)
#
# for i in range(0, len(list)):
#     print(list[i])

# licznik = 0
#
# while licznik != len(list):
#     print(list[licznik])
#     licznik += 1
#

# liczby = [3, 4, 5, 1, 7, 8]
#
# a = int(input('Enter number: '))
# licznik = 0

# while licznik != len(liczby):
#     if a - liczby[licznik] == 0:
#         print('{} - {} = 0'. format(a, liczby[licznik]))
#         break
#     licznik += 1

liczby = [1, 2, 2, 2, 4, 5, 6]

licznik = 0

while licznik != len(liczby):
    if liczby[licznik] == 2:
        liczby.pop(licznik)
    else:
        licznik += 1
print(liczby)