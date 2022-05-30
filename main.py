import csv

arquivo = open('professores_toy.csv')

linhas = csv.reader(arquivo)

for linha in linhas:
    print(linha)
