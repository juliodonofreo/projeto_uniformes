from consultas import criar_lista, mostrar_pedidos
from rich.table import Table
from rich.console import Console
from rich import print
from time import sleep


console = Console()
tabela_menu = Table(title='[green]Suup! Bem vindo![/]')


# Limpar a tela
def clr():
    print("\n" * 100)


# Tabela do menu
def tabelaMenu():
    # Colunas da tabela
    tabela_menu.add_column("", style="bold")
    tabela_menu.add_column("[italic]Como posso ajudá-lo?[/]", style="bold blue")

    # Linhas da tabela
    tabela_menu.add_row("1", "Cadastrar pedido")
    tabela_menu.add_row("2", "Mostrar todos os pedidos")
    tabela_menu.add_row("3", "Consulta individual por ID")
    tabela_menu.add_row("4", "Consulta por nome")
    tabela_menu.add_row("5", "Editar pedido")
    tabela_menu.add_row("6", "Deletar pedido")
    tabela_menu.add_row("0", "Sair")


# Menu principal
def menu() -> int:

    while True:
        # Validação da entrada do código do Menu
        try:
            console.print(tabela_menu, "[bold]Escolha uma opção[/]: ", end="")
            funcao: int = int(input())
            # Caso a entrada digitada for menor que 0 ou maior que 6
            if funcao < 0 or funcao > 6:
                clr()
                print('[red]Por favor, digite um dos valores mencionados.[/] ')
                sleep(2)
                clr()
            else:
                return funcao
        # Caso a entrada digitada não seja um número
        except ValueError:
            clr()
            print('[red]Por favor digite um número inteiro.[/]')
            sleep(2)
            clr()


# Validação da entrada de nome
def validar_nome(mensagem) -> str:
    while True:
        # Converte a primeira letra do nome para maiúscula
        nome: str = str(input(mensagem)).capitalize()
        # Caso a entrada digitada esteja vazia
        if nome == '':
            clr()
            print('[red]O nome não pode ficar vazio.[/]')
            sleep(1)
        # Caso a entrada digitada não contenha apenas letras
        elif not nome.replace(' ', '').isalpha():
            clr()
            print('[red]O nome deve conter apenas letras.[/]')
            sleep(1)
        # Caso a entrada digitada contenha menos que dois caracteres
        elif len(nome) < 2:
            clr()
            print('[red]O nome precisa ter ao menos duas letras.[/]')
            sleep(1)
        else:
            return nome


# Validação da entrada de cor
def validar_cor(mensagem) -> str:
    # Tupla de cores disponíveis para a entrada
    cores: tuple = ('azul', 'amarelo', 'vermelho', 'preto', 'verde', 'bege', 'laranja',
                    'magenta', 'ciano', 'cinza', 'roxo', 'rosa', 'branco', 'marrom',
                    'turquesa', 'marsala', 'jade', 'violeta', 'salmão', 'salmao', 'anil',
                    'gelo', 'vinho', 'ambar', 'amber', 'grafite', 'fosco', 'perola', 'abobora'
                    'esmeralda', 'ametista', 'topazio', 'madeira', 'amadeirado', 'amarelado',
                    'mogno', 'carmim', 'terroso', 'rubi', 'diamante', 'rgb', 'terracota', 'cobre',
                    'menta', 'onix', 'carmesim', 'dourado', 'prateado', 'caramelo')
    while True:
        # Converte o valor da cor para minúsculo e retira os espaços em branco
        cor_uniforme: str = str(input(mensagem)).lower().strip()
        # Recebe apenas o primeiro valor digitado
        try:
            primeira_cor = cor_uniforme.split()[0]
        # Caso a entrada digitada esteja vazia
        except IndexError:
            clr()
            print('[red]A cor não pode ficar vazia.[/]')
            sleep(1)
        # Caso a entrada digitada esteja fora da tupla de cores possíveis
        else:
            if primeira_cor not in cores:
                clr()
                print('[red]Por favor digite uma cor válida.[/]')
                sleep(1)
            else:
                return cor_uniforme


# Validação do tipo de uniforme
def validar_tipo(mensagem) -> str:
    # Tupla de uniformes dispoíveis para a entrada
    tipos_uniforme: tuple = ('escolar', 'militar', 'industrial', 'esportivo')
    while True:
        # Converte o valor do uniforme para minúsculo
        tipo_uniforme: str = str(input(mensagem)).lower()
        # Caso a entrada digitada esteja fora da tupla de uniformes disponíveis
        if tipo_uniforme not in tipos_uniforme:
            clr()
            print('[red]O tipo do uniforme deve ser Escolar, Militar, Industrial ou Esportivo.[/]')
            sleep(1)
        else:
            return tipo_uniforme


# Validação da quantidade de uniformes
def validar_quantidade(mensagem) -> int:
    while True:
        # Converte o valor da quantidade de uniformes em número inteiro
        try:
            quantidade: int = int(input(mensagem))
        # Caso a entrada digitada não seja um número
        except ValueError:
            clr()
            print('[red]A quantidade deve ser um número.[/]')
            sleep(1)
        # Caso a entrada digitada seja menor que zero
        else:
            if quantidade < 0:
                clr()
                print('[red]A quantidade não pode ser um valor negativo.[/]')
                sleep(1)
            # Caso que a entrada digitada seja zero
            elif quantidade == 0:
                clr()
                print('[red]Quantidade não pode ser igual a zero.[/]')
                sleep(1)
            else:
                sleep(1)
                return quantidade


# Gerador de ID
def gerar_id() -> int:
    lista: list = criar_lista()
    id_pedido: int = 0
    try:
        id_pedido: int = lista[-1]['id'] + 1
    except IndexError:
        id_pedido = 1
    finally:
        return id_pedido


# Valição do ID
def validar_id(mensagem, lista) -> int:
    mostrar_pedidos()
    while True:
        # Converte o valor do ID para número inteiro
        try:
            identificacao: int = int(input(mensagem))
        # Caso o valor do ID não for um número
        except ValueError:
            clr()
            print('[red]O ID deve ser um número.[/]')
            sleep(1)
        else:
            if identificacao == 0:
                return identificacao
            # Caso o valor do ID esteja fora dos parâmetros indicados
            elif identificacao < lista[0]['id'] or identificacao > lista[-1]['id']:
                clr()
                print('[red]Por favor digite um dos IDs mostrados.[/]')
                sleep(1)
            else:
                return identificacao
