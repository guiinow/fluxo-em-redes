import pandas as pd

class Network:
    def __init__(self, size_vertices=0, adjacent_matrix=None, cappacity=0, cost=0, demand=0):
        self.size_vertices = size_vertices
        self.adjacent_matrix = adjacent_matrix
        self.cappacity = cappacity
        self.cost = cost
        self.demand = demand

    def ler_arquivo(self, nome_arq):
        """Le arquivo de grafo no formato dimacs"""
        try:
            arq = open(nome_arq)
            # Leitura do cabecalho
            teste = pd.read_csv(arq, sep=';')
            # # Inicializacao das estruturas de dados
            professores = [(int(str[0]), int(str[1])) for i in range(int(str[0]))]
        except IOError:
            print("Nao foi possivel encontrar ou ler o arquivo!")

    
    def create_network(self, arq):
        # Le cada aresta do arquivo
            for i in (0, self.num_arestas):
                teste = pd.read_csv(arq, sep=';')
                teste = pd.read_csv(arq, sep=';')
                prof = int(str[0])  # Vertice prof
                disc = int(str[1])  # Vertice disciplinas
                p1 = int(str[2])  # Aresta preferencia 1
                p2 = int(str[3])  # Aresta preferencia 2
                p3 = int(str[4])  # Aresta preferencia 3
                p4 = int(str[5])  # Aresta preferencia 4
                p5 = int(str[6])  # Aresta preferencia 5
                self.add_aresta((prof, disc, p1, p2, p3, p4, p5))
       