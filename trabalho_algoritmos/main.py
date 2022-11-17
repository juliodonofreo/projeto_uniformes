"""
integrantes:
    julio donofreo morais
    vitor
    fabricio
    henriky
    joao
"""

from consultas import *
from registros import *
from validacoes import *
from rich import *

clr()
tabelaPedidos()
tabelaMenu()

# Menu interativo
while True:
    valor: int = menu()
    if valor == 1:
        clr()
        cadastrar_pedido()
        reset_tabela()
    elif valor == 2:
        clr()
        mostrar_pedidos()
        reset_tabela()
    elif valor == 3:
        clr()
        consulta_individual()
        reset_tabela()
    elif valor == 4:
        clr()
        consulta_nome()
        reset_tabela()
    elif valor == 5:
        clr()
        editar_pedido()
        reset_tabela()
    elif valor == 6:
        clr()
        deletar_pedido()
        reset_tabela()
    elif valor == 0:
        break
clr()
print(':hand: Até logo!')
