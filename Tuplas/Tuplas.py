'''lanche = ['pizza', 'macarrao']
print(lanche[1])
print(lanche[:1])

lan = ['teste', 'teste', 'teste']
for c in lan:
    print(c) '''

# Tuplas são Imutaveis

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
print(lanche)

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
print(lanche[2])

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
print(lanche[-3])

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
print(lanche[1:3])

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
print(lanche[:2])

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
print(lanche[2:])

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
print(lanche[-3:])

lanche = ('Hamburguer', 'Pizza', 'Pudim')
Bebidas = ('Suco', 'Refrigerante')
for comida in lanche:
    print(f'Vou comer {comida}')
for bebidas in Bebidas:
    print(f'Vou beber {bebidas}')

lanche = ('Hamburguer', 'Pizza', 'Pudim')
Bebidas = ('Suco', 'Refrigerante')
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')
for a in range(0, len(Bebidas)):
    print(f'Eu vou beber {Bebidas[a]}')
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
print(sorted(lanche)) # Ordenado em ordem

a = (1, 2, 3, 4)
b = (4, 5, 6, 7, 8)
c = a + b # junta as duas tuplas
print(c)
print(c.count(4))
print(len(c))
print(c.index(8)) # mostra em que posição está o item
print(c.index(4))
print(c.index(4, 4))

pessoa = ('Lucas', 19, 'Masculino', 64) # posso ter tanto str e int numa tupla junto
del (pessoa) # Deleta uma variavel
print(pessoa)