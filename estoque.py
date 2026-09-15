class Lote:
    def __init__(self, nome_produto, preco_compra, preco_venda, data_compra, data_vencimento, quantidade):
        self.nome_produto = nome_produto
        self.preco_compra = preco_compra
        self.preco_venda = preco_venda
        self.data_compra = data_compra
        self.data_vencimento = data_vencimento
        self.quantidade = quantidade

    def __repr__(self):
        return f"Lote({self.nome_produto}, qtd={self.quantidade}, venc={self.data_vencimento})"


class FilaDeLotes:
    def __init__(self):
        self._itens = []

    def enfileirar(self, lote):
        self._itens.append(lote)

    def quantidade_total(self):
        total = 0
        for lote in self._itens:
            total += lote.quantidade
        return total

    def desenfileirar_quantidade(self, quantidade):
        if self.quantidade_total() < quantidade:
            return False

        restante = quantidade
        while restante > 0:
            lote = self._itens[0]

            if lote.quantidade > restante:
                lote.quantidade -= restante
                restante = 0
            else:
                restante -= lote.quantidade
                lote.quantidade = 0
                self._itens.pop(0)

        return True

    def editar_quantidade(self, posicao, nova_quantidade):
        if posicao < 0 or posicao >= len(self._itens):
            return False
        self._itens[posicao].quantidade = nova_quantidade
        return True

    def listar_lotes(self):
        return list(self._itens)


class Estoque:
    def __init__(self):
        self._produtos = {}

    def adicionar_compra(self, nome_produto, preco_compra, preco_venda, data_compra, data_vencimento, quantidade):
        if nome_produto not in self._produtos:
            self._produtos[nome_produto] = FilaDeLotes()

        lote = Lote(nome_produto, preco_compra, preco_venda, data_compra, data_vencimento, quantidade)
        self._produtos[nome_produto].enfileirar(lote)

    def dar_baixa(self, nome_produto, quantidade):
        if nome_produto not in self._produtos:
            return False
        return self._produtos[nome_produto].desenfileirar_quantidade(quantidade)

    def consultar_quantidade(self, nome_produto):
        if nome_produto not in self._produtos:
            return 0
        return self._produtos[nome_produto].quantidade_total()

    def editar_quantidade(self, nome_produto, posicao, nova_quantidade):
        if nome_produto not in self._produtos:
            return False
        return self._produtos[nome_produto].editar_quantidade(posicao, nova_quantidade)

    def listar_produtos(self):
        return list(self._produtos.keys())

    def listar_lotes_do_produto(self, nome_produto):
        if nome_produto not in self._produtos:
            return []
        return self._produtos[nome_produto].listar_lotes()
