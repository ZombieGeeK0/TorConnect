# importamos las librerías
from colorama import Fore, Back
import os, sys, requests
from torpy import TorClient
from urllib.parse import urlparse

# definimos los colores de colorama
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'

# hacemos las funciones principales
def install_tor():
    os.system('clear')
    title = '''
\033[31m ██▓ ███▄    █   ██████ ▄▄▄█████▓\033[34m ▄▄▄       ██▓     ██▓    ▓█████  ██▀███  
\033[31m▓██▒ ██ ▀█   █ ▒██    ▒ ▓  ██▒ ▓▒\033[34m▒████▄    ▓██▒    ▓██▒    ▓█   ▀ ▓██ ▒ ██▒
\033[31m▒██▒▓██  ▀█ ██▒░ ▓██▄   ▒ ▓██░ ▒░\033[34m▒██  ▀█▄  ▒██░    ▒██░    ▒███   ▓██ ░▄█ ▒
\033[31m░██░▓██▒  ▐▌██▒  ▒   ██▒░ ▓██▓ ░ \033[34m░██▄▄▄▄██ ▒██░    ▒██░    ▒▓█  ▄ ▒██▀▀█▄  
\033[31m░██░▒██░   ▓██░▒██████▒▒  ▒██▒ ░ \033[34m ▓█   ▓██▒░██████▒░██████▒░▒████▒░██▓ ▒██▒
\033[31m░▓  ░ ▒░   ▒ ▒ ▒ ▒▓▒ ▒ ░  ▒ ░░   \033[34m ▒▒   ▓▒█░░ ▒░▓  ░░ ▒░▓  ░░░ ▒░ ░░ ▒▓ ░▒▓░
\033[31m ▒ ░░ ░░   ░ ▒░░ ░▒  ░ ░    ░    \033[34m  ▒   ▒▒ ░░ ░ ▒  ░░ ░ ▒  ░ ░ ░  ░  ░▒ ░ ▒░
\033[31m ▒ ░   ░   ░ ░ ░  ░  ░    ░      \033[34m  ░   ▒     ░ ░     ░ ░      ░     ░░   ░ 
\033[31m ░           ░       ░           \033[34m      ░  ░    ░  ░    ░  ░   ░  ░   ░     
'''
    print(title)
    print(Fore.BLUE + Back.RESET + '[#] Instalando...')
    print(Fore.RED + Back.RESET + '[#]> ----------------------------------------------------------------------- <[#]')
    os.system('sudo su')
    os.system('sudo apt update && sudo apt install -y tor torbrowser-launcher')
    os.system('torbrowser-launcher')
    print('[#]> ----------------------------------------------------------------------- <[#]')
    print(Fore.BLUE + Back.RESET + '\n[#] Presiona ENTER para volver al menú.')
    choice = input(Fore.RED + Back.RESET + '[#] ====>  ')
    menu()

