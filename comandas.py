class ItemPedido:
    def __init__(self, nome_produto, quantidade, tipo):
        self.nome_produto = nome_produto
        self.quantidade = quantidade
        self.tipo = tipo  # "refeicao" ou "bebida"

    def __repr__(self):
        return f"{self.tipo}: {self.nome_produto} x{self.quantidade}"


class Comanda:
    def __init__(self, numero, nome_cliente, data_hora_abertura):
        self.numero = numero
        self.nome_cliente = nome_cliente
        self.data_hora_abertura = data_hora_abertura
        self.itens = []

    def adicionar_item(self, item):
        self.itens.append(item)

    def remover_item(self, nome_produto):
        for item in self.itens:
            if item.nome_produto == nome_produto:
                self.itens.remove(item)
                return True
        return False

    def __repr__(self):
        return f"Comanda({self.numero}, {self.nome_cliente})"


class ListaComandas:
    def __init__(self):
        self._itens = []

    def adicionar(self, comanda):
        self._itens.append(comanda)

    def buscar(self, numero):
        for comanda in self._itens:
            if comanda.numero == numero:
                return comanda
        return None

    def remover(self, numero):
        comanda = self.buscar(numero)
        if comanda is None:
            return False
        self._itens.remove(comanda)
        return True

    def listar(self):
        return list(self._itens)
