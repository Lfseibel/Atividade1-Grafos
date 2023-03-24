import sys
from Initialization import (dataSet as ds)
from Methods import (traits as trait)

# Program core
def main(instance):
    headquarters = ds.startHeadquarters(instance)
    print(headquarters, '\n') # '\n' insert blank space after code line
    
    traits = trait.getTraits(headquarters); #funcao responsavel por pegar as caracteristicas da matriz
    
    
    ds.saveResults(traits, instance); #funcao responsavel por salvar as caracteristicas da matriz e da instancia

# Chamada a função main() Argumento Entrada: [1] dataset
if __name__ == '__main__':
    main(str(sys.argv[1]))

#python -u "c:\Users\lfsei\Downloads\Grafos\Atividade1\Meu\main.py" exemplo