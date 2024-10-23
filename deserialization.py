import pickle

class DesserializadorPickle:
    def __init__(self, nome_arquivo):
        self.nome_arquivo = nome_arquivo

    def desserializar(self):
        with open(self.nome_arquivo, 'rb') as arquivo:
            return pickle.load(arquivo)

objeto = DesserializadorPickle('meu_objeto.pickle').desserializar()
print("Objeto desserializado:", objeto)
