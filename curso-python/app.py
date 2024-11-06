from modelos.restaurante import Restaurante
from modelos.cardapio.prato import Prato
from modelos.cardapio.bebida import Bebida


restaurante_praca = Restaurante('praça', 'Gourmet')
bebida_suco = Bebida('Suco', 5.0, 'grande')
prato_pao = Prato('Pãozinho', 2.0, 'paozinho de queijo')
restaurante_praca.adicionar_item_cardapio(bebida_suco)
restaurante_praca.adicionar_item_cardapio(prato_pao)


def main():
    print(bebida_suco)
    print(prato_pao)


if __name__ == '__main__':
    main()
