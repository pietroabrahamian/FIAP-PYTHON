import json

def main():
    with open ("GBP.json") as arquivo:
        dados_gbp = json.loads(arquivo)

    print(f"Taxas de cambio de GBP para outras moedas: {dados_gbp["rates"]} ")

def main_dolar():
    