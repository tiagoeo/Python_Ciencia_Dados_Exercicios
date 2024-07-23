# Operações de conjunto
# Disjunto
conj1 = set(range(0,10,2))
conj2 = set(range(1,11,2))
print('Conjunto 1', conj1)
print('Conjunto 2', conj2)
print(conj1.isdisjoint(conj2))

# Subconjunto
subconj1 = set(range(15))
subconj2 = set(range(3, 15, 3))
print('subconj1 1', subconj1)
print('subconj1 2', subconj2)

print('subconj1 é subconjunto de subconj2: ', subconj1.issubset(subconj2))

# Subconjuntos próprios
print('subconj1 é subconjunto próprio de subconj2: ', subconj1 < subconj2)
print('subconj1 é superconjunto próprio de subconj2: ', subconj1.issuperset(subconj2))

# União
print('subconj1 união com subconj2', subconj1.union(subconj2))

# Interseção
print('subconj1 interseção com subconj2', subconj1.intersection(subconj2))

# Diferença
print('subconj1 diferença com subconj2', subconj1.difference(subconj2))

# Atualizando os conjuntos
conj3 = {0, 1 , 2, 3}
print('conj3 inicial', conj3)
conj3.update({4, 5, 6, 7, 8})
conj3.update([9, 10])
conj3.update(range(11, 15))
print('conj3 após o update', conj3)