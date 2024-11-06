from modelos.cardapio.item_cardapio import ItemCardapio


class Prato(ItemCardapio):
    def __init__(self, nome, preco, descricao):
        super().__init__(nome, preco)
        self._descricao = descricao

    def __str__(self):
        # Garantir que todos os campos sejam alinhados corretamente
        return f"{'Nome do Item':<10}: {self._nome:<20} | {'Preço (R$)':<10}: {self._preco:>7.2f} | {'Descrição':<10}: {self._descricao:<20}"
