import os

diretorio = 'arquivo_filtrado.txt'

def file_dir():
    with open(diretorio, 'r') as file:
        for line in file:
            try:
                account = line.strip()
                if(int(len(account)) != 0):
                    username = account.split(":")[0]
                    password = account.split(":")[1]

                    if(username != 'username'):
                        ff = open('account-checker/contas.txt', 'a')
                        ff.write(f'\n{username}:{password}')
                        print(f'{username}:{password}')
                        ff.close()
            except:
                pass


print('(Carregando..)')
file_dir()