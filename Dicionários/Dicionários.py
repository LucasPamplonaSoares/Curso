# print(filme.values()) # pega a parte de cima
# print(filme.keys()) # pega a parte de baixo
# print(filme.items()) # pega a parte de baixo e a parte de cima

'''pessoas = {'Nome': 'Lucas',
           'Idade': 19,
           'Sexo': 'Masculino'
}
# print(pessoas.keys())
# print(pessoas.values())
# print(pessoas.items())
# del pessoas['Sexo']
pessoas['Nome'] = 'Pedro'
pessoas['Peso'] = 63
for k, i in pessoas.items():
    print(f'{k} = {i}')'''

'''Brasil = []
estado1 = {'UF': 'Rio de Janeiro', 'Sigla': 'RJ'}
estado2 = {'UF': 'Santa Catarina', 'Sigla': 'SC'}
Brasil.append(estado1)
Brasil.append(estado2)

print(Brasil[0] ['UF'])
print(Brasil[1] ['UF'])
print(Brasil[0] ['Sigla'])
print(Brasil[1] ['Sigla'])'''

estado = dict()
brasil = list()
for c in range(0, 5):
    estado['UF'] = str(input('Unidade Federativa: '))
    estado['Sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()