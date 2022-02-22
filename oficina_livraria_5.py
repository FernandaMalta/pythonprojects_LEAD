#!/usr/bin/env python
# coding: utf-8

# # Oficina Microlearning 10

# ##### Este código foi escrito pela aluna Fernanda Malta para a avaliação do tópico 2.5 do curso Introdução a lógica de programação em Python.

# In[124]:


#Leitura dos dados
dados_livros = {} 

dados_livros['Livro 01'] = {'titulo': 'A Guerra dos Mundos', 'genero':'Ficcao', 'subgenero':'Cientifica', 
                            'editora':'Suma', 'num_copias': 3, 'preco': 46.90}
dados_livros['Livro 02'] = {'titulo': 'Admiravel Mundo Novo', 'genero':'Ficcao', 'subgenero':'Cientifica', 
                            'editora':'Biblioteca Azul', 'num_copias': 2, 'preco': 20.80}
dados_livros['Livro 03'] = {'titulo': 'Eragon', 'genero':'Ficcao', 'subgenero':'Distópica',
                            'editora':'Rocco', 'num_copias': 8, 'preco': 29.99}
dados_livros['Livro 04'] = {'titulo': 'Orgulho e Preconceito', 'genero':'Romance', 'subgenero':'Historico',
                            'editora':'Martin Claret', 'num_copias': 1, 'preco': 27.94}
dados_livros['Livro 05'] = {'titulo': 'O Assassinato de Roger Ackroyd', 'genero':'Romance', 'subgenero':'Policial',
                            'editora':'Globo', 'num_copias': 6, 'preco': 49.90}
dados_livros['Livro 06'] = {'titulo': 'Um corpo na biblioteca', 'genero':'Romance', 'subgenero':'Policial',
                            'editora':'Livros do Brasil', 'num_copias': 2, 'preco': 14.84}


# In[127]:


#Apresentação dos dados

bibli_genero= []
bibli_subgenero = []
bibli_titulo = []

for livro in sorted(dados_livros.keys()):
    if dados_livros[livro]['genero'] not in bibli_genero:
        bibli_genero.append(dados_livros[livro]['genero'])
        print('')
        print('--- Gênero {} ---' .format(dados_livros[livro]['genero']))
        
        
        for subgenero in sorted(dados_livros.keys()):
            if dados_livros[subgenero]['subgenero'] not in bibli_subgenero:
                if dados_livros[subgenero]['genero'] == dados_livros[livro]['genero']:
                    bibli_subgenero.append(dados_livros[subgenero]['subgenero'])
                    print('')
                    print('---- Subgênero {} ----'.format(dados_livros[subgenero]['subgenero']))
                    
                    
            for titulos in sorted(dados_livros.keys()):
                if dados_livros[titulos]['titulo'] not in bibli_titulo:
                    if dados_livros[titulos]['genero'] == dados_livros[livro]['genero']:
                        if dados_livros[titulos]['subgenero'] == dados_livros[subgenero]['subgenero']:
                            bibli_titulo.append(dados_livros[titulos]['titulo'])
                            bibli_titulo.append(dados_livros[titulos]['num_copias'])
                            print('{} [{}]'.format(dados_livros[titulos]['titulo'], dados_livros[titulos]['num_copias']))
            
    

