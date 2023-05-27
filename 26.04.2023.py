import numpy as np
import pandas as pd

# df = pd.read_csv('australian.txt', header=None, sep=' ', decimal=' ')
# print(df)

xlsx = pd.ExcelFile('imiona.xlsx')
data = pd.read_excel(xlsx, header=0)
df = pd.DataFrame(data)
#
# a = int(input("Enter: "))
# print(df[(df.Liczba > 1000) & (df.Rok == a)])
#
# b = str(input("Enter: "))
# print(df[df.Imie == b])
#
# print(" ")
# print(" ")
# print(" ")
# print(" ")
#
# c = int(input("Enter: "))
# df2 = df[df.Rok == c]
# print(df2.sum()['Liczba'])
#
# print(" ")
# print(" ")
# print(" ")
# print(" ")
#
# df3 = df[(df.Rok >= 2000) & (df.Rok <= 2005)]
# print(df3.sum()['Liczba'])
#
# print(" ")
# print(" ")
# print(" ")
# print(" ")
#
# print(df[df.Plec == 'M'].sum()['Liczba'])
# print(" ")
# print(df[df.Plec == 'K'].sum()['Liczba'])
#
# print(" ")
# print(" ")
# print(" ")
# print(" ")

# d = int(input("Enter: "))
# print(df[(df.Plec == 'M') & (df.Rok == d)].max()['Liczba'])
# print(df[(df.Plec == 'K') & (df.Rok == d)].max()['Liczba'])

# print(" ")
# print(" ")
# print(" ")
# print(" ")

print(df[df.Plec == 'M'].groupby(['Imie']).agg({'Liczba':['sum']}))
print(df[df.Plec == 'K'].groupby(['Imie']).agg({'Liczba':['sum']}))

