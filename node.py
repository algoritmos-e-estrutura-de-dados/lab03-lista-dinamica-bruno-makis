class Node:
    valor = 0
    anterior = None
    proximo = None #none é equivalente ao null

    def __init__(self, valor=0, anterior=None, proximo=None):
        self.valor = valor
        self.anterior = anterior
        self.proximo = proximo 
        
