#!/usr/bin/env python
# coding: utf-8

# # Oficina Microlearning 7

# Este código foi escrito pela aluna Fernanda Malta para a avaliação do tópico 2.2 do curso Introdução a lógica de programação em Python.

# In[93]:


cursos = [
  'Engenharia de Software',
  'Python para Data Science',
  'Introdução a Java'
]

respostas = [1, 2, 0, 1, 1, 1, 1, 0, 0, 2, 2, 0, 1, 1,
  1, 1, 2, 0, 1, 1, 0, 1, 0, 2, 1, 1, 0, 2,
  2, 1, 0, 1, 1, 0, 0, 0, 1, 1, 2, 1
]

total_eng_soft = respostas.count(0)
porcentagem_eng_soft = ((total_eng_soft)/(len(respostas))) * 100
print('Há', total_eng_soft, 'votos para cursar', cursos[0], 'representando', 
porcentagem_eng_soft, '% dos votos.')

total_ds = respostas.count(1)
porcentagem_ds = ((total_ds)/(len(respostas))) * 100
print('Há', total_ds, 'votos para cursar', cursos[1], 'representando', 
porcentagem_ds, '% dos votos.')

total_java = respostas.count(2)
porcentagem_java = ((total_java)/(len(respostas))) * 100
print('Há', total_java, 'votos para cursar', cursos[2], 'representando',
porcentagem_java, '% dos votos')

mais_votado = 0
porcentagem_final = porcentagem_eng_soft

if porcentagem_ds > porcentagem_final:
    mais_votado = 1
    porcentagem_final = porcentagem_ds
    
if porcentagem_java > porcentagem_final:
    mais_votado = 2
    porcentagem_final = porcentagem_java
    
print('Portanto, o curso mais votado foi:', cursos[mais_votado])

