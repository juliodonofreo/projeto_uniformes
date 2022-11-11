from consultas import criar_lista, mostrar_pedidos
from time import sleep


def validar_nome(mensagem) -> str:
    while True:
        nome: str = str(input(mensagem)).capitalize()
        if nome == '':
            print('o nome não pode ficar vazio.', end='')
        elif not nome.replace(' ', '').isalpha():
            print('o nome deve conter apenas letras. ', end='')
        elif len(nome) < 2:
            print('o nome precisa ter ao menos duas letras. ', end='')
        else:
            return nome


def validar_cor(mensagem) -> str:
    cores: tuple = ('azul', 'amarelo', 'vermelho', 'preto', 'verde', 'bege', 'laranja'
                    'magenta', 'ciano', 'cinza', 'roxo', 'rosa', 'branco', 'marrom',
                    'turquesa', 'marsala', 'jade', 'violeta', 'salmão', 'salmao', 'anil',
                    'gelo', 'vinho', 'ambar', 'amber', 'grafite', 'fosco', 'perola', 'abobora'
                    'esmeralda', 'ametista', 'topazio', 'madeira', 'amadeirado', 'amarelado',
                    'mogno', 'carmim', 'terroso', 'rubi', 'diamante', 'rgb', 'terracota', 'cobre',
                    'menta', 'onix', 'carmesim', 'dourado', 'prateado', 'caramelo')
    while True:
        cor_uniforme: str = str(input(mensagem)).lower().strip()
        try:
            primeira_cor = cor_uniforme.split()[0]
        except IndexError:
            print('a cor não pode ficar vazia. ', end='')
        else:
            if primeira_cor not in cores:
                print('por favor digite uma cor válida. ', end='')
            else:
                return cor_uniforme


def validar_tipo(mensagem) -> str:
    tipos_uniforme: tuple = ('escolar', 'militar', 'profissional')
    while True:
        tipo_uniforme: str = str(input(mensagem)).lower()
        if tipo_uniforme not in tipos_uniforme:
            print('o tipo do uniforme deve ser escolar, militar ou profissional. ', end='')
        else:
            return tipo_uniforme


def validar_quantidade(mensagem) -> int:
    while True:
        try:
            quantidade: int = int(input(mensagem))
        except ValueError:
            print('a quantidade deve ser um número. ', end='')
        else:
            if quantidade < 0:
                print('a quantidade não pode ser um valor negativo. ', end='')
            elif quantidade == 0:
                print('quantidade não pode ser igual a zero. ', end='')
            else:
                sleep(1)
                return quantidade


def gerar_id() -> int:
    lista: list = criar_lista()
    id_pedido: int = 0
    try:
        id_pedido: int = lista[-1]['id'] + 1
    except IndexError:
        id_pedido = 1
    finally:
        return id_pedido


def validar_id(mensagem, lista) -> int:
    mostrar_pedidos()
    while True:
        try:
            identificacao: int = int(input(mensagem))
        except ValueError:
            print('o id deve ser um número. ', end='')
        else:
            if identificacao == 0:
                return identificacao
            elif identificacao < lista[0]['id'] or identificacao > lista[-1]['id']:
                print('por favor digite um dos ids mostrados. ', end='')
            else:
                return identificacao
