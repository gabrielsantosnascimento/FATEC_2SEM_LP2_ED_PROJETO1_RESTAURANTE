from pagamentos import Pagamento


class MapaConsumo:
    def __init__(self):
        self._consumos = {}

    def registrar(self, numero_comanda, itens):
        self._consumos[numero_comanda] = itens

    def buscar_por_comanda(self, numero_comanda):
        return self._consumos.get(numero_comanda)

    def listar_todos(self):
        return list(self._consumos.items())


def fechar_comanda(lista_comandas, estoque, mapa_pagamentos, mapa_consumo,
                    numero_comanda, nome_pagador, forma_pagamento, data_hora):
    comanda = lista_comandas.buscar(numero_comanda)
    if comanda is None:
        return False

    if not comanda.itens:
        lista_comandas.remover(numero_comanda)
        return True

    valor_total = 0
    for item in comanda.itens:
        sucesso, valor = estoque.dar_baixa(item.nome_produto, item.quantidade)
        valor_total += valor

    pagamento = Pagamento(nome_pagador, numero_comanda, forma_pagamento, valor_total, data_hora)
    mapa_pagamentos.registrar(pagamento)
    mapa_consumo.registrar(numero_comanda, comanda.itens)
    lista_comandas.remover(numero_comanda)
    return True
