import requests
import json
import time
from colorama import Fore

url = 'https://discord.com/api/v9/users/@me/lootboxes/open'

with open("config.json", "r") as arquivo:
    token = json.load(arquivo)

headers = {
    'Authorization': token['token'],
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    'X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyMy4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTIzLjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjI4MDQ3MiwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0='
}

tentativa_atual = 1

while True:
    res = requests.post(url, headers=headers)

    if res.status_code == 200:
        print(f'{Fore.WHITE}[{Fore.GREEN}{tentativa_atual}{Fore.WHITE}] {Fore.GREEN}Novo item coletado!')
    elif res.status_code == 429:
        print(f'{Fore.WHITE}[{Fore.RED}!{Fore.WHITE}] {Fore.RED}Você está coletando itens muito rapidamente! Aguarde um pouco antes de tentar novamente.')
    else:
        print(f'{Fore.WHITE}[{Fore.RED}!{Fore.WHITE}] {Fore.RED}Ocorreu um erro na tentativa {tentativa_atual}:', res.status_code)

    tentativa_atual += 1

    time.sleep(3) 
