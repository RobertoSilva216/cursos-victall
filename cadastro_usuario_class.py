import os

# Função para limpar o console
def limpar_console():
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Linux e MacOS
        os.system('clear')

# Classe Usuario
class Usuario:
    def __init__(self, nome, email, idade):
        self.nome = nome
        self.email = email
        self.idade = idade

    def exibir_dados(self):
        print(f"\nNome: {self.nome}")
        print(f"Email: {self.email}")
        print(f"Idade: {self.idade} anos")

    def eh_maior_de_idade(self):
        return self.idade >= 18

# Classe SistemaCadastro
class SistemaCadastro:
    def __init__(self):
        self.usuarios = []

    # Método para adicionar usuário à lista
    def adicionar_usuario(self):
        nome = input("Digite o nome: ")
        email = input("Digite o email: ")
        idade = int(input("Digite a idade: "))
        limpar_console()  # Limpa o console antes de mostrar a mensagem de sucesso
        novo_usuario = Usuario(nome, email, idade)
        self.usuarios.append(novo_usuario)
        print(f"\nUsuário {nome} adicionado com sucesso!")

    # Método para exibir usuários cadastrados
    def exibir_usuarios(self):
        limpar_console()
        if not self.usuarios:
            print("\nNenhum usuário cadastrado.")
        else:
            print("\nLista de Usuários Cadastrados:")
            for usuario in self.usuarios:
                usuario.exibir_dados()

    # Método para verificar se os usuários são maiores de idade
    def verificar_maioridade(self):
        limpar_console()
        for usuario in self.usuarios:
            if usuario.eh_maior_de_idade():
                print(f"\n{usuario.nome} é maior de idade.")
            else:
                print(f"\n{usuario.nome} é menor de idade.")


# Função principal para executar o sistema
def main():
    sistema = SistemaCadastro()

    while True:
        print("\n=== Sistema de Cadastro ===")
        print("1. Adicionar Usuário")
        print("2. Exibir Usuários")
        print("3. Verificar Maioridade")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            sistema.adicionar_usuario()  # Chamando o método da classe
        elif opcao == "2":
            sistema.exibir_usuarios()
        elif opcao == "3":
            sistema.verificar_maioridade()
        elif opcao == "4":
            limpar_console()
            print("Saindo do sistema. Até logo!")
            break
        else:
            limpar_console()
            print("Opção inválida. Tente novamente.")


# Executa o programa
if __name__ == "__main__":
    main()
