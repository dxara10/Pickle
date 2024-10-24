import pickle

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __repr__(self):
        return f'Pessoa(nome={self.nome}, idade={self.idade})'

# Serialização
pessoa = Pessoa('João', 25)
with open('pessoa.pickle', 'wb') as arquivo:
    pickle.dump(pessoa, arquivo)

# Desserialização
with open('pessoa.pickle', 'rb') as arquivo:
    pessoa_desserializada = pickle.load(arquivo)

print("Pessoa desserializada:", pessoa_desserializada)
