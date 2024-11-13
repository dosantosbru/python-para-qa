from modelos.restaurante import Restaurante
from modelos.cardapio.prato import Prato
from modelos.cardapio.bebida import Bebida

restaurante_praca = Restaurante('praça', 'Gourmet')

prato_pao = Prato('Pãozinho', 2.0, 'paozinho de queijo')
bebida_suco = Bebida("Refrigerante", 7.50, "500ml")

restaurante_praca.adicionar_item_cardapio(bebida_suco)
restaurante_praca.adicionar_item_cardapio(prato_pao)


def main():
    # Corrigido para chamar o método corretamente
    restaurante_praca.exibir_cardapio


if __name__ == '__main__':
    main()
