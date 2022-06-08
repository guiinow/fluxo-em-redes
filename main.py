# import csv

# arquivo = open('professores_toy.csv')

# linhas = csv.reader(arquivo)

# for linha in linhas:
#     print(linha)

import grafo

g1 = grafo.Grafo()

g1.ler_arquivo_professor('./datasets/professores_toy.csv')
