from time import sleep
from typing import Union


def criar_lista() -> list:
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
                            'quantidade de pedidos': linha[4]} for linha in linhas]
    except (FileNotFoundError, StopIteration):
        with open('dados.txt', 'w') as dados:
            dados.write('id/nome/cor/tipo do uniforme/quantidade de pedidos\n\n')
            lista = []
    return lista


def mostrar_pedidos() -> None:
    lista: list = criar_lista()
    if not lista:
        print('não há pedidos para mostrar. ')
        sleep(1)
        return
    for item in lista:
        for k, v in item.items():
            print(f'{k}: {v}')
        sleep(1)
        print()
    input('pressione enter para prosseguir. ')


def consulta_individual() -> None:
    lista: list = criar_lista()
    if not lista:
        print('ainda não há pedidos para consultar. ')
        sleep(1)
        return
    consulta: str = str(input('digite aqui o id do pedido que deseja procurar:')).capitalize()
    for item in lista:
        if item['id'] == int(consulta):
            for k, v in item.items():
                print(f'{k}: {v}')
            input('pressione enter para prosseguir. ')
            return
    print('id não encontrado. ')
    sleep(1)


def consulta_nome() -> None:
    lista: list = criar_lista()
    if not lista:
        print('ainda não há pedidos para consultar. ')
        sleep(1)
        return
    consulta: str = str(input('digite o nome que você quer procurar: ')).capitalize()
    consultado: bool = False
    for item in lista:
        primeiro_nome = item['nome do cliente'].split()[0]
        if consulta == primeiro_nome:
            for k, v in item.items():
                consultado = True
                print(f'{k}: {v}')
    if not consultado:
        print('nome não encontrado. ')
    sleep(1)
    input('pressione enter para prosseguir. ')
