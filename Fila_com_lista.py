class Fila(object):
    def __init__(self):
        self.dados = []

    def inserir_dados(self,elemento):
        self.dados.append(elemento) 
    
    def remover_da_fila(self):
        return self.dados.pop(0)
    
    def mostrar_fila(self):
        return print(self.dados)

    def fila_vazia(self):
        if len(self.dados) == 0:
            return print(True)
        else:
            return print(False)
f = Fila()
f.fila_vazia()
f.inserir_dados(10)
f.inserir_dados(20)
f.mostrar_fila()
f.remover_da_fila()
f.mostrar_fila()
        