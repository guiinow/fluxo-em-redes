from csv import reader


class Network:
    def __init__(self, size_vertices=0, adjacent_list=None, adjacent_matrix=None, size_arestas=0):
        self.size_vertices = size_vertices
        self.size_arestas = size_arestas
        self.dict_prof = {}
        self.dict_disc = {}
        self.lista_professores = []
        self.lista_disciplinas = []
        self.professores = []
        self.disciplinas = []
        self.arestas_list = []

        if adjacent_list == None:
            self.adjacent_list = [[] for i in range(size_vertices)]
        else:
            self.adjacent_list = adjacent_list

        if adjacent_matrix == None:
            self.adjacent_matrix = [
                [0 for i in range(size_vertices)] for j in range(size_vertices)]
        else:
            self.adjacent_matrix = adjacent_matrix

    def ler_arquivo_professores(self, nome_arq):

        try:
            with open(nome_arq, 'r') as csv_file:

                csv_reader = reader(csv_file, delimiter=';')
                next(csv_reader)  # pula primeira linha
                self.lista_professores = list(csv_reader)
        except IOError:
            print("Nao foi possivel encontrar ou ler o arquivo!")
            return False
        tamanho_vet = len(self.lista_professores)
        vet_nome = []
        vet_disc = []
        vet_pref = [[] for i in range(tamanho_vet)]
        for i in range(tamanho_vet-1):
            vet_nome.append(self.lista_professores[i][0])
            vet_disc.append(self.lista_professores[i][1])
            for j in range(2, len(self.lista_professores[i])-1):
                if(self.lista_professores[i][j] != ''):
                    vet_pref[i].append(self.lista_professores[i][j])
        return vet_nome, vet_disc, vet_pref

    def ler_arquivo_disciplinas(self, nome_arq):
        try:
            with open(nome_arq, 'r') as csv_file:
                csv_reader = reader(csv_file, delimiter=';')
                next(csv_reader)  # Pula cabeçalho
                self.lista_disciplinas = list(csv_reader)
        except IOError:
            print("Nao foi possivel encontrar ou ler o arquivo!")
            return False
        num_diciplinas = len(self.lista_disciplinas)
        soma_materia = 0
        for i in range(len(self.lista_disciplinas)-1):
            soma_materia = soma_materia + int(self.lista_disciplinas[i][2])

        self.disciplinas = soma_materia
        return self.lista_disciplinas, soma_materia, num_diciplinas-1

    def add_aresta(self, u, v, c=float('inf'), w=0):
        """Adiciona aresta de u a v com peso w"""
        if u < self.size_vertices and v < self.size_vertices:
            self.adjacent_matrix[u][v] = [int(w), int(c)]
            self.adjacent_list[u].append((v, [w, c]))
            self.size_arestas = self.size_arestas + 1
        else:
            print("Aresta invalida!")

    def remove_aresta(self, u, v):
        """Remove aresta de u a v, se houver"""
        if u < self.size_vertices and v < self.size_vertices:
            if self.adjacent_matrix[u][v] != 0:
                self.adjacent_matrix[u][v] = 0
                for (v2, w2) in self.adjacent_list[u]:
                    if v2 == v:
                        self.adjacent_list[u].remove((v2, w2))
                        break
                self.size_arestas = self.size_arestas - 1
            else:
                print("Aresta inexistente!")
        else:
            print("Aresta invalida!")

    def add_lista_arestas(self):
        for i in range(len(self.adjacent_matrix)):
            for j in range(len(self.adjacent_matrix[i])):
                if self.adjacent_matrix[i][j] != 0:
                    [w, c] = self.adjacent_matrix[i][j]
                    self.arestas_list.append((i, j, w))

    def add_cappacity_cost_demanda(self):
        capacity = [[0 for i in range(len(self.adjacent_matrix))]
                    for j in range(len(self.adjacent_matrix))]
        cost = [
            [0 for i in range(len(self.adjacent_matrix))] for j in range(len(self.adjacent_matrix))]

        for i in range(len(self.adjacent_matrix)):
            for j in range(len(self.adjacent_matrix[i])):
                if self.adjacent_matrix[i][j] != 0:
                    [w, c] = self.adjacent_matrix[i][j]
                    capacity[i][j] = int(w)
                    cost[i][j] = int(c)
        demanda = [self.disciplinas]
        for i, [vet_nome, vet_disc, [*vet_pref]] in self.dict_prof.items():
            demanda.append(int(vet_disc))
        for i, [lista_disciplinas, soma_materia, num_diciplinas] in self.dict_disc.items():
            demanda.append(int(num_diciplinas))
        demanda.append(-(self.disciplinas))
        return capacity, cost, demanda

    def juntar_professores_disciplinas(self, disc_informacoes, vert_inicial, dados_prof):
        (vet_nome, vet_disc, vet_pref) = dados_prof

        for i in range(len(vet_nome)):
            self.dict_prof[i+1] = (vet_nome[i], vet_disc[i], vet_pref[i])

        for i in range(disc_informacoes, self.size_vertices - 1):
            for j in vert_inicial:
                self.dict_disc[i] = j
                vert_inicial.remove(j)
                break

    def SetSuperOferta_SuperDemanda(self, prof, disc, num_vert, lista_disciplinas):
        const = self.adjacent_matrix[0]
        copia = [0]
        copia = copia + disc.copy()

        for i in range(len(prof)+1):
            cont = i
            capac = copia[i]
            self.add_aresta(const[i], cont, capac)

        self.adjacent_matrix[0][0] = 0
        self.adjacent_list[0].pop(0)

        capac_disc = [i[2] for i in lista_disciplinas]
        sdemanda = self.size_vertices - 1
        capac = None

        for i in range(num_vert, self.size_vertices - 1):
            const = i
            for j in capac_disc:
                capac = j
                capac_disc.remove(j)
                break
            self.add_aresta(const, sdemanda, capac)

    def setProfparaDisc(self):
        prof = self.dict_prof
        disc = self.dict_disc

        w = [0, 3, 5, 8, 10]

        for i, (vet_nome, vet_disc, [*vet_pref]) in prof.items():
            oferecidas = 0
            for j, (listaDiciplinas, turma, num_disciplinas) in disc.items():
                if oferecidas == len(vet_pref):
                    break
                if vet_disc == 0:
                    self.professores.append(vet_nome)
                    break
                if listaDiciplinas in vet_pref:
                    self.add_aresta(i, j, num_disciplinas,
                                    w[vet_pref.index(listaDiciplinas)])
                    oferecidas = oferecidas + 1

    def chamarFuncao(self, info_prof, info_disc):

        # self.demand.append(int(self.lista_professores[-1][1]))
        # self.demand.append(-int(self.lista_disciplinas[-1][2]))

        (vet_nome, vet_disc, vet_pref) = info_prof
        (lista_disciplinas, soma_materia, num_diciplinas) = info_disc

        self.size_vertices = 2 + len(vet_nome) + num_diciplinas

        self.adjacent_matrix = [[0 for i in range(self.size_vertices)]
                                for i in range(self.size_vertices)]
        self.adjacent_list = [[] for i in range(self.size_vertices)]

        self.SetSuperOferta_SuperDemanda(
            vet_nome, vet_disc, len(vet_nome) + 1, lista_disciplinas)

        self.juntar_professores_disciplinas(
            len(vet_nome) + 1, lista_disciplinas, info_prof)

        self.setProfparaDisc()

        self.add_lista_arestas()

    def bellman_ford(self, s, t):
        dist = [float("inf")
                for _ in range(len(self.adjacent_list))]  # Distance from s
        # Predecessor in shortest path from s
        pred = [None for _ in range(len(self.adjacent_list))]
        dist[s] = 0
        for i in range(len(self.adjacent_list)-1):
            updated = False
            for (u, v, w) in self.arestas_list:
                if dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w
                    pred[v] = u
                    updated = True
            if updated is False:  # interrompe a execução caso não haja mais caminho
                break

        caminho = [t]
        i = pred[t]
        while i in pred:
            if i is None:
                break
            caminho.append(i)
            i = pred[i]
        caminho.reverse()

        return caminho

    def SucessivosCaminhosMinimos(self, s, t):
        F = [[0 for i in range(self.size_vertices)]
             for i in range(self.size_vertices)]
        C = self.bellman_ford(s, t)

        capacity, cost, demanda = self.add_cappacity_cost_demanda()

        while len(C) != 0 and demanda[s] != 0:
            f = float('inf')
            for i in range(1, len(C)):
                u = C[i-1]
                v = C[i]
                if cost[u][v] < f:
                    f = cost[u][v]
            for i in range(1, len(C)):
                u = C[i-1]
                v = C[i]
                F[u][v] += f
                cost[u][v] -= f
                if cost[u][v] == 0:
                    self.adjacent_matrix[u][v] = 0
                    self.arestas_list.remove((u, v, capacity[u][v]))
                if self.adjacent_matrix[v][u] == 0:
                    self.adjacent_matrix[v][u] = 1
                    self.arestas_list.append((v, u, -capacity[u][v]))
                    capacity[v][u] = -capacity[u][v]
                cost[v][u] += f
                if F[v][u] != 0:
                    F[v][u] -= f
            demanda[s] -= f
            demanda[t] += f
            C = self.bellman_ford(s, t)
        return F

    def imprime(self, caminhoMinimo):
        prof = self.dict_prof.keys()
        disc = self.dict_disc.keys()
        arestas = []
        custo = [0, 3, 5, 8, 10]
        custoTotal = 0
        disciplinasTotal = 0

        for i in range(len(caminhoMinimo)):
            for j in range(len(caminhoMinimo[i])):
                if caminhoMinimo[i][j] != 0:
                    if i in prof or j in disc:
                        arestas.append((i, j, caminhoMinimo[i][j]))

        print("\n")
        print('Prof\t\t\t\t\tDisc\t\t\t\t\tNome\t\t\t\t\tTurmas\t\t\t\t\tCusto')

        for prof, disc, turmas in arestas:

            disc_ = self.dict_disc[disc][0]
            prof_disc = self.dict_prof[prof][2]
            custoDisc = prof_disc.index(disc_)

            print(self.dict_prof[prof][0], '\t\t\t\t\t',
                  disc_, '\t\t\t\t\t',
                  self.dict_disc[disc][1], '\t\t\t\t\t',
                  turmas, '\t\t\t\t\t',
                  custo[custoDisc] * turmas)

            custoTotal += custo[custoDisc] * turmas
            disciplinasTotal += turmas

        print(f"\nCusto Total {custoTotal}")
        print(f"Total Disciplinas Alocadas: {disciplinasTotal}")

        if len(self.lista_professores) != 0:
            print(f"\nNao receberam disciplinas")
        else:
            print("\nTodos receberam disciplinas")
