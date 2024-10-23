import pickle

class SerializadorPickle:
    def __init__(self, objeto, nome_arquivo):
        self.objeto = objeto
        self.nome_arquivo = nome_arquivo

    def serializar(self):
        with open(self.nome_arquivo, 'wb') as arquivo:
            pickle.dump(self.objeto, arquivo)

meu_objeto = {'nome': 'Alice', 'idade': 30, 'cidade': 'São Paulo'}
serializador = SerializadorPickle(meu_objeto, 'meu_objeto.pickle')
serializador.serializar()
