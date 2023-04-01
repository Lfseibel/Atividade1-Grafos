import numpy as np

# Cria Matriz de Adjacência: Função para leitura de um dataset em forma de matriz de adjacências.
# Entrada: instancia (nome do arquivo .txt do dataset em forma de matriz de adjacência
# Saída: matriz de adjacência (tipo NumPy.ndarray)
def startHeadquarters(instance):
    print('Instance name:', instance, '\n')
    path = 'c:/Users/lfsei/Documents/Atv1grafo/Instances/' + instance + '.txt'
    with open(path, 'rb') as f:
        data = np.genfromtxt(f, dtype="int64") #OBS. Lê arquivo .txt de uma Instancia no formato Matriz de Adjacência
    return data

# Salva Resultado: Função para salvar em arquivo .txt o resultado da execução do programa.
# Entrada: resultado (tipo lista)
# Saída: arquivo .txt no diretório especificado'''
def saveResults(result, instance):
    stringRes = ''
    stringRes += 'nome_instancia' + ':' + str(instance) + '  '
    for key in result: #percorre o dicionario e armazena na string a ser salva
        # access the value corresponding to the current key
        value = result[key]
        stringRes += str(key) + ':' + str(value) + '  '
    stringRes += '\n'
    arq = open('c:/Users/lfsei/Documents/Atv1grafo/Results/resultado.txt', 'a+')
    arq.writelines(stringRes + '\n')
    arq.close()