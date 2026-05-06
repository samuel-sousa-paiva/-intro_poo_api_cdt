'''



'''
import requests

def consulta_cep(cep):
    url = f'https://viacep.com.br/ws/{cep}/json/'
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()
        return dados
    else:
        return 'Erro na consulta ⚠'

print('=== Aula de API com Python: Consulta de CEP ===')

meu_cep = "05329000"
resultado = consulta_cep(meu_cep)

if isinstance(resultado, dict):
    print()
    print("CEP:", resultado.get("cep"))
    print("Rua:", resultado.get("logradouro"))
    print("Bairro:", resultado.get("bairro"))
    print("Cidade:", resultado.get("localidade"))
    print("Estado:", resultado.get("uf"))
else:
    print(resultado)