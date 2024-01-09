import pandas as pd

dados = [['Jose', 29, 'Manaus', 'M'], ['Natalia', 27, 'Passos', 'F'], ['Zeze', 40, 'Sao Paulo', 'M'],
         ['Alex', 38, 'Rio de Janeiro', 'M'],['Bruna', 21, 'Guarulhos', 'F']]
#dados = [dados,['Geise', 34, 'Recife', 'F']]
#dados = pd.concat([dados,['Adriana',50,'Manaus','F']], axis = 0)

dados.append(['Geise', 34, 'Recife', 'F'])

print(dados)

colunas = ['Nome', 'Idade', 'Cidade', 'Sexo']

indice = range(0,6)

df = pd.DataFrame(data = dados, columns = colunas, index = indice)

df = df.append(pd.Series(['Adriana',50,'Manaus','F'],index=df.columns), ignore_index=True)

print(df)

df.to_csv('lista_de_dados.csv')