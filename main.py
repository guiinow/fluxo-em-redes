import network

network = network.Network()

network.chamarFuncao(network.ler_arquivo_professores('./datasets/professores.csv'),
                     network.ler_arquivo_disciplinas('./datasets/disciplinas.csv'))

network.imprime(network.SucessivosCaminhosMinimos(
    0, network.size_vertices - 1))
