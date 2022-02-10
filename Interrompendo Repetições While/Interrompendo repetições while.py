'''cont = 1
while True:
    print(cont, ' > ', end='')
    cont += 1'''

'''n = cont = 0
while cont < 5:
    n = int(input('Digite um valor: '))
    cont += 1'''

n = s = 0
while True:
    n = int(input('Digite um valor: '))
    if n == 999:
        break
    s = s + n
print('A soma vale {}'.format(s))