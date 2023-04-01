import numpy as np

def getTraits(headquarters):
    traits = {}
    traits['qtd_linhas'] = headquarters.shape[0];
    traits['qtd_colunas'] = headquarters.shape[1];
    return traits

def checkAdjacency(headquarters, vL, vC):
    if(headquarters[vL][vC]):
        test = True;
    else:
        test = False;
    print(test);



#for vL in range(0, qtdVertice)
#for vC in range(vL + 1, qtdVertice)

#remover vertice troca pra -1