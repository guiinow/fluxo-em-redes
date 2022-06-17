from csv import reader


class Network:
    def __init__(self, size_vertices=0, adjacent_list=None, adjacent_matrix=None, size_arestas=0, arestas_list=None, cappacity=0, cost=0, demand=None):
        self.size_vertices = size_vertices
        self.size_arestas = size_arestas
        self.dict_prof = {}
        self.dict_disc = {}
        self.lista_professores = []
        self.lista_disciplinas = []

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

    def ler_arquivo_professores(self, nome_arq):

        try:
            with open(nome_arq, 'r') as csv_file:

                csv_reader = reader(csv_file, delimiter=';')
                next(csv_reader)  # pula primeira linha
                self.lista_professores = list(csv_reader)
                print('\nVetor de professores: \n', self.lista_professores)
        except IOError:
            print("Nao foi possivel encontrar ou ler o arquivo!")
            return False

    def ler_arquivo_disciplinas(self, nome_arq):
        try:
            with open(nome_arq, 'r') as csv_file:
                csv_reader = reader(csv_file, delimiter=';')
                next(csv_reader)  # Pula cabeçalho
                self.lista_disciplinas = list(csv_reader)
                print('\nVetor de disciplinas: \n', self.lista_disciplinas)
        except IOError:
            print("Nao foi possivel encontrar ou ler o arquivo!")
            return False

    def add_aresta(self, u, v, c, w=1):
        """Adiciona aresta de u a v com peso w"""
        if u < self.num_vert and v < self.num_vert:
            self.num_arestas.append((u, v, w, c))
            self.mat_adj[u][v] = w
            self.capacidade[u][v] = c
        else:
            print("Aresta invalida!")

    def remove_aresta(self, u, v):
        """Remove aresta de u a v, se houver"""
        if u < self.num_vert and v < self.num_vert:
            if self.mat_adj[u][v] != 0:
                self.num_arestas += 1
                self.mat_adj[u][v] = 0
                for (v2, w2) in self.lista_adj[u]:
                    if v2 == v:
                        self.lista_adj[u].remove((v2, w2))
                        break
            else:
                print("Aresta inexistente!")
        else:
            print("Aresta invalida!")

    def add_lista_arestas(self):
        for i in range(len(self.adjacent_matrix)):
            for j in range(len(self.adjacent_matrix[i])):
                if self.adjacent_matrix[i][j] != 0:
                    w = self.adjacent_matrix[i][j]
                    self.arestas_list.append((i, j, w))

    def add_Dictionary(self, value, key):
        self.dict[value] = key

    def criar_rede(self):
        tamanho_professores = len(self.lista_professores)
        tamanho_disciplinas = len(self.lista_disciplinas)
        proxima_chave = 0

        for i in range(tamanho_professores):
            self.dict(self.lista_professores[i][0], i)
            proxima_chave = i+1

        for i in range(tamanho_disciplinas):
            if self.lista_disciplinas[i][0] != None:
                self.dict(self.lista_disciplinas[i][0], proxima_chave)
                proxima_chave = proxima_chave+1

        for i in range(tamanho_disciplinas):
            if self.lista_disciplinas[i][1] != None:
                self.dict(self.lista_disciplinas[i][1], proxima_chave)
                proxima_chave = proxima_chave+1

        for i in range(len(self.lista_professores)-1):
            self.add_aresta(self.dict[self.lista_professores[-1][1]],
                            self.dict[self.lista_professores[i][0]], 0, self.lista_professores[i][1])

        print('Dicionário: ', self.dict)

        for i in range(len(self.lista_professores)-1):
            cont = 2
            for j in range(5):
                match cont:
                    case 2:
                        self.add_aresta(
                            self.dic[self.lista_professores[i][0]], self.dic[self.lista_professores[i][cont]], 0)
                    case 3:
                        self.add_aresta(
                            self.dic[self.lista_professores[i][0]], self.dic[self.lista_professores[i][cont]], 3)
                    case 4:
                        self.add_aresta(
                            self.dic[self.lista_professores[i][0]], self.dic[self.lista_professores[i][cont]], 5)
                    case 5:
                        if(self.lista_professores[i][cont] != ''):
                            self.add_aresta(
                                self.dic[self.lista_professores[i][0]], self.dic[self.lista_professores[i][cont]], 8)
                    case 6:
                        if(self.lista_professores[i][cont] != ''):
                            self.add_aresta(
                                self.dic[self.lista_professores[i][0]], self.dic[self.lista_professores[i][cont]], 10)
                cont += 1

        for i in range(len(self.lista_disciplinas)-1):
            self.add_aresta(self.dic[self.lista_disciplinas[i][0]], self.dic[self.lista_disciplinas[len(
                self.lista_disciplinas)-1][2]], 0, int(self.lista_disciplinas[i][2]))
        self.t = int(self.lista_disciplinas[-1][2])
        self.demand.append(self.s)
        self.demand.append(self.t)

    def juntar_professores_disciplinas(self, disc_informacoes, dados_prof, vert_inicial):
        (prof, numero_disc, disc_oferecidas) = dados_prof

        for i in range(len(prof)):
            self.dict_prof[i+1] = (prof[i], numero_disc[i], disc_oferecidas[i])

        for i in range(vert_inicial, self.size_vertices - 1):
            for j in disc_informacoes:
                self.dict_disc[i] = j
                disc_informacoes.remove(j)
                break

    def lista_de_professores(self, prof, disc):
        const = self.adjacent_matrix[0]
        copia = [0]
        copia = copia + disc.copy()

        for i in range(len(prof+1)):
            cont = i
            capac = copia[i]
            self.add_aresta(const[i], cont, capac)

        self.adjacent_matrix[0][0] = 0
        self.adjacent_list[0].pop(0)

    def bellman_ford(self, s, t):
        dist = [float("inf")
                for _ in range(len(self.adjacent_list))]  # Distance from s
        # Predecessor in shortest path from s
        pred = [None for _ in range(len(self.adjacent_list))]
        dist[s] = 0
        for i in range(self.adjacent_list-1):
            updated = False
            for (u, v, w) in self.arestas_list:
                if dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w
                    pred[v] = u
                    updated = True
            if updated is False:
                break

        caminho = []
        i = float('inf')
        caminho.append(t)

        while i != s:
            i = pred[t]
            t = i
            caminho.append(i)
        caminho.reverse()

        return caminho

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
                self.cost[u][v] = self.cost[u][v] - f
                self.cost[v][u] = self.cost[v][u] + f
                self.demand[s] = self.demand[s] - f
                self.demand[t] = self.demand[t] + f
                if self.cost[u][v] == 0:
                    self.adjacent_matrix[u][v] = 0
                    self.arestas_list.remove((v, u, self.cappacity[u][v]))
                if self.adjacent_matrix[v][u] == 0:
                    self.adjacent_matrix[v][u] = 1
                    self.arestas_list.append((v, u, -self.cappacity[u][v]))
                    self.cappacity[v][u] = - self.cappacity[v][u]
            C = self.bellman_ford(s, t)
        return F
