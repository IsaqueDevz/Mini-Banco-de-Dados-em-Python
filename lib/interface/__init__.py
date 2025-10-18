def readint(message):
    while True:
        numberint = input(message)
        try:
            numberint = int(numberint)
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[0;31mO usuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return numberint
            

def readfloat(message):
    while True:
        numberfloat = input(message)
        try:
            numberfloat = float(numberfloat)
            return numberfloat
        except:
            print('\033[0;31mERRO! Digite um número real válido.\033[0;m')


def line(size=42):
    global centersize
    centersize = size
    return '-' * size
    

def header(text):
    print(line())
    print(text.center(42))
    print(line())


def menu(list):
    header('MENU PRINCIPAL')
    count = 1
    for item in list:
        print(f'\033[33m{count}\033[m - \033[34m{item}\033[m')
        count += 1
    print(line())
    option = readint('\033[32mSua opção:\033[m ')
    return option