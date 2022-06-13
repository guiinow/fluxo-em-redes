class Grafo:
    def __init__(self, num_vert=0, num_arestas=0, lista_adj=None, mat_adj=None, lista_arestas=None):
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
        else:
            self.lista_arestas = lista_arestas

    def ler_arquivo_professor(self, nome_arq):
        """Le arquivo de grafo no formato dimacs"""
        try:
            arq = open(nome_arq)
            # Leitura do cabecalho
            str = csv.reader(arq)
            str = str.split(";")
            self.num_vert = 3
            cont_arestas = 5
            # # Inicializacao das estruturas de dados
            self.lista_adj = [[] for i in range(self.num_vert)]
            self.mat_adj = [[0 for j in range(self.num_vert)]
                            for i in range(self.num_vert)]
            # Le cada aresta do arquivo
            for i in (0, cont_arestas):
                str = csv.reader(arq)
                str = str.split(";")
                prof = int(str[0])  # Vertice prof
                disc = int(str[1])  # Vertice disc
                p1 = int(str[2])  # Aresta preferencia 1
                p2 = int(str[3])  # Aresta preferencia 2
                p3 = int(str[4])  # Aresta preferencia 3
                p4 = int(str[5])  # Aresta preferencia 4
                p5 = int(str[6])  # Aresta preferencia 5
                self.add_aresta(prof, disc, p1, p2, p3, p4, p5)
        except IOError:
            print("Nao foi possivel encontrar ou ler o arquivo!")
