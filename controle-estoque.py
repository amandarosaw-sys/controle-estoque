# Sistema de Controle de Estoque
#AMANDA ROSA DOS SANTOS 

estoque = []


def exibir_menu():
    print('Menu:')
    print('1. Cadastrar novo produto')
    print('2. Calcular estoque')
    print('3. Sair')


def codigo_existe(estoque, codigo):
    for item in estoque:
        if item['codigo'] == codigo:
            return True
    return False


def cadastrar_produto(estoque):
    print('Cadastrar novo produto')
    codigo = int(input('Código: '))
    if codigo_existe(estoque, codigo):
        print('Erro, código existente no estoque')
        return

    nome = input('Nome do produto: ')
    preco = float(input('Preço: '))
    quantidade = int(input('Quantidade: '))

    if preco < 0 or quantidade < 0:
        print('Erro, preço ou quantidade inválidos')
        return

    produto = {
        'codigo': codigo,
        'nome': nome,
        'preco': preco,
        'quantidade': quantidade
    }
    estoque.append(produto)
    print('Produto cadastrado com sucesso!')


def calcular_total_estoque(estoque):
    total = 0
    for item in estoque:
        total = total + item['quantidade']
    return total


def main():
    opcao = ''
    while opcao != '3':
        exibir_menu()
        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            cadastrar_produto(estoque)
        elif opcao == '2':
            total = calcular_total_estoque(estoque)
            print(f'O total de produtos em estoque é: {total}')
        elif opcao == '3':
            print('Saindo do programa')
        else:
            print('Opção inválida')


main()