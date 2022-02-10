n = int(input('DIgite um numeo: '))
for c in range(0, n + 1):
    print(c)

i = int(input('Inicio: '))
f = int(input('Fim '))
p = int(input('Passo: '))
for c in range(0, f + 1, p):
    print(c)

s = 0
for c in range(0, 3):
    n = int(input('Digite um valor : '))
    s += n
