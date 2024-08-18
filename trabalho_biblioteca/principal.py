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
        print("\nMenu:")
        print("1. Adicionar livro")
        print("2. Listar livros")
        print("3. Adicionar usuário")
        print("4. Emprestar livro")
        print("5. Devolver livro")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            titulo = input("Digite o título do livro: ")
            autor = input("Digite o autor do livro: ")
            adicionar_livro(titulo, autor)
            print(f'Livro "{titulo}" adicionado com sucesso!')
        elif opcao == '2':
            exibir_livros()
        elif opcao == '3':
            nome = input("Digite o nome do usuário: ")
            adicionar_usuario(nome)
            print(f'Usuário "{nome}" adicionado com sucesso!')
        elif opcao == '4':
            nome_usuario = input("Digite o nome do usuário: ")
            titulo_livro = input("Digite o título do livro: ")
            resultado = emprestar_livro(nome_usuario, titulo_livro)
            print(resultado)
        elif opcao == '5':
            titulo_livro = input("Digite o título do livro: ")
            resultado = devolver_livro(titulo_livro)
            print(resultado)
        elif opcao == '6':
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == '__main__':
    main()
