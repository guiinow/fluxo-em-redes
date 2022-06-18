import network

network = network.Network()

network.ler_arquivo_professores('./datasets/professores.csv')
network.ler_arquivo_disciplinas('./datasets/disciplinas.csv')
# print(network.ler_arquivo_professores('./datasets/professores_toy.csv'))

# prof = input("digite o nome do arquivo prof: ")
# disc = input("digite o nome do arquivo disc: ")

# network.executa('professores_toy.csv', 'disciplinas_toy.csv')

