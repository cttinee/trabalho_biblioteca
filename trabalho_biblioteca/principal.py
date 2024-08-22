from biblioteca import adicionar_livro, listar_livros, adicionar_usuario, emprestar_livro, devolver_livro

def exibir_livros():
    livros = listar_livros()
    if not livros:
        print("Nenhum livro disponível.")
    else:
        for livro in livros:
            print(f'Título: {livro["titulo"]}, Autor: {livro["autor"]}')

def main():
    while True:
        print("\n- Menu do sistema da biblioteca")
        print()
        print("1. Cadastrar usuário.")
        print("2. Adicionar livros.")
        print("3. Listar Livros.")
        print("4. Emprestar livro.")
        print("5. Devolver livro.")
        print("6. Fechar o sistema.")
        print()

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Digite o novo nome do usuário: ").lower()
            adicionar_usuario(nome)
            print(f'Usuário "{nome}" adicionado com sucesso!')
        elif opcao == '2':
            titulo = input("Digite o título do livro: ").lower()
            autor = input("Digite o autor do livro: ").lower()
            adicionar_livro(titulo, autor)
            print(f'Livro "{titulo}" adicionado com sucesso!')
        elif opcao == '3':
            exibir_livros()
        elif opcao == '4':
            nome_usuario = input("Digite o nome do usuário: ").lower()
            titulo_livro = input("Digite o título do livro: ").lower()
            resultado = emprestar_livro(nome_usuario, titulo_livro)
            print(resultado)
        elif opcao == '5':
            titulo_livro = input("Digite o título do livro: ").lower()
            resultado = devolver_livro(titulo_livro)
            print(resultado)
        elif opcao == '6':
            print("Até mais!")
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == '__main__':
    main()
