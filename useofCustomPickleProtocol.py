import pickle

class ObjetoPickleCustomizado:
    def __init__(self, dados):
        self.dados = dados

    def __getstate__(self):
        return self.dados

    def __setstate__(self, estado):
        self.__init__(estado)

objeto_original = ObjetoPickleCustomizado({'nome': 'Ana', 'idade': 35})

# Serialização
with open('objeto_custom.pickle', 'wb') as arquivo:
    pickle.dump(objeto_original, arquivo)

# Desserialização
with open('objeto_custom.pickle', 'rb') as arquivo:
    objeto_desserializado = pickle.load(arquivo)

print("Objeto desserializado:", objeto_desserializado)
