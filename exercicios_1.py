# Tipos
type(1)
type(2.0)
type(True)
type("Tipo String")

# Módulo de um número
x = 5
y = 2
print('resultado da divisão é = ', x/y)
print('resultado inteiro desta divisão é = ', x//y)
print('resultado do resto é = ', x%y)

# Declaração Multipla
a = 27//3
b = a**3
print('a = ', a)
print('b', b, sep=' = ')
print(f"a = {a} e b = {b}")

# Associação
'primeiro' in ['primeiro', 'segundo', 'terceiro']
'b' not in 'calcio'

# Indexando
nome = 'borboleta'
print('index 0 = ', nome[0])
print('index -1 = ', nome[-1])
print('index 2:5 = ', nome[2:5])
print('index 4: = ', nome[4:])
print('index :5 = ', nome[:5])

# Funções Auxiliares de String
nm = "João Paulo"
print(nm.capitalize())
print(nm.lower())
print(nm.upper())
print(nm.swapcase())
print(nm.title())

# Strings \t = tabulação; \r muda linha; \n nova linha, para string bruta usa-se
windows_local = r"c:\users\public\desktop\teste"
print(windows_local)
