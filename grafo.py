class Grafo:
    def __init__(self, num_vert=0, num_arestas=0, lista_adj=None, mat_adj=None, lista_arestas=None, lista_sem_peso=None):
        self.num_vert = num_vert
        self.num_arestas = num_arestas
        if lista_adj is None:
            self.lista_adj = [[] for i in range(num_vert)]
        else:
            self.lista_adj = lista_adj
        if mat_adj is None:
            self.mat_adj = [[0 for j in range(num_vert)]
                            for i in range(num_vert)]
        else:
            self.mat_adj = mat_adj
        if lista_arestas is None:
            self.lista_arestas = [[] for i in range(num_vert)]
            # receber somente []
        else:
            self.lista_arestas = lista_arestas
        # if lista_sem_peso is None:
        #     self.lista_sem_peso = [[] for i in range(num_vert)]
        # else:
        #     self.lista_sem_peso = lista_arestas

    def add_aresta(self, u, v, w=1):
        """Adiciona aresta de u a v com peso w"""
        self.num_arestas += 1
        if u < self.num_vert and v < self.num_vert:
            self.lista_adj[u].append((v, w))
            self.mat_adj[u][v] = w
        else:
            print("Aresta invalida!")

    def ler_arquivo(self, nome_arq):
        """Le arquivo de grafo no formato dimacs"""
        try:
            arq = open(nome_arq)
            # Leitura do cabecalho
            str = arq.readline()
            str = str.split(" ")
            self.num_vert = int(str[0])
            cont_arestas = int(str[1])
            # Inicializacao das estruturas de dados
            self.lista_adj = [[] for i in range(self.num_vert)]
            self.mat_adj = [[0 for j in range(self.num_vert)]
                            for i in range(self.num_vert)]
            # Le cada aresta do arquivo
            for i in range(0, cont_arestas):
                str = arq.readline()
                str = str.split(" ")
                u = int(str[0])  # Vertice origem
                v = int(str[1])  # Vertice destino
                w = int(str[2])  # Peso da aresta
                self.add_aresta(u, v, w)
                self.lista_arestas.append((u, v, w))
                selecao = 0
                if w != 1:
                    if w < 0:
                        selecao = 3
                    else:
                        selecao = 2
                else:
                    selecao = 1
            return selecao
        except IOError:
            print("Nao foi possivel encontrar ou ler o arquivo!")