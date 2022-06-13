from cmath import cos
import pandas as pd


class Network:
    def __init__(self, size_vertices=0, adjacent_list=None, adjacent_matrix=None, arestas_list=None, cappacity=0, cost=0, demand=None):
        self.size_vertices = size_vertices

        if adjacent_list == None:
            self.adjacent_list = [[] for i in range(size_vertices)]
        else:
            self.adjacent_list = adjacent_list

        if adjacent_matrix == None:
            self.adjacent_matrix = [
                [0 for i in range(size_vertices)] for j in range(size_vertices)]
        else:
            self.adjacent_matrix = adjacent_matrix

        if arestas_list == None:
            self.arestas_list = []
        else:
            self.arestas_list = arestas_list

        if cappacity == 0:
            self.cappacity = [
                [0 for i in range(size_vertices)] for j in range(size_vertices)]
        else:
            self.cappacity = cappacity

        if cost == 0:
            self.cost = [
                [0 for i in range(size_vertices)] for j in range(size_vertices)]
        else:
            self.cost = cost

        if demand == None:
            self.demand = [[] for i in range(size_vertices)]
        else:
            self.demand = demand

    def ler_arquivo(self, nome_arq):
        """Le arquivo de grafo no formato dimacs"""
        try:
            arq = open(nome_arq)
            # Leitura do cabecalho
            teste = pd.read_csv(arq, sep=';')
            # # Inicializacao das estruturas de dados
            professores = [(int(str[0]), int(str[1]))
                           for i in range(int(str[0]))]
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

    def bellman_ford(self, s, t):
        dist = [float("inf")
                for _ in range(self.size_vertices)]  # Distance from s
        # Predecessor in shortest path from s
        pred = [None for _ in range(self.size_vertices)]
        dist[s] = 0
        for i in range(self.size_vertices):
            updated = False
            for (u, v, w) in self.arestas_list:
                if dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w
                    pred[v] = u
                    updated = True
            if not updated:
                return dist, pred
        return dist, pred

    def SucessivosCaminhosMinimos(self, s, t):
        F = [[0 for i in range(len(self.size_vertices))]
             for i in range(len(self.size_vertices))]
        C = self.bellman_ford(s, t)
        while len(C) != 0 and self.demand[s] != 0:
            f = float('inf')
            for i in range(1, len(C)):
                u = C[i-1]
                v = C[i]
                if self.cost[u][v] < f:
                    f = self.cost[u][v]
            for i in range(1, len(C)):
                u = C[i-1]
                v = C[i]
                F[u][v] += f
                self.cost[u][v] -= f
                self.cost[v][u] += f
                self.demand[s] -= f
                self.demand[t] += f
                if self.cost[u][v] == 0:
                    self.adjacent_matrix[u][v] = 0
                    self.arestas_list.remove((v, u, self.cappacity[u][v]))
                if self.adjacent_matrix[v][u] == 0:
                    self.adjacent_matrix[v][u] = 1
                    self.arestas_list.append((v, u, -self.cappacity[u][v]))
                    self.cappacity[v][u] = - self.cappacity[v][u]
            C = self.bellman_ford(s, t)
        return F
