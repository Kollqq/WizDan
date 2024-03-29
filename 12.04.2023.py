import numpy as np

a = np.array([[0, 1], [2, 3], [4, 5]])
print(a)

a = np.arange(2, 5, 0.1)
print(a)

print(type(a))

print(a.dtype)

a = np.arange(6, dtype='int64')
print(a)
print(a.dtype)

b = a.astype('float')
print(b)

print(b.shape)

print(a.ndim)

m = np.array([np.arange(2), np.arange(2)])
print(m.shape)

print(type(m))

zera = np.zeros((5, 5))
print(zera)
print(zera.dtype)

jedynki = np.ones((4, 4))
print(jedynki)
print(jedynki.dtype)

pusta = np.empty((2, 2))
print(pusta)

macierz = np.array([[12, 11], [2, 1]])
print(macierz)

poz_1 = macierz[1, 1]
poz_2 = macierz[0][1]
print(poz_1)
print(poz_2)

liczby_lin = np.linspace(1, 2, 5, endpoint=False)
print(liczby_lin)

z = np.indices((5, 3))
print(z)
print(z[1][1][2])

mat_diag = np.diag([a for a in range(5)])
print(mat_diag)

mat_diag = np.diag([a for a in range(5)], 1)
print(mat_diag)

z = np.fromiter(range(5), dtype='int32')
print(z)

znaki = b'ogolna'
z1 = np.frombuffer(znaki, dtype='S1')
print(z1)
z2 = np.frombuffer(znaki, dtype='S2')
print(z2)

z3 = np.array(list(znaki))
z4 = np.array(list(znaki), dtype='S1')
z5 = np.array(list(b'ogolna'))
z6 = np.fromiter(znaki, dtype='S1')
print(z3)
print(z4)
print(z5)
print(z6)

a = np.arange(10)
print(a)
s = slice(2, 7, 2)
print(a[s])
s = range(2, 7, 2)
print(a[s])

print(a[2:7:2])

print(a[1:])
print(a[2:5])

mat = np.arange(25)

mat = mat.reshape(5, 5)
print(mat)
print(mat[1:])
print(mat[:, 1])
print(mat[:, -1])
print(mat[2:5, 1:3])
print(mat[:, [2, 4]])

x = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
print(x)
rows = np.array([[0, 0], [3, 3]])
cols = np.array([[0, 2], [0, 2]])
y = x[rows, cols]
print(y)
