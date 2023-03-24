import numpy as np

def getTraits(headquarters):
    traits = {}
    traits['qtd_linhas'] = headquarters.shape[0];
    traits['qtd_colunas'] = headquarters.shape[1];
    return traits