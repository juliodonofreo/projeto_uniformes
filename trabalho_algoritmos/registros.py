from validacoes import *


def cadastrar_pedido() -> None:
    nome_cliente: str = validar_nome('nome do cliente: ')
    cor_uniforme: str = validar_cor('cor do uniforme: ')
    tipo_uniforme: str = validar_tipo('tipo do uniforme (escolar, militar ou profissional) ')
    quantidade: int = validar_quantidade('quantidade de uniformes a produzir:  ')
    id_pedido: int = gerar_id()
    with open('dados.txt', 'a') as dados:
        dados.write(f'{id_pedido}/{nome_cliente}/{cor_uniforme}/{tipo_uniforme}/{quantidade}\n')


def editar_pedido() -> None:
    lista: list = criar_lista()
    if not lista:
        print('ainda não há pedidos para editar. ')
        sleep(1)
        return
    pedido: int = validar_id('qual o id do pedido que você deseja editar? [0 cancela] ', lista)
    if pedido == 0:
        return
    lista[pedido - 1]["cor do uniforme"] = validar_cor('nova cor: ')
    lista[pedido - 1]["tipo do uniforme"] = validar_tipo('novo tipo do uniforme (escolar, militar ou profissional) ')
    lista[pedido - 1]["quantidade de pedidos"] = validar_quantidade('nova quantidade: ')
    with open('dados.txt', 'w') as dados:
        dados.write('id/nome/cor/tipo do uniforme/quantidade de pedidos\n\n')
        for linha in lista:
            linha = '/'.join(str(v) for v in linha.values()) + '\n'
            dados.write(linha)


def deletar_pedido() -> None:
    lista: list = criar_lista()
    if not lista:
        print('ainda não há pedidos para deletar. ')
        sleep(1)
        return
    id_cliente: int = validar_id('quer deletar qual id? [0 cancela] ', lista)
    if id_cliente == 0:
        return
    with open('dados.txt', 'w') as dados:
        dados.write('id/nome/cor/tipo do uniforme/quantidade de pedidos\n\n')
        for linha in lista:
            if linha['id'] != id_cliente:
                if linha['id'] > id_cliente:
                    linha['id'] -= 1
                linha = '/'.join(str(v) for v in linha.values()) + '\n'
                dados.write(linha)
