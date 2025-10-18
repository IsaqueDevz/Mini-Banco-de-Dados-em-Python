from lib.interface import *


def fileexists(name):
    try:
        file_obj = open(name, 'rt')
        file_obj.close()
    except FileNotFoundError:
        return False
    else:
        return True
    

def createfile(name):
    try:
        file_obj = open(name, 'wt+')
        file_obj.close()
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {name} criado com sucesso!')


def readfile(name):
    try:
        file_obj = open(name, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        header('PESSOAS CADASTRADAS')
        for line in file_obj:
            data = line.split(';')
            data[1] = data[1].replace('\n', '')
            print(f'{data[0]} \t\t\t\t{data[1]} anos')
    finally:
        file_obj.close()


def register(archive_name, name='Desconhecido', age=0):
    try:
        file_obj = open(archive_name, 'at')
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            file_obj.write(f'{name};{age}\n')
        except:
            print('Houve um ERRO na hora de escrever os dados!')
        else:
            print(f'Novo cadastro de {name} adicionado.')
            file_obj.close()