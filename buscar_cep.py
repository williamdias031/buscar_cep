import requests

def buscar_cep(cep):
    try:
        url = f"https://viacep.com.br/ws/{cep}/json/"
        resposta = requests.get(url, timeout=5)
        resposta.raise_for_status()  # Garante que a requisição foi bem-sucedida

        dados = resposta.json()

        if "erro" in dados:
            print("⚠️ CEP não encontrado. Verifique e tente novamente.")
            return None

        return dados

    except requests.exceptions.RequestException as e:
        print(f"❌ Erro ao acessar a API ViaCEP: {e}")
        return None

def exibir_dados(dados):
    print("\n📍 Informações do CEP:")
    print(f"CEP: {dados.get('cep')}")
    print(f"Logradouro: {dados.get('logradouro')}")
    print(f"Bairro: {dados.get('bairro')}")
    print(f"Cidade: {dados.get('localidade')}")
    print(f"Estado: {dados.get('uf')}")

if __name__ == "__main__":
    print("🔎 Consulta de Endereço pelo CEP (ViaCEP)")
    cep = input("Digite um CEP (somente números): ").strip()

    if len(cep) == 8 and cep.isdigit():
        dados = buscar_cep(cep)
        if dados:
            exibir_dados(dados)
    else:
        print("⚠️ CEP inválido. Digite apenas 8 números.")
