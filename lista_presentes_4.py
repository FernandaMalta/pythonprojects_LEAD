#!/usr/bin/env python
# coding: utf-8

# # Micro 09: Conjuntos e suas utilizações – oficina

# Este código foi escrito pela aluna Fernanda Malta para a avaliação do tópico 2.4 do curso Introdução a lógica de programação em Python.

# In[130]:


presentes = {
    'cadeira', 'cafeteira', 'caneca', 'escumadeira',
    'espanador', 'espátula', 'estante', 'faqueiro',
    'frigideira', 'funil', 'halter', 'liquidificador',
    'notebook', 'panela', 'peneira', 'playstation',
    'rádio', 'smartphone', 'sofá', 'tablet', 'teclado',
    'televisão', 'vassoura', 'webcam', 'xbox',
}

loja1 = {
    'cadeira', 'cafeteira', 'caneca', 'escumadeira', 'estante',
    'frigideira', 'funil', 'liquidificador', 'notebook', 'panela',
    'playstation', 'smartphone', 'teclado', 'televisão'}
loja2 = {
    'cafeteira', 'escumadeira', 'espanador', 'frigideira', 'funil',
    'halter', 'peneira', 'playstation', 'sofá', 'tablet', 'televisão',
    'vassoura', 'webcam', 'xbox'}
loja3 = {
    'caneca', 'escumadeira', 'espanador', 'espátula', 'estante',
    'frigideira', 'halter', 'playstation', 'rádio', 'smartphone',
    'sofá', 'teclado', 'televisão', 'vassoura', 'xbox'}
loja4 = {
    'caneca', 'escumadeira', 'espanador', 'espátula', 'estante',
    'frigideira', 'halter', 'playstation', 'rádio', 'smartphone',
    'sofá', 'teclado', 'televisão', 'vassoura', 'xbox'}

#Questão 1
questao1 = loja1 | loja2 | loja3 | loja4
print('1. Produtos oferecidos em ao menos uma loja:', '\n', questao1)

#Questão 2
questao2 = loja1 & loja2 & loja3 & loja4
print('2. Produtos oferecidos em todas as lojas:','\n', questao2)

#Questão 3
questao3 = presentes - loja1 - loja2 - loja3 - loja4
print('3. Produtos que não são encontrados em nenhuma loja:', '\n', questao3)

#Questão 4
questao4_1 = loja1 - loja2 - loja3 - loja4
questao4_2 = loja2 - loja1 - loja3 - loja4
questao4_3 = loja3 - loja1 - loja2 - loja4
questao4_4 = loja4 - loja1 - loja2 - loja3

print('4. Produtos exclusivos:',  [questao4_1, questao4_2, questao4_3, questao4_4])

#Questão 5
comb1 = loja1 | loja2
comb2 = loja1 | loja3
comb3 = loja1 | loja4
comb4 = loja2 | loja3
comb5 = loja2 | loja4
comb6 = loja3 | loja4

melhor_dupla = len(comb1)

if len(comb2) > melhor_dupla:
    melhor_dupla = len(comb2)
if len(comb3) > melhor_dupla:
    melhor_dupla = len(comb3)
if len(comb4) > melhor_dupla:
    melhor_dupla = len(comb4)
if len(comb5) > melhor_dupla:
    melhor_dupla = len(comb5)
if len(comb6) > melhor_dupla:
    melhor_dupla = len(comb6)

print('5. Melhor dupla possui', melhor_dupla, 'itens.')

