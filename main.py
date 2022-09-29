from lista import Lista

lista = Lista()

lista.adicionar(1)#atribui
lista.adicionar(2, inicio=True)
lista.adicionar(3)
lista.adicionar(4)
lista.adicionar(5)
lista.adicionar(6, inicio=True)

lista.show() #mostra

lista.remover(3)#remove
lista.remover(5)#remove
lista.remover(6)#remove

lista.show()