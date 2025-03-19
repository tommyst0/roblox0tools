import secrets, string, time, os, sys, requests
from datetime import date

# design
from rich import print

# selenium
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By

def Logger(text, type):
    if(type == 0): # fatal
        print(f'[red bold](\U0001F480) {text}[/red bold]')
    if(type == 1): # good
        print(f'[bright_green bold](\U0001F49C) {text}[/bright_green bold]')
    if(type == 2): # log
        print(f'[white bold](\U0001F939) {text}[/white bold]')

def LogarConta(cookies):
    ContaEntrou = False
    elapsed_time = 0

    req = requests.Session()
    req.cookies['.ROBLOSECURITY'] = cookies

    r = req.get('https://www.roblox.com/mobileapi/userinfo')
    if 'mobileapi/user' in r.url:
        f = open("cookies-checker/output.txt","a+")
        f.write(f"{cookies}\n")

        ff = open('meuscookies.txt', 'a')
        ff.write(f'{cookies}' + '\n\n')
        ff.close()

        Logger('Sucesso! Conta foi insirida em [white u]meuscookies.txt[/white u]', 1)
    else:
        Logger('Erro! [white u]Indo pro proximo cookie..[/white u]', 0)
        return True

    
def main():
    with open('cookies-checker/cookies.txt', 'r') as file:

        for line in file:
            try:
                account = line.strip()
                if(int(len(account)) != 0):
                    Logger(f'Verificando o Login -> [bright_green u]{account}[/bright_green u]', 2)
                    LogarConta(account)
            except:
                pass


    '''
    username = sys.argv[1].split(":")[0]
    password = sys.argv[1].split(":")[1]
    '''

if __name__ == "__main__":
    os.system('cls')
    logo = '''[bright_green]

 ▄████▄   ▒█████   ▒█████   ██ ▄█▀ ██▓▓█████   ██████     ▄████▄   ██░ ██ ▓█████  ▄████▄   ██ ▄█▀▓█████  ██▀███  
▒██▀ ▀█  ▒██▒  ██▒▒██▒  ██▒ ██▄█▒ ▓██▒▓█   ▀ ▒██    ▒    ▒██▀ ▀█  ▓██░ ██▒▓█   ▀ ▒██▀ ▀█   ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒
▒▓█    ▄ ▒██░  ██▒▒██░  ██▒▓███▄░ ▒██▒▒███   ░ ▓██▄      ▒▓█    ▄ ▒██▀▀██░▒███   ▒▓█    ▄ ▓███▄░ ▒███   ▓██ ░▄█ ▒
▒▓▓▄ ▄██▒▒██   ██░▒██   ██░▓██ █▄ ░██░▒▓█  ▄   ▒   ██▒   ▒▓▓▄ ▄██▒░▓█ ░██ ▒▓█  ▄ ▒▓▓▄ ▄██▒▓██ █▄ ▒▓█  ▄ ▒██▀▀█▄  
▒ ▓███▀ ░░ ████▓▒░░ ████▓▒░▒██▒ █▄░██░░▒████▒▒██████▒▒   ▒ ▓███▀ ░░▓█▒░██▓░▒████▒▒ ▓███▀ ░▒██▒ █▄░▒████▒░██▓ ▒██▒
░ ░▒ ▒  ░░ ▒░▒░▒░ ░ ▒░▒░▒░ ▒ ▒▒ ▓▒░▓  ░░ ▒░ ░▒ ▒▓▒ ▒ ░   ░ ░▒ ▒  ░ ▒ ░░▒░▒░░ ▒░ ░░ ░▒ ▒  ░▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░
  ░  ▒     ░ ▒ ▒░   ░ ▒ ▒░ ░ ░▒ ▒░ ▒ ░ ░ ░  ░░ ░▒  ░ ░     ░  ▒    ▒ ░▒░ ░ ░ ░  ░  ░  ▒   ░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░
░        ░ ░ ░ ▒  ░ ░ ░ ▒  ░ ░░ ░  ▒ ░   ░   ░  ░  ░     ░         ░  ░░ ░   ░   ░        ░ ░░ ░    ░     ░░   ░ 
░ ░          ░ ░      ░ ░  ░  ░    ░     ░  ░      ░     ░ ░       ░  ░  ░   ░  ░░ ░      ░  ░      ░  ░   ░     
░                                                        ░                       ░                               
                                                              
                        
[white bold](*)[/white bold][white] Lista de Cookies Verificados ficarao em [bright_green u]cookies.txt[bright_green u]

Iniciando...
'''
    print(logo)
    main()