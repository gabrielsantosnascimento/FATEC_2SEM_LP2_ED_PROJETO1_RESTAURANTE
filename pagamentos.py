class Pagamento:
    def __init__(self, nome_pagador, numero_comanda, forma_pagamento, valor_total, data_hora):
        self.nome_pagador = nome_pagador
        self.numero_comanda = numero_comanda
        self.forma_pagamento = forma_pagamento
        self.valor_total = valor_total
        self.data_hora = data_hora

    def __repr__(self):
        return f"Pagamento(comanda={self.numero_comanda}, valor={self.valor_total}, forma={self.forma_pagamento})"


class MapaPagamentos:
    def __init__(self):
        self._pagamentos = {}

    def registrar(self, pagamento):
        self._pagamentos[pagamento.numero_comanda] = pagamento

    def buscar_por_comanda(self, numero_comanda):
        return self._pagamentos.get(numero_comanda)

    def listar_todos(self):
        return list(self._pagamentos.values())
