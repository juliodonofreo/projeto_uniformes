from consultas import *
from registros import *


def menu() -> int:
    while True:
        try:
            funcao: int = int(input('''[0] sair
[1] cadastrar pedidos
[2] mostrar todos os pedidos
[3] consulta individual por id
[4] consulta por nome
[5] editar pedido
[6] deletar pedido
digite aqui: '''))
            if funcao < 0 or funcao > 6:
                print('Por favor digite um dos valores mencionados. ')
            else:
                return funcao
        except ValueError:
            print('Por favor digite um número. ')


while True:
    valor: int = menu()
    if valor == 1:
        cadastrar_pedido()
    elif valor == 2:
        mostrar_pedidos()
    elif valor == 3:
        consulta_individual()
    elif valor == 4:
        consulta_nome()
    elif valor == 5:
        editar_pedido()
    elif valor == 6:
        deletar_pedido()
    elif valor == 0:
        break
print('até logo!')
