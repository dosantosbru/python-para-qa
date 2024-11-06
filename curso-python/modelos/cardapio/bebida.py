from modelos.cardapio.item_cardapio import ItemCardapio


class Bebida(ItemCardapio):
    def __init__(self, nome, preco, tamanho):
        super().__init__(nome, preco)
        self._tamanho = tamanho

    def __str__(self):

        return f"{'Nome do Item':<10}: {self._nome:<20} | {'Preço (R$)':<10}: {self._preco:>7.2f} | {'Tamanho':<10}: {self._tamanho:<10}"
