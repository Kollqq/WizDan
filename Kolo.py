import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# list1 = [1, 2, 3, 4, 5]
# arr = np.array(list1)
#
# print(arr)
#
# arr2 = np.array([5, 4, 3, 2, 1])
# print(arr2)
#
# arr3 = np.array([5, 4, 3, 2, 1], dtype=float)
# print(arr3)
#
# arr4 = arr3.astype(np.int64)
# print(arr4)
#
# arr5 = np.arange(1, 11)
# print(arr5)
#
# arr6 = np.linspace(0, 10, 3)
# print(arr6)
#
# random_arr = np.random.random(5)
# print(random_arr)

# arr = np.arange(1, 6)
# arr1 = np.sqrt(arr)
# print(arr)
# print(arr1)

# arr = np.arange(1,11)
# print(arr)
#
# print(arr[2])
# print(arr[0:2])
# print(arr[::-1])
# print(arr[0:6:2])
# print(arr[arr < 6])

# mat = np.array([(1, 2, 3),(4, 5, 6)])
# print(mat)
#
# mat3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
# print(mat3d)

# mat = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9)])
# print(mat)
# print(mat.shape)
# print(mat.ndim)
# print(mat.size)
#
# new_mat = mat.reshape(1, 9)
# print(new_mat)

# mat1 = np.array([(1, 2), (4, 5)])
# mat2 = np.array([(6, 5), (3, 2)])
# print(mat1+mat2)
# print(mat1.dot(mat2))

# mat = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9)])
# print(mat)
#
# print(np.sin(mat))
# print(np.sum(mat))
# print(mat.max(axis=1))

# mat = np.arange(9)
# print(mat.reshape(3,3))

# x = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
# print(x)
# rows = np.array([[0, 0], [3, 3]])
# cols = np.array([[0, 2], [0, 2]])
# y = x[rows, cols]
# print(y)


# plik = pd.ExcelFile('imiona.xlsx')
# df = pd.read_excel(plik, header=0)

# print(df)

# print(df[df.Liczba > 1000])

# print(df[df.Imie == 'ANTON'])

# print(df.Liczba.sum())

# grupa = df[df.Rok < 2006]
# print(grupa.Liczba.sum())

# grupa = df[df.Rok < 2006].groupby('Rok').agg({'Liczba': ['sum']})
# print(grupa)

# m = df[df.Plec == 'M']
# d = df[df.Plec == 'K']
#
# print(m.Liczba.sum())
# print(d.Liczba.sum())

# print(df[df['Plec'] == 'M'].groupby(['Imie']).agg({'Liczba' : ['sum']}).sort_values(('Liczba', 'sum'), ascending=False).iloc[0])
# print(df[df['Plec'] == 'K'].groupby(['Imie']).agg({'Liczba' : ['sum']}).sort_values(('Liczba', 'sum'), ascending=False).iloc[0])

# print(df.sort_values('Liczba', ascending=False).groupby(['Rok', 'Plec']).nth(0))

# new_df = df.sort_values('Liczba', ascending=False).groupby(['Rok', 'Plec'])
# for index, group in enumerate(new_df, start=1):
#     print(f"{index} {group[0]}")
#     print(f" {group[1].iloc[0]['Imie']}", end='')
#     print(f" {group[1].iloc[0]['Liczba']}")

# df = pd.read_csv('zamowienia.csv', header=0, sep=';', decimal='.')

# print(df)

# print(df['Sprzedawca'].unique())

# print(df.sort_values('Utarg', ascending=False).head(5))

# print(df.groupby('Sprzedawca').size())

# print(df.groupby('Kraj').agg({'Utarg': ['sum']}))

# print(df[(df['Kraj'] == 'Polska') & (df['Data zamowienia'] >= '2005-01-01') & (df['Data zamowienia'] <= '2005-12-31')].agg({'Utarg': ['sum']}))

# print(df[(df['Data zamowienia'] >= '2004-01-01') & (df['Data zamowienia'] <= '2004-12-31')].agg({'Utarg': ['mean']}))

# rok_2004 = df[((df[ 'Data zamowienia'] >= '2004-01-01') & (df['Data zamowienia'] <= '2004-12-31'))]
# print(rok_2004)
# rok_2004.to_csv("zamowienia_2004.csv", index=False)

# x = np.arange(1, 21)
# print(x)
# plt.plot(x, 1/x, label='f(x) = 1/x')
# plt.xlabel('x')
# plt.ylabel('f(x)')
# plt.axis([0, 20, 0, 1])
# plt.legend()
# plt.title('Wykres funkcji f(x) = 1/x dla x [1,20]')
# plt.show()

# x = np.arange(1, 21)
# print(x)
# plt.plot(x, 1/x, 'g>:', label='f(x) = 1/x')
# plt.xlabel('x')
# plt.ylabel('f(x)')
# plt.axis([0, 20, 0, 1])
# plt.legend()
# plt.title('Wykres funkcji f(x) = 1/x dla x [1,20]')
# plt.show()

# x = np.arange(0, 30.1, 0.1)
# plt.plot(x, np.sin(x), 'b', label='sin(x)')
# plt.plot(x, np.cos(x), 'r', label='sin(x)')
# plt.xlabel('x')
# plt.ylabel('sin(x) cos(x)')
# plt.legend(loc='upper right')
# plt.title('Wykres sin(x), cos(x)')
# plt.show()

