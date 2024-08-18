
dados_biblioteca = {
    "livros": [],
    "usuarios": [],
    "emprestimos": {}
}

def adicionar_livro(titulo, autor):
    """Adiciona um livro à biblioteca."""
    dados_biblioteca['livros'].append({'titulo': titulo, 'autor': autor})

def listar_livros():
    """Retorna uma lista de todos os livros disponíveis na biblioteca."""
    return dados_biblioteca['livros']

def adicionar_usuario(nome):
    """Adiciona um usuário à biblioteca."""
    dados_biblioteca['usuarios'].append({'nome': nome})

def emprestar_livro(nome_usuario, titulo_livro):
    """Empresta um livro a um usuário."""
    livro = next((l for l in dados_biblioteca['livros'] if l['titulo'] == titulo_livro), None)
    if livro and nome_usuario in [u['nome'] for u in dados_biblioteca['usuarios']]:
        if titulo_livro in dados_biblioteca['emprestimos']:
            return f'O livro "{titulo_livro}" já está emprestado.'
        else:
            dados_biblioteca['emprestimos'][titulo_livro] = nome_usuario
            return f'Livro "{titulo_livro}" emprestado a "{nome_usuario}".'
    else:
        return "Livro não encontrado ou usuário não registrado."

def devolver_livro(titulo_livro):
    """Devolve um livro emprestado."""
    if titulo_livro in dados_biblioteca['emprestimos']:
        nome_usuario = dados_biblioteca['emprestimos'].pop(titulo_livro)
        return f'Livro "{titulo_livro}" devolvido por "{nome_usuario}".'
    else:
        return f'O livro "{titulo_livro}" não está emprestado.'
