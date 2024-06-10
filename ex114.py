import requests
from utilidades import cores as c
url = 'https://www.google.com'
try:
    response = requests.get(url)
except requests.exceptions.ConnectionError:
    print(f'O SITE {url} ESTÁ {c.vermelho}INACESSÍVEL!')
else:
    print(f'O SITE {url} ESTÁ {c.amarelo}ACESSÍVEL!')
