from typing import List, Dict
from time import sleep

from models.produto import Produto
from utils.helper import formata_float_str_moeda

produtos: List[Produto] = []
carrinho: List[Dict[Produto, int]] = []

def main() -> object:
    menu()

def menu() -> None:
    print('==============================================================')
    print('======================== Bem-Vindo(a) ========================')
    print('========================= Gadi Shop ==========================')
    print('==============================================================')

    print('Selecione uma opcao abaixo: ')
    print('1 > Register Product')
    print('2 > List Product')
    print('3 > Buy Product')
    print('4 > View Product')
    print('5 > Closer Order')
    print('6 > Exit the system')

    opcao: int = int(input())
    if opcao == 1:
        cadastrar_produto()
    elif opcao == 2:
        listar_produto()
    elif opcao == 3:
        comprar_produto()
    elif opcao == 4:
        visualizar_produto()
    elif opcao == 5:
        fechar_pedido()
    elif opcao == 6:
        print('Ate breve!')
        sleep(2)
        exit(0)
    else:
        print('Invalid Option')
        sleep(1)
        menu()



def cadastrar_produto() -> None:
    print('Register Product')
    print('================')

    nome: str = input('Informe o nome do produto: ')
    preco: float = float(input('informe o preco do produto: '))

    produto: Produto = Produto(nome, preco)

    produtos.append(produto)

    print(f'O produto {produto.nome} foi cadastrado com sucesso!')
    sleep(2)
    menu()

def listar_produto() -> None:
    if len(produtos) > 0:
        print('List Product')
        print('============')
        for produto in produtos:
            print(produto)
            print('============')
            sleep(1)

    else:
        print(f'Ainda nao existe produtos cadastrados.')
    sleep(2)
    menu()

def comprar_produto() -> None:
    if len(produtos) > 0:
        print('informe o codigo do produto que deseja adicionar ao carrinho: ')
        print('==============================================================')
        print('==================== Produtos Disponiveis ====================')
        for produto in produtos:
            print(produto)
            print('=========================================')
            sleep(1)
        codigo: int = int(input())

        produto: Produto = pegar_produto(codigo)

        if produto:
            if len(carrinho) > 0:
                tem_no_carrinho: bool = False
                for item in carrinho:
                    quant: int = item.get(produto)
                    if quant:
                        item[produto] = quant + 1
                        print(f'O produto {produto.nome} agora possui {quant + 1} unidades no carrinho.')
                        tem_no_carrinho = True
                        sleep(2)
                        menu()

                if not tem_no_carrinho:
                    prod = {produto: 1}
                    carrinho.append(prod)
                    print(f'O produto {produto.nome} foi adicionando ao carrinho.')
                    sleep(2)
                    menu()

            else:
                item = {produto: 1}
                carrinho.append(item)
                print(f'O produto {produto.nome} foi adicionado ao carrinho.')
                sleep(2)
                menu()
        else:
            print(f'O produto com o codigo {codigo} nao foi encontrado.')
            sleep(2)
            menu()

    else:
        print('Ainda nao existem produtos para vender.')
    sleep(2)
    menu()


def visualizar_produto() -> None:
    if len(carrinho) > 0:
        print('Cart Products: ')

        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                print('========================')
                sleep(1)
    else:
        print('Ainda nao existem produtos no carrinho.')
    sleep(2)
    menu()

def fechar_pedido() -> None:
    if len(carrinho) > 0:
        valor_total: float = 0

        print('Cart Products')
        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                valor_total += dados[0].preco * dados[1]
                print('================================')
                sleep(1)
        print(f'Sua compra ficou {formata_float_str_moeda(valor_total)}')
        print('Ate breve!')
        carrinho.clear()
        sleep(5)

    else:
        print('Ainda nao existem produtos no carrinho')
    sleep(2)
    menu()

def pegar_produto(codigo: int) -> Produto:
    p: Produto = None

    for produto in produtos:
        if produto.codigo == codigo:
            p = produto
    return p

if __name__ == '__main__':
    main()
