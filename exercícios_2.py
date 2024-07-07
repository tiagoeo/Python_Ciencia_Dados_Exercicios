# Listas
ls = "Octonautas"
lista = list(ls)
print("Lista = ", lista)
lista.sort()
print("Lista sort() = ", lista)
lista.reverse()
print("Lista reverse() = ", lista)

# Gerando Intervalos
print(range(10))
print(list(range(0, 10)))
print(list(range(0,10,2)))
print(list(range(20,0,-2)))

# Dicionários
pessoa1 = dict(nome='Victor', idade=17)
pessoa2 = dict([['nome', 'Ana'],['idade', 26]])
pessoa3 = {'nome' : 'Paulo', 'idade' : 34}
print(pessoa1)
print(pessoa2)
print(pessoa3)

keys = pessoa1.keys()
print(keys)

valores = pessoa1.values()
print(valores)

itens = pessoa1.items()
print(itens)

# Saber dicionário possui chave
'nome' in pessoa1.keys()

print(pessoa1.get('ano'))