# df = pd.read_csv('iris.data', header=0, sep=',', decimal='.')
# print(df)
# colors = np.random.randint(0, 50, len(df.index))
# # przygotowanie wektora z rozmiarami 'kropek'
# scale = np.abs(df['sepal length'] - df['sepal width'])
#
#
# plt.scatter(df['sepal length'], df['sepal width'], c=colors, s=scale)
# plt.xlabel('sepal length')
# plt.ylabel('sepal width')
# plt.show()

# xlsx = pd.ExcelFile('imiona.xlsx')
# df = pd.read_excel(xlsx, header=0)
# print(df)
#
# plt.subplot(1, 3, 1)
# grouped = df.groupby('Plec')
# etykiety = list(grouped.groups.keys())
# wartosci = list(grouped.agg('Liczba').sum())
# plt.bar(x=etykiety, height=wartosci, color=['green', 'red'])
# plt.xlabel('Płeć')
# plt.ylabel('Liczba narodzonych dzieci')
#
# plt.subplot(1, 3, 2)
# x = df['Rok'].unique()
# kobiety = df[(df.Plec == 'K')].groupby('Rok').agg({'Liczba':['sum']}).values
# mezczyzni = df[(df.Plec == 'M')].groupby('Rok').agg({'Liczba':['sum']}).values
# plt.plot(x, kobiety, label="Kobiety")
# plt.plot(x, mezczyzni, label="Mężczyźni")
# plt.xlabel('Rok')
#
# plt.subplot(1, 3, 3)
# x = df['Rok'].unique()
# y = df.groupby('Rok').agg('Liczba').sum()
# plt.bar(x, y)
# plt.xlabel('Rok')
# plt.subplots_adjust(wspace=0.85)
# plt.show()

# sns.set(rc={'figure.figsize': (8, 8)})
# sns.lineplot(x=[1, 2, 3, 4], y=[1, 4, 9, 16],
#              label='linia nr1', color='red', marker='o', linestyle=':')
# sns.lineplot(x=[1, 2, 3, 4], y=[2, 5, 10, 17],
#              label='linia nr2', color='green', marker='^',
# linestyle=':')
# plt.xlabel('oś x')
# plt.ylabel('oś y')
# plt.title('Wykres liniowy')
# plt.show()
#
# s = pd.Series(np.random.randn(1000))
# s = s.cumsum()
# sns.set()
# wykres = sns.relplot(kind='line', data=s, label='linia')
# wykres.fig.set_size_inches(8, 6)
# wykres.fig.suptitle('Wykres liniowy losowych danych')
# wykres.set_xlabels('indeksy')
# wykres.set_ylabels('wartości')
# wykres.add_legend()
# wykres.figure.subplots_adjust(left=0.1, right=0.9, bottom=0.1, top=0.9)
# plt.show()
#
# sns.set()
# df = pd.read_csv('iris.data', header=0, sep=',', decimal='.')
# print(df)
# wykres = sns.lineplot(data=df, x=df.index, y='sepal length', hue='class')
# wykres.set_xlabel('indeksy')
# wykres.set_title('Wykres liniowy danych z Iris dataset')
# wykres.legend(title='Rodzaj kwiatu')
# plt.show()

# sns.set()
# data = {'a': np.arange(10),'c': np.random.randint(0, 50, 10),'d': np.random.randn(10)}
# data['b'] = data['a'] + 10 * np.random.randn(10)
# data['d'] = np.abs(data['d']) * 100
# print(data['c'])
# print(data['d'])
# df = pd.DataFrame(data)
# plot = sns.relplot(data=df, x="a", y="b", hue="c", palette='bright', size="d", legend=True)
# plot.fig.set_size_inches(6, 6)
# plot.set(xticks=data['a'])
# plt.show()

data = {'Kraj': ['Belgia', 'Indie', 'Brazylia', 'Polska'],
        'Stolica': ['Bruksela', 'New Delhi', 'Brasilia', 'Warszawa'],
        'Kontynent': ['Europa', 'Azja', 'AmerykaPołudniowa', 'Europa'],
        'Populacja': [11190846, 1303171035, 207847528, 38675467]}
df = pd.DataFrame(data)
sns.set()
# plot = sns.catplot(data=df, x='Kontynent', y='Populacja',
# kind='bar', hue='Kontynent', estimator=np.sum,
#     dodge=False, palette=['red', 'green',
# 'yellow'], legend_out=False)
# plot.fig.set_size_inches(7, 6)
# plot.add_legend(title='Populacja na kontynentach', loc='upper right')
# plot.fig.suptitle('Populacja na kontynentach')
# plot = sns.barplot(data=df, x='Kontynent', y='Populacja', hue='Kontynent', estimator=np.sum,
#                    dodge=False, palette=['red', 'green', 'yellow'])
# plot.legend(title='Populacja na kontynentach')
plot = sns.barplot(data=df, x='Kontynent', y='Populacja', hue='Kontynent', estimator=np.sum,
                   dodge=False, palette=['red', 'green',
'yellow'])
plot.legend(title='Populacja na kontynentach')
plot.set(title='Wykres słupkowy')
plt.show()