from classes.py import Livro

livro = Livro("", "", 0)

titulo = input('Qual o nome do livro a ser adicionado: ')
livro.setTitulo(titulo)

autor = input('Digite o autor desse livro: ')
livro.setAutor(autor)

ano = int(input('Digite o ano do livro: '))
livro.setAno(ano)

print('Livro: ', livro.getTitulo(), livro.getAutor(), livro.getAno(), livro.getDisponivel())
