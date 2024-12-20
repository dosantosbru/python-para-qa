from modelos.cardapio.item_cardapio import ItemCardapio


class Prato(ItemCardapio):
    def __init__(self, nome, preco, descricao):
        super().__init__(nome, preco)
        self._descricao = descricao
    
    @property
    def descricao(self):
        return self._descricao
    

    def __str__(self):
        return f"{'Nome do Item'}: {self.nome:<20} | {'Preço (R$)':>5}: {self.preco:>7.2f} | {'Descrição'}: {self._descricao:<20}"
