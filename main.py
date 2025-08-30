from utils import definir_tabela, inserir_dados, deleter_dados, atualizar_preco, listar_itens 

def menu():
    print("Menu de Opções:")
    print("1. Adicionar Item")
    print("2. Remover Item")
    print("3. Atualizar Item")
    print("4. Listar Itens")
    print("5. Sair")
    escolha = input("Escolha uma opção (1-5): ")
    return escolha

def main():
    definir_tabela() # Cria a tabela se não existir
    while True:
        escolha = menu()
        if escolha == '1':
            nome = input("Digite o nome do item: ")
            preco = float(input("Digite o preço do item: "))
            inserir_dados(nome, preco)
            print(f"Item '{nome}' adicionado com sucesso.")
        elif escolha == '2':
            nome = input("Digite o nome do item a ser removido: ")
            deleter_dados(nome)
            print(f"Item '{nome}' removido com sucesso.")
        elif escolha == '3':
            nome = input("Digite o nome do item a ser atualizado: ")
            novo_preco = float(input("Digite o novo preço do item: "))
            atualizar_preco(nome, novo_preco)
            print(f"Item '{nome}' atualizado com sucesso.")
        elif escolha == '4':
            listar_itens()
        elif escolha == '5':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()