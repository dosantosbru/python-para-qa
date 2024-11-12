from modelos.cardapio.item_cardapio import ItemCardapio


class Bebida(ItemCardapio):
    def __init__(self, nome, preco, tamanho):
        super().__init__(nome, preco)  # Chama o construtor da classe base
        self._tamanho = tamanho

    @property
    def tamanho(self):
        return self._tamanho

    def __str__(self):
        return f"{'Nome do Item':<15}: {self.nome:<20} | {'Preço (R$)':<12}: {self.preco:>7.2f} | {'Tamanho':<10}: {self.tamanho:<10}"
