import random
from faker import Faker

from comandas import Comanda, ItemPedido, ListaComandas
from consumo import fechar_comanda

fake = Faker("pt_BR")

BEBIDAS = ["Coca-Cola", "Suco", "Agua"]
REFEICOES = ["Feijoada", "Escondidinho", "Salada Caesar", "Frango Grelhado"]


def gerar_estoque_aleatorio(estoque, quantidade_compras=10):
    produtos = BEBIDAS + REFEICOES
    for _ in range(quantidade_compras):
        nome = random.choice(produtos)
        data_compra = fake.date_between(start_date="-30d", end_date="today")
        data_vencimento = fake.date_between(start_date=data_compra, end_date="+60d")
        quantidade = random.randint(10, 50)
        preco_compra = round(random.uniform(2.0, 15.0), 2)
        preco_venda = round(preco_compra * random.uniform(1.5, 2.5), 2)

        estoque.adicionar_compra(nome, preco_compra, preco_venda, data_compra, data_vencimento, quantidade)


def gerar_comandas_aleatorias(lista_comandas, quantidade_comandas=5):
    for numero in range(1, quantidade_comandas + 1):
        nome_cliente = fake.name()
        data_hora = fake.date_time_between(start_date="-1d", end_date="now")
        comanda = Comanda(numero, nome_cliente, data_hora)

        qtd_itens = random.randint(0, 4)
        for _ in range(qtd_itens):
            if random.choice([True, False]):
                nome_produto = random.choice(BEBIDAS)
                tipo = "bebida"
            else:
                nome_produto = random.choice(REFEICOES)
                tipo = "refeicao"
            comanda.adicionar_item(ItemPedido(nome_produto, random.randint(1, 3), tipo))

        lista_comandas.adicionar(comanda)


def fechar_todas_as_comandas(lista_comandas, estoque, mapa_pagamentos, mapa_consumo):
    numeros = [c.numero for c in lista_comandas.listar()]
    for numero in numeros:
        comanda = lista_comandas.buscar(numero)
        forma = random.choice(["PIX", "Cartao", "Dinheiro"])
        data_hora = fake.date_time_between(start_date="-1d", end_date="now")
        fechar_comanda(lista_comandas, estoque, mapa_pagamentos, mapa_consumo,
                        numero, comanda.nome_cliente, forma, data_hora)


def popular_sistema(estoque, lista_comandas, mapa_pagamentos, mapa_consumo,
                     quantidade_compras=10, quantidade_comandas=5):
    gerar_estoque_aleatorio(estoque, quantidade_compras)
    gerar_comandas_aleatorias(lista_comandas, quantidade_comandas)
    fechar_todas_as_comandas(lista_comandas, estoque, mapa_pagamentos, mapa_consumo)
