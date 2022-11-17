from time import sleep
from typing import Union
from rich import *
from rich.console import Console
from rich.table import Table

console = Console()
tabela_pedidos = Table(title="[green]Pedidos[/]")


# Limpar a tela
def clr() -> None:
    print("\n" * 100)


# Criação de lista
def criar_lista() -> list:
    # Tratamento de erro
    try:
        with open('dados.txt', 'r') as dados:
            next(dados)
            next(dados)
            linhas: Union[list, map] = dados.readlines()
            linhas = map(lambda linha: linha.rstrip().split('/'), linhas)
            lista: list = [{'id': int(linha[0]),
                            'nome do cliente': linha[1],
                            'cor do uniforme': linha[2],
                            'tipo do uniforme': linha[3],
                            'quantidade de uniformes': linha[4]} for linha in linhas]
    except (FileNotFoundError, StopIteration):
        with open('dados.txt', 'w') as dados:
            dados.write('id/nome/cor/tipo do uniforme/quantidade de uniformes\n\n')
            lista = []
    return lista


# Interface visual da tabela
def tabelaPedidos() -> None:
    lista_pedidos = []
    tabela_pedidos.add_column('ID')
    tabela_pedidos.add_column('Nome do cliente')
    tabela_pedidos.add_column('Cor do uniforme')
    tabela_pedidos.add_column('Tipo do uniforme')
    tabela_pedidos.add_column('Quantidade')
    lista: list = criar_lista()
    for item in lista:
        for v in item.values():
            if v != str:
                v = str(v)
            lista_pedidos.append(v.capitalize())
        tabela_pedidos.add_row(lista_pedidos[0], lista_pedidos[1], lista_pedidos[2], lista_pedidos[3], lista_pedidos[4])
        lista_pedidos = []


# Reset da tabela em caso de alteração da mesma
def reset_tabela() -> None:
    global tabela_pedidos
    tabela_pedidos = Table(title='[green]Pedidos[/]')
    lista_pedidos = []
    tabela_pedidos.add_column('ID')
    tabela_pedidos.add_column('Nome do cliente')
    tabela_pedidos.add_column('Cor do uniforme')
    tabela_pedidos.add_column('Tipo do uniforme')
    tabela_pedidos.add_column('Quantidade')
    lista: list = criar_lista()
    for item in lista:
        for v in item.values():
            if v != str:
                v = str(v)
            lista_pedidos.append(v.capitalize())
        tabela_pedidos.add_row(lista_pedidos[0], lista_pedidos[1], lista_pedidos[2], lista_pedidos[3], lista_pedidos[4])
        lista_pedidos = []


# Visualização dos pedidos
def mostrar_pedidos() -> None:
    lista: list = criar_lista()
    # Caso não exista nenhum pedido cadastrado
    if not lista:
        print('[red]Não há pedidos para mostrar.[/]')
        sleep(2)
        clr()
        return
    # Impressão da interface visual da tabela de pedidos
    console.print(tabela_pedidos)
    input('Pressione ENTER para prosseguir. ')
    clr()


# Consulta do pedido através do ID
def consulta_individual() -> None:
    lista: list = criar_lista()
    # Caso não exista nenhum pedido cadastrado
    if not lista:
        print('[red]Ainda não há pedidos para consultar.[/]')
        sleep(2)
        return
    while True:
        # Tratamento de erro
        try:
            consulta: int = int(input('Digite aqui o ID do pedido que deseja procurar: '))
        # Caso o valor digitado não seja um número inteiro
        except ValueError:
            clr()
            print('[red]O ID deve ser um número.[/]')
        # Impressão visual do pedido solicitado
        else:
            for item in lista:
                if item['id'] == consulta:
                    print("")
                    for k, v in item.items():
                        print(f'{k}: {v}'.upper())
                    print("")
                    input('pressione ENTER para prosseguir. ')
                    clr()
                    return
            # Caso o ID digitado não exista
            print('[red]ID não encontrado.[/]')
            sleep(2)
            clr()


# Consulta do pedido através do nome do cliente
def consulta_nome() -> None:
    lista: list = criar_lista()
    # Caso não exista nenhum pedido cadastrado
    if not lista:
        print('[red]Ainda não há pedidos para consultar.[/]')
        sleep(2)
        clr()
        return
    consulta: str = str(input('Digite o nome que você quer procurar: ')).capitalize()
    consultado: bool = False
    # Impressão visual do pedido solicitado
    for item in lista:
        primeiro_nome = item['nome do cliente'].split()[0]
        if consulta == primeiro_nome:
            print("")
            for k, v in item.items():
                consultado = True
                print(f'{k}: {v}'.upper())
            print("")
    # Caso o nome digitado não esteja cadastrado
    if not consultado:
        print('[red]Nome não encontrado.[/]')
    sleep(2)
    input('Pressione ENTER para prosseguir. ')
    clr()
