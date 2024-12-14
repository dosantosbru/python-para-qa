from modelos.cardapio.item_cardapio import ItemCardapio


class Bebida(ItemCardapio):
    def __init__(self, nome, preco, tamanho):
        super().__init__(nome, preco)
        self._tamanho = tamanho

    @property
    def tamanho(self):
        return self._tamanho

    def __str__(self):
        return f"{'Nome do Item'}: {self.nome:<15} | {'Preço (R$)'}: {self.preco:>7.2f} | {'Tamanho'}: {self._tamanho:<10}"
