# c = 1
# while c < 10: ''''Usado quando se sabe o limite'''
 #    print(c)
 #    c = c + 1

''''n = 1
while n != 0:
    n = int(input('Digite um valor: '))''''' \

'''r = 'S'
while r == 'S':
    n = int(input('DIgite um valor: '))
    r = str(input('Deseja continuar ? [S/N]')).upper()'''''

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        par += 1
    else:
        impar += 1
print('VocÇe digitou {} números pares e {} impares'.format(par, impar))