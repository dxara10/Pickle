import pickle

# Dados de exemplo
dados = {'nome': 'Maria', 'idade': 30}
lista = [1, 2, 3, 4, 5]

# Serialização de múltiplos objetos
with open('multiplos_objetos.pickle', 'wb') as arquivo:
    pickle.dump(dados, arquivo)
    pickle.dump(lista, arquivo)

# Desserialização de múltiplos objetos
with open('multiplos_objetos.pickle', 'rb') as arquivo:
    dados_desserializados = pickle.load(arquivo)
    lista_desserializada = pickle.load(arquivo)

print("Dados desserializados:", dados_desserializados)
print("Lista desserializada:", lista_desserializada)