def tor_requests():
    os.system('clear')
    title = '''
\033[31m▄▄▄█████▓ ▒█████   ██▀███  \033[34m ██▀███  ▓█████   █████   █    ██ ▓█████   ██████ ▄▄▄█████▓  ██████ 
\033[31m▓  ██▒ ▓▒▒██▒  ██▒▓██ ▒ ██▒\033[34m▓██ ▒ ██▒▓█   ▀ ▒██▓  ██▒ ██  ▓██▒▓█   ▀ ▒██    ▒ ▓  ██▒ ▓▒▒██    ▒ 
\033[31m▒ ▓██░ ▒░▒██░  ██▒▓██ ░▄█ ▒\033[34m▓██ ░▄█ ▒▒███   ▒██▒  ██░▓██  ▒██░▒███   ░ ▓██▄   ▒ ▓██░ ▒░░ ▓██▄   
\033[31m░ ▓██▓ ░ ▒██   ██░▒██▀▀█▄  \033[34m▒██▀▀█▄  ▒▓█  ▄ ░██  █▀ ░▓▓█  ░██░▒▓█  ▄   ▒   ██▒░ ▓██▓ ░   ▒   ██▒
\033[31m  ▒██▒ ░ ░ ████▓▒░░██▓ ▒██▒\033[34m░██▓ ▒██▒░▒████▒░▒███▒█▄ ▒▒█████▓ ░▒████▒▒██████▒▒  ▒██▒ ░ ▒██████▒▒
\033[31m  ▒ ░░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░\033[34m░ ▒▓ ░▒▓░░░ ▒░ ░░░ ▒▒░ ▒ ░▒▓▒ ▒ ▒ ░░ ▒░ ░▒ ▒▓▒ ▒ ░  ▒ ░░   ▒ ▒▓▒ ▒ ░
\033[31m    ░      ░ ▒ ▒░   ░▒ ░ ▒░\033[34m  ░▒ ░ ▒░ ░ ░  ░ ░ ▒░  ░ ░░▒░ ░ ░  ░ ░  ░░ ░▒  ░ ░    ░    ░ ░▒  ░ ░
\033[31m  ░      ░ ░ ░ ▒    ░░   ░ \033[34m  ░░   ░    ░      ░   ░  ░░░ ░ ░    ░   ░  ░  ░    ░      ░  ░  ░  
\033[31m             ░ ░     ░     \033[34m   ░        ░  ░    ░       ░        ░  ░      ░                 ░  
'''
    print(title)

    print(Fore.BLUE + Back.RESET + '[#] Ingresa la página a la que hacer requests.')
    pagina = input(Fore.RED + Back.RESET + '[#] ===>  ')
    print(Fore.BLUE + Back.RESET + '[#]> ----------------------------------------------------------------------- <[#]')
    proxies = {'https': 'socks5h://127.0.0.1:9150', 'https':'socks5h://127.0.0.1:9150'}
    respuesta = requests.get(pagina, proxies=proxies)
    print(respuesta.status_code)
    print('[#]> ----------------------------------------------------------------------- <[#]')
    print(Fore.RED + Back.RESET + '\n[#] Presiona ENTER para volver al menú.')
    choice = input(Fore.BLUE + Back.RESET + '[#] ====>  ')
    menu()

def info_url():
    os.system('clear')
    title = '''
\033[31m █    ██  ██▀███   ██▓    \033[34m ██▓ ███▄    █   █████▒▒█████  
\033[31m ██  ▓██▒▓██ ▒ ██▒▓██▒    \033[34m▓██▒ ██ ▀█   █ ▓██   ▒▒██▒  ██▒
\033[31m▓██  ▒██░▓██ ░▄█ ▒▒██░    \033[34m▒██▒▓██  ▀█ ██▒▒████ ░▒██░  ██▒
\033[31m▓▓█  ░██░▒██▀▀█▄  ▒██░    \033[34m░██░▓██▒  ▐▌██▒░▓█▒  ░▒██   ██░
\033[31m▒▒█████▓ ░██▓ ▒██▒░██████▒\033[34m░██░▒██░   ▓██░░▒█░   ░ ████▓▒░
\033[31m░▒▓▒ ▒ ▒ ░ ▒▓ ░▒▓░░ ▒░▓  ░\033[34m░▓  ░ ▒░   ▒ ▒  ▒ ░   ░ ▒░▒░▒░ 
\033[31m░░▒░ ░ ░   ░▒ ░ ▒░░ ░ ▒  ░\033[34m ▒ ░░ ░░   ░ ▒░ ░       ░ ▒ ▒░ 
\033[31m ░░░ ░ ░   ░░   ░   ░ ░   \033[34m ▒ ░   ░   ░ ░  ░ ░   ░ ░ ░ ▒  
\033[31m   ░        ░         ░  ░\033[34m ░           ░            ░ ░  
'''
    print(title)

    url = input("[#] Ingresa tu URL: ")

    parsed_url = urlparse(url)

    if parsed_url.scheme != 'http':
        print("\n[#] Error: Solo se admiten URLs con el esquema 'http'.")

    else:

        hostname = parsed_url.netloc

        port = 80

        with TorClient() as tor:
            
            with tor.create_circuit(3) as circuit:
            
                with circuit.create_stream((hostname, port)) as stream:
            
                    stream.send(f'GET {parsed_url.path} HTTP/1.0\r\nHost: {hostname}\r\n\r\n'.encode())
                    recv = stream.recv(1024)

        print(recv.decode())

