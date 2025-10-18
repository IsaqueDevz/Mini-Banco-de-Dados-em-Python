from lib.interface import *
from lib.archive import *
from time import sleep

archive_name = 'PessoasCadastradas.txt'

if not fileexists(archive_name):
    createfile(archive_name)

header('SISTEMA ARQUIVO v1.0')

while True:
    answer = menu(['Listar pessoas', 'Cadastrar pessoas', 'Sair do sistema'])
    if answer == 1:
        readfile(archive_name)

    elif answer == 2:
        header('NOVO CADASTRO')
        name = str(input('Nome: '))
        age = readint('Idade: ')
        register(archive_name, name, age)
        
    elif answer == 3:
        header('Saindo do sistema... Até logo!')
        break

    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(1)