import pickle


def salvar_dados(caminho, estoque, lista_comandas, mapa_pagamentos, mapa_consumo):
    dados = {
        "estoque": estoque,
        "lista_comandas": lista_comandas,
        "mapa_pagamentos": mapa_pagamentos,
        "mapa_consumo": mapa_consumo,
    }
    with open(caminho, "wb") as arquivo:
        pickle.dump(dados, arquivo)


def carregar_dados(caminho):
    with open(caminho, "rb") as arquivo:
        dados = pickle.load(arquivo)
    return dados["estoque"], dados["lista_comandas"], dados["mapa_pagamentos"], dados["mapa_consumo"]
