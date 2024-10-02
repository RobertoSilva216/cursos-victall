# Função para exibir o menu de opções
def exibir_menu():
    print("\n--- Gerenciador de Tarefas ---")
    print("1. Adicionar Tarefa")
    print("2. Listar Tarefas")
    print("3. Marcar Tarefa como Concluída")
    print("4. Remover Tarefa")
    print("5. Sair")

# Função para adicionar uma nova tarefa
def adicionar_tarefa():
    tarefa = input("Digite a tarefa: ")
    with open('tarefas.txt', 'a') as arquivo:
        arquivo.write(f'{tarefa} | Pendente\n')
    print("Tarefa adicionada com sucesso!")

# Função para listar todas as tarefas
def listar_tarefas():
    try:
        with open('tarefas.txt', 'r') as arquivo:
            tarefas = arquivo.readlines()
            if not tarefas:
                print("Nenhuma tarefa cadastrada.")
            else:
                print("\n--- Tarefas ---")
                for i, tarefa in enumerate(tarefas, 1):
                    print(f"{i}. {tarefa.strip()}")
    except FileNotFoundError:
        print("Nenhuma tarefa encontrada. O arquivo será criado automaticamente ao adicionar uma tarefa.")

# Função para marcar uma tarefa como concluída
def marcar_tarefa_concluida():
    listar_tarefas()
    numero_tarefa = int(input("\nDigite o número da tarefa que deseja marcar como concluída: "))
    
    with open('tarefas.txt', 'r') as arquivo:
        tarefas = arquivo.readlines()
    
    if 0 < numero_tarefa <= len(tarefas):
        tarefa = tarefas[numero_tarefa - 1].split(' | ')
        tarefa[1] = "Concluída\n"
        tarefas[numero_tarefa - 1] = ' | '.join(tarefa)
        
        with open('tarefas.txt', 'w') as arquivo:
            arquivo.writelines(tarefas)
        print("Tarefa marcada como concluída.")
    else:
        print("Número de tarefa inválido.")

# Função para remover uma tarefa
def remover_tarefa():
    listar_tarefas()
    numero_tarefa = int(input("\nDigite o número da tarefa que deseja remover: "))
    
    with open('tarefas.txt', 'r') as arquivo:
        tarefas = arquivo.readlines()

    if 0 < numero_tarefa <= len(tarefas):
        tarefas.pop(numero_tarefa - 1)
        with open('tarefas.txt', 'w') as arquivo:
            arquivo.writelines(tarefas)
        print("Tarefa removida com sucesso.")
    else:
        print("Número de tarefa inválido.")

# Função principal que executa o programa
while True:
    exibir_menu()
    opcao = input("Escolha uma opção: ")
    
    if opcao == '1':
        adicionar_tarefa()
    elif opcao == '2':
        listar_tarefas()
    elif opcao == '3':
        marcar_tarefa_concluida()
    elif opcao == '4':
        remover_tarefa()
    elif opcao == '5':
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")

