mensagens = []

class Mensagem:
    def __init__(self, conteudo):
        self._conteudo = conteudo  # protegido
        self.status = 'disponivel'

    @property
    def conteudo(self):
        return self._conteudo

    def visualizar(self):
        return f'Conteúdo: {self.conteudo}'
    
    def alternar_trava(self):
        print("Essa mensagem não pode ser trancada/destrancada.")

    def __str__(self):
        return f"[Comum] {self.status}"


class Mensagem_protegida(Mensagem):
    def __init__(self, conteudo, chave):
        super().__init__(conteudo)
        self.__chave = chave  # privado
        self._trancada = True

    @property
    def trancada(self):
        return self._trancada

    def verificar_chave(self):
        chave = input("Digite a chave: ")
        return chave == self.__chave

    def alternar_trava(self):
        if self.verificar_chave():
            self._trancada = not self._trancada
            estado = "trancada" if self._trancada else "destrancada"
            print(f"Mensagem {estado} com sucesso!")
        else:
            print("Chave incorreta!")

    def visualizar(self):
        if self.trancada:
            return f"Conteúdo: {'*' * len(self.conteudo)}"
        return f"Conteúdo: {self.conteudo}"
    
    def __str__(self):
        estado = "trancada" if self.trancada else "destrancada"
        return f"[Protegida - {estado}] {self.status}"


class Mensagem_unica(Mensagem):
    def visualizar(self):
        if self.status == 'indisponivel':
            return f"Conteúdo: {'*' * len(self.conteudo)}"
        
        self.status = 'indisponivel'
        return f"Conteúdo: {self.conteudo}"

    def __str__(self):
        return f"[Única] {self.status}"


# FUNÇÕES AUXILIARES

def solicitar_conteudo():
    return input("Digite o conteúdo da mensagem: ")

def solicitar_chave():
    return input("Digite a chave: ")


# FUNÇÕES PRINCIPAIS

def criar_mensagem(mensagens):
    print("1. Mensagem Comum\n2. Mensagem Protegida\n3. Mensagem Única")
    
    try:
        tipo = int(input("Escolha o tipo da mensagem: "))
    except ValueError:
        print("Digite um número válido!")
        return
    
    conteudo = solicitar_conteudo()
    
    if tipo == 1:
        mensagem = Mensagem(conteudo)
    elif tipo == 2:
        chave = solicitar_chave()
        mensagem = Mensagem_protegida(conteudo, chave)
    elif tipo == 3:
        mensagem = Mensagem_unica(conteudo)
    else:
        print("Opção inválida!")
        return
        
    mensagens.append(mensagem)
    print("Mensagem criada com sucesso!")


def listar_mensagens(mensagens):
    if not mensagens:
        print("Nenhuma mensagem cadastrada!")
        return
    
    print("Mensagens cadastradas:")
    for index, mensagem in enumerate(mensagens):
        print(f"{index} - {mensagem}")


def visualizar_mensagem(mensagens):
    if not mensagens:
        print("Nenhuma mensagem cadastrada!")
        return

    listar_mensagens(mensagens)
    
    try:
        indice = int(input("Digite o índice da mensagem: "))
        mensagem = mensagens[indice]
    except (ValueError, IndexError):
        print("Índice inválido!")
        return

    print(mensagem.visualizar())


def remover_mensagem(mensagens):
    if not mensagens:
        print("Nenhuma mensagem cadastrada!")
        return
    
    listar_mensagens(mensagens)

    try:
        indice = int(input("Digite o índice da mensagem: "))
        mensagens.pop(indice)
        print("Mensagem removida com sucesso!")
    except ValueError:
        print("Digite um número válido!")
    except IndexError:
        print("Índice inválido!")


def alternar_trava_mensagem(mensagens):
    if not mensagens:
        print("Nenhuma mensagem cadastrada!")
        return

    listar_mensagens(mensagens)

    try:
        indice = int(input("Digite o índice da mensagem: "))
        mensagem = mensagens[indice]
    except (ValueError, IndexError):
        print("Índice inválido!")
        return

    mensagem.alternar_trava()


# MENU PRINCIPAL

while True:
    print("\n===== MURAL DE MENSAGENS =====\n")
    print("1 - Criar mensagem")
    print("2 - Listar mensagens")
    print("3 - Visualizar mensagem")
    print("4 - Remover mensagem")
    print("5 - Trancar/Destrancar mensagem")
    print("0 - Sair\n")

    try:
        opcaoEscolhida = int(input("Escolha uma opção: "))
    except ValueError:
        print("Digite um número válido!")
        continue

    if opcaoEscolhida == 1:
        criar_mensagem(mensagens)
    elif opcaoEscolhida == 2:
        listar_mensagens(mensagens)
    elif opcaoEscolhida == 3:
        visualizar_mensagem(mensagens)
    elif opcaoEscolhida == 4:
        remover_mensagem(mensagens)
    elif opcaoEscolhida == 5:
        alternar_trava_mensagem(mensagens)
    elif opcaoEscolhida == 0:
        print("Saindo...")
        break
    else:
        print("Opção inválida!")