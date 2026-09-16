def relatorio_vendas(mapa_pagamentos):
    pagamentos = mapa_pagamentos.listar_todos()

    total_arrecadado = 0
    total_por_forma = {}

    for pagamento in pagamentos:
        total_arrecadado += pagamento.valor_total

        if pagamento.forma_pagamento not in total_por_forma:
            total_por_forma[pagamento.forma_pagamento] = 0
        total_por_forma[pagamento.forma_pagamento] += pagamento.valor_total

    return {
        "quantidade_vendas": len(pagamentos),
        "total_arrecadado": round(total_arrecadado, 2),
        "total_por_forma_pagamento": total_por_forma,
    }


def relatorio_consumo(mapa_consumo):
    consumos = mapa_consumo.listar_todos()

    quantidade_por_produto = {}

    for numero_comanda, itens in consumos:
        for item in itens:
            if item.nome_produto not in quantidade_por_produto:
                quantidade_por_produto[item.nome_produto] = 0
            quantidade_por_produto[item.nome_produto] += item.quantidade

    return quantidade_por_produto
