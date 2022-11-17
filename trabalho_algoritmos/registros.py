from validacoes import *
from rich import *


# Cadastro de pedido
def cadastrar_pedido() -> None:
    nome_cliente: str = validar_nome('Nome do cliente: ')
    cor_uniforme: str = validar_cor('Cor do uniforme: ')
    tipo_uniforme: str = validar_tipo(
        'Tipo do uniforme (Escolar, Militar, Industrial ou Esportivo): ')
    quantidade: int = validar_quantidade(
        'Quantidade de uniformes a produzir: ')
    id_pedido: int = gerar_id()
    # Registro dos dados no .txt
    with open('dados.txt', 'a') as dados:
        dados.write(
            f'{id_pedido}/{nome_cliente}/{cor_uniforme}/{tipo_uniforme}/{quantidade}\n')
    clr()
    print("[green]Pedido cadastrado com sucesso! :heavy_check_mark:[/]")
    sleep(3)
    clr()


# Validações para edição do pedido
def editar_pedido() -> None:
    lista: list = criar_lista()
    # Caso não existam pedidos registrados
    if not lista:
        clr()
        print('[red]Ainda não há pedidos para editar.[/]')
        sleep(2)
        clr()
        return
    # Edição do pedido por meio do ID
    pedido: int = validar_id('Qual o ID do pedido que você deseja editar? [0 cancela]: ', lista)
    # Opção de retorno
    if pedido == 0:
        clr()
        return
    # Registro de novos valores (Edição do pedido)
    lista[pedido - 1]["cor do uniforme"] = validar_cor('Nova cor: ')
    lista[pedido - 1]["tipo do uniforme"] = validar_tipo(
        'Novo tipo do uniforme (Escolar, Militar, Industrial ou Esportivo): ')
    lista[pedido -
          1]["quantidade de pedidos"] = validar_quantidade('Nova quantidade: ')
    # Sobrescrição dos dados anteriores pelos novos
    with open('dados.txt', 'w') as dados:
        dados.write('id/nome/cor/tipo do uniforme/quantidade de pedidos\n\n')
        for linha in lista:
            linha = '/'.join(str(v) for v in linha.values()) + '\n'
            dados.write(linha)
    clr()
    print("[green]Pedido alterado com sucesso! :heavy_check_mark:[/]")
    sleep(3)
    clr()


# Exclusão de pedido existente
def deletar_pedido() -> None:
    lista: list = criar_lista()
    # Caso não existam pedidos registrados
    if not lista:
        clr()
        print('[red]Ainda não há pedidos para deletar.[/]')
        sleep(2)
        clr()
        return
    # Seleção do ID para exclusão
    id_cliente: int = validar_id('Quer deletar qual id? [0 cancela]: ', lista)
    # Opção de retorno
    if id_cliente == 0:
        clr()
        return
    # Exclusão dos dados do pedido
    with open('dados.txt', 'w') as dados:
        dados.write('id/nome/cor/tipo do uniforme/quantidade de pedidos\n\n')
        for linha in lista:
            if linha['id'] != id_cliente:
                if linha['id'] > id_cliente:
                    linha['id'] -= 1
                linha = '/'.join(str(v) for v in linha.values()) + '\n'
                dados.write(linha)