def salir():
    print(Fore.RESET + Back.RESET)
    os.system('clear')
    sys.exit()

def volver_menu():
    print(Fore.BLUE + Back.RESET + '\n[#] Presiona ENTER para volver al menú.')
    choice = input(Fore.RED + Back.RESET + '[#] ====>  ')
    menu()

def error():
    print(Fore.BLUE + Back.RESET + '\n[#] Error. Presiona ENTER para volver al menú.')
    choice = input(Fore.RED + Back.RESET + '[#] ====>  ')
    menu()

# hacemos el menú
def menu():
    os.system('clear')
    title = '''
    \033[31m▄▄▄█████▓ ▒█████   ██▀███  \033[34m ▄████▄   ▒█████   ███▄    █  ███▄    █ ▓█████  ▄████▄  ▄▄▄█████▓
    \033[31m▓  ██▒ ▓▒▒██▒  ██▒▓██ ▒ ██▒\033[34m▒██▀ ▀█  ▒██▒  ██▒ ██ ▀█   █  ██ ▀█   █ ▓█   ▀ ▒██▀ ▀█  ▓  ██▒ ▓▒
    \033[31m▒ ▓██░ ▒░▒██░  ██▒▓██ ░▄█ ▒\033[34m▒▓█    ▄ ▒██░  ██▒▓██  ▀█ ██▒▓██  ▀█ ██▒▒███   ▒▓█    ▄ ▒ ▓██░ ▒░
    \033[31m░ ▓██▓ ░ ▒██   ██░▒██▀▀█▄  \033[34m▒▓▓▄ ▄██▒▒██   ██░▓██▒  ▐▌██▒▓██▒  ▐▌██▒▒▓█  ▄ ▒▓▓▄ ▄██▒░ ▓██▓ ░ 
    \033[31m  ▒██▒ ░ ░ ████▓▒░░██▓ ▒██▒\033[34m▒ ▓███▀ ░░ ████▓▒░▒██░   ▓██░▒██░   ▓██░░▒████▒▒ ▓███▀ ░  ▒██▒ ░ 
    \033[31m  ▒ ░░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░\033[34m░ ░▒ ▒  ░░ ▒░▒░▒░ ░ ▒░   ▒ ▒ ░ ▒░   ▒ ▒ ░░ ▒░ ░░ ░▒ ▒  ░  ▒ ░░   
    \033[31m    ░      ░ ▒ ▒░   ░▒ ░ ▒░\033[34m  ░  ▒     ░ ▒ ▒░ ░ ░░   ░ ▒░░ ░░   ░ ▒░ ░ ░  ░  ░  ▒       ░    
    \033[31m  ░      ░ ░ ░ ▒    ░░   ░ \033[34m░        ░ ░ ░ ▒     ░   ░ ░    ░   ░ ░    ░   ░          ░      
    \033[31m             ░ ░     ░     \033[34m░ ░          ░ ░           ░          ░    ░  ░░ ░               
    \033[31m                           \033[34m░                                              ░                 
    '''
    print(title + Fore.RED + Back.RESET + '\n[!] De ZombieGeek0: https://www.github.com/ZombieGeek0')

    options = '''
[00]: Salir.
[01]: Volver al menú.
[02]: Instalar El navegador Tor.
[03]: Hacer request anónima a una web pasando por Tor.
[04]: Obtener datos anónimamente de una URL del servicio HTTP.
'''
    print(Fore.BLUE + Back.RESET + options)

    choice = input(Fore.RED + Back.RESET + '[#] ===>  ')

    if choice == '00':
        salir()

    elif choice == '01':
        volver_menu()

    elif choice == '02':
        install_tor()

    elif choice == '03':
        tor_requests()

    elif choice == '04':
        info_url()

    else:
        error()

menu()
