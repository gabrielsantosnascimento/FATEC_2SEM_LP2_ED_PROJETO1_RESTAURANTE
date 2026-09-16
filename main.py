from estoque import Estoque
from comandas import ListaComandas
from pagamentos import MapaPagamentos
from consumo import MapaConsumo
from gerar_dados import popular_sistema
from persistencia import salvar_dados, carregar_dados
from relatorios import relatorio_vendas, relatorio_consumo


def main():
    estoque = Estoque()
    lista_comandas = ListaComandas()
    mapa_pagamentos = MapaPagamentos()
    mapa_consumo = MapaConsumo()

    popular_sistema(estoque, lista_comandas, mapa_pagamentos, mapa_consumo,
                     quantidade_compras=15, quantidade_comandas=8)

    salvar_dados("dados.pkl", estoque, lista_comandas, mapa_pagamentos, mapa_consumo)
    print("Dados salvos em dados.pkl")

    estoque, lista_comandas, mapa_pagamentos, mapa_consumo = carregar_dados("dados.pkl")
    print("Dados carregados novamente do arquivo")

    print("\nRELATORIO DE VENDAS")
    print(relatorio_vendas(mapa_pagamentos))

    print("\nRELATORIO DE CONSUMO")
    print(relatorio_consumo(mapa_consumo))

    print("\nCOMANDAS AINDA ABERTAS")
    print(lista_comandas.listar())

    print("\nESTOQUE RESTANTE")
    for produto in estoque.listar_produtos():
        print(produto, "-", estoque.consultar_quantidade(produto))


if __name__ == "__main__":
    main()
