import requests

cep = input('Dite seu cep:')
via_cep = f'https://viacep.com.br/ws/{cep}/json/'
requicisao = requests.get(via_cep)

print(requicisao)

print(f"CEP: {requicisao.json()['cep']}")
print(f"RUA: {requicisao.json()['logradouro']}")
print(f"BAIRRO: {requicisao.json()['bairro']}")
print(f"CIDADE:{requicisao.json()['localidade']}")
print(f"ESTADO: {requicisao.json()['estado']}")