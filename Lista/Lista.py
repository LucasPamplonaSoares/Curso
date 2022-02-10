# Lista pode ser Mutaveis

# Comida = ['Hamburgue', 'Pudim', 'Pastel']
# Bebida = ['Refrigerante', 'Suco', 'Cerveja']
# Comida[0] = 'Burguer King'
# Comida.append('teste') # APPEND adiciona elemento
# Comida.insert(0, 'oi') # Adiciona um elemento em uma posição específica
# Comida.remove('oi') # Usado para remover o conteúdo
# Comida.pop(1) # Remove pela chave
# if 'oi' in Comida: # Remove casa 'OI' está na lista de Comida
    # Comida.remove('oi')

# valores = list(range(4,11)) # Cria uma lista com elementos gerados automaticamente como no exemplo ao lado
# valores.sort() # Coloca os valores da lista em ordem
# valores.sort(reverse=True) # Colocou os valores ao contrário
# len(valores) # Tamanho dos elementos

# for lanche in Comida:
   #  print(f'Vou comer {lanche}')

# for drinque in Bebida:
    # print(f'VOu beber {drinque}')

'''num = [1, 2, 3, 9]
num[3] = 4 # Muda o valor
num.append(7)
num[4] = 5
num.insert(6, 0)
num.insert(2, 2)
if 6 in num:
    num.remove(6)
else:
    print('Número 5 não encontrado')
# num.pop(0)
num.sort(reverse=True)
print(num)
print(f'Essa lista tem {len(num)} elementos')'''

'''valores = list()
valores.append(1)
valores.append(2)
valores.append(6)'''

'''valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'A posição {c} foi encontrado o valor {v}')
valores.sort()
print(valores)

a = [1, 2, 3, 4]
b = a[:] # Copia oque está na lista 'A' e coloca na lista 'B'
b[3] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')

dados = ['Pedro', 19, 'Lucas', 29]
pessoa = list()
pessoa.append(dados[:])
# pessoa = [['Pedro', 19], ['Lucas', 29]]
print(pessoa)'''

'''teste = list()
teste.append('Lucas')
teste.append(19)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 20
galera.append(teste[:])
print(galera)

g = [['Lucas', 19], ['Vitoria', 19], ['Maria Alice', 18], ['Gabriel', 19]]
print(g[0] [0]) # Mostra a informação diante da posição que eu escolhi

for p in g:
    print(f'{p[0]} tem {p[1]} anos de idade.')'''

galera = list()
dado = list()
totmaior = totmenor = 0
for c in range(0, 5):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        totmaior += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmenor += 1
print('')
print(f'Temos {totmaior} maiores de idade e {totmenor} menores de idade')
