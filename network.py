from csv import reader


class Network:
    def __init__(self, size_vertices=0, adjacent_list=None, adjacent_matrix=None, size_arestas=0, arestas_list=None, cappacity=0, cost=0, demand=None):
        self.size_vertices = size_vertices
        self.size_arestas = size_arestas
        self.dict_prof = {}
        self.dict_disc = {}
        self.lista_professores = []
        self.lista_disciplinas = []
        self.dicionario = {}

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
                self.criar_rede()
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
                self.criar_rede()
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
        self.dicionario[value] = key

    def criar_rede(self):
        tamanho_professores = len(self.lista_professores)
        tamanho_disciplinas = len(self.lista_disciplinas)
        proxima_chave = 0

        for i in range(tamanho_professores):
            self.add_Dictionary(self.lista_professores[i][0], i)
            proxima_chave = i+1

        for i in range(tamanho_disciplinas):
            if self.lista_disciplinas[i][0] != None:
                self.add_Dictionary(self.lista_disciplinas[i][0], i)
                proxima_chave = proxima_chave+1

        for i in range(tamanho_disciplinas):
            if self.lista_disciplinas[i][0] != None:
                self.add_Dictionary(self.lista_disciplinas[i][0], proxima_chave)
                proxima_chave = proxima_chave+1

        for i in range(tamanho_disciplinas):
            if self.lista_disciplinas[i][1]!=None:
                self.add_Dictionary(self.lista_disciplinas[i][1], proxima_chave)
                proxima_chave = proxima_chave + 1

        print('Dicionário: ', self.dicionario)

    def juntar_professores_disciplinas(self, disc_informacoes, dados_prof, vert_inicial):
        (prof, numero_disc, disc_oferecidas) = dados_prof

        for i in range(len(prof)):
            self.dict_prof[i+1] = (prof[i], numero_disc[i], disc_oferecidas[i])

        for i in range(vert_inicial, self.size_vertices - 1):
            for j in disc_informacoes:
                self.dict_disc[i] = j
                disc_informacoes.remove(j)
                break

    def SetSuperOferta(self, prof, disc):
        const = self.adjacent_matrix[0]
        copia = [0]
        copia = copia + disc.copy()

        for i in range(len(prof+1)):
            cont = i
            capac = copia[i]
            self.add_aresta(const[i], cont, capac)

        self.adjacent_matrix[0][0] = 0
        self.adjacent_list[0].pop(0)

    def setSuperDemanda(self, vert_inicial, info_disciplinas):
        capac_disc = [i[2] for i in info_disciplinas]
        sdemanda = self.size_vertices - 1
        capac = None

        for i in range(vert_inicial, self.size_vertices - 1):
            const = i
            for _ in capac_disc:
                capac = i
                capac_disc.remove(i)
                break
            self.addEdge(const, sdemanda, capac)

    def setProfparaDisc(self):
        for i in range(len(self.lista_professores)-1):
            cont = 0
            for _ in range(5):
                match cont:
                    case 0:
                        self.add_aresta(
                            self.dict_prof[self.lista_professores[i][0]], self.dict_prof[self.lista_professores[i][cont+2]], 0)
                    case 1:
                        self.add_aresta(
                            self.dict_prof[self.lista_professores[i][0]], self.dict_prof[self.lista_professores[i][cont+2]], 3)
                    case 2:
                        self.add_aresta(
                            self.dict_prof[self.lista_professores[i][0]], self.dict_prof[self.lista_professores[i][cont+2]], 5)
                    case 3:
                        if(self.lista_professores[i][cont+2] != ''):
                            self.add_aresta(
                                self.dict_prof[self.lista_professores[i][0]], self.dict_prof[self.lista_professores[i][cont+2]], 8)
                    case 4:
                        if(self.lista_professores[i][cont+2] != ''):
                            self.add_aresta(
                                self.dict_prof[self.lista_professores[i][0]], self.dict_prof[self.lista_professores[i][cont+2]], 10)
                cont += 1

    def setDadosIniciais(self, info_prof, info_disc):
        
        (prof, disc_ofertadas) = info_prof
        total_disc = info_disc

        self.size_vertices = 2 + len(prof) + total_disc

        self.adjacent_matrix = [[0 for _ in range(self.size_vertices)]
                        for _ in range(self.size_vertices)]
        self.adjacent_list = [[] for _ in range(self.size_vertices)]

        self.SetSuperOferta(prof, disc_ofertadas)

        self.setSuperDemanda(len(prof) + 1, info_disc) 

        self.juntar_professores_disciplinas(len(prof) + 1, info_disc, info_prof)

        self.setProfparaDisc()

        self.add_lista_arestas()

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
            if updated is False:  #interrompe a execução caso não haja mais caminho
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

    def formatData(self, matrix: list):
            prof = self.dict_prof.keys()
            disc = self.dict_disc.keys()
            edges = []
            costs = [0, 3, 5, 8, 10]  # Based on preferences table
            total_cost = 0
            total_classes = 0

            for i in range(0, len(matrix)):
                for j in range(0, len(matrix[i])):
                    if matrix[i][j] != 0:  # If the edge has flow
                        if i in prof or j in disc:
                            # Append edge in edges
                            edges.append((i, j, matrix[i][j]))

            print("\n")
            print("{:<20} {:<20} {:<40} {:<40} {:<40}".format(
                'Teacher', 'Subject', 'Name', 'Classes', 'Cost'))
            for teacher, subject, classes in edges:

                subject_id = self.dict_disc[subject][0]
                teacher_subjects = self.dict_prof[teacher][2]
                subject_cost = teacher_subjects.index(subject_id)

                print("{:<20} {:<20} {:<40} {:<40} {:<40}"
                    .format(self.dict_prof[teacher][0],  # Teacher name
                            subject_id,  # Subject id
                            self.dict_disc[subject][1],  # Subject name
                            classes,  # Classes
                            costs[subject_cost] * classes))  # Cost of allocation

                total_cost += costs[subject_cost] * \
                    classes  # Total cost of all allocations
                total_classes += classes  # Total classes allocated

            print(f"\nThe total cost was {total_cost}")
            print(f"Total classes allocated: {total_classes}")

            if len(self.lista_professores) != 0:
                print(f"\nThis teachers dont offer any subject:")
                print(*self.lista_professores, sep=", ")
            else:
                print("\nAll teachers offer at least one subject")

    def executa(self, teachers_file, subjects_file):

        self.setDadosIniciais(self.ler_arquivo_professores(teachers_file),
                            self.ler_arquivo_disciplinas(subjects_file))
        self.formatData(self.SucessivosCaminhosMinimos(0, self.size_vertices - 1))