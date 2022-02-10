# Tratamento de ERRO
try:
    a = int(input('Digite um Número: '))
    b = int(input('Digite um Número: '))
    r = a / b

# except Exception as erro:
    # print(f'Problema encontrado foi {erro.__class__}')
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados  que você digitou: ')
except ZeroDivisionError:
    print('Não foi possivel dividir um número por zero: ')
except KeyboardInterrupt:
    print('O Usuário não quis informar o seus dados! ')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__class__}')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre')