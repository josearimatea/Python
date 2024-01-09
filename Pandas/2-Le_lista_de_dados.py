import pandas as pd

lista = pd.read_csv('lista_de_dados.csv', index_col=0)

print(lista)

print(lista.describe())