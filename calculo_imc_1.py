#!/usr/bin/env python
# coding: utf-8

# Olá! Este código foi escrito pela aluna Fernanda Malta para resolução do exercício para cálculo do Índice de Massa Corporal (IMC). 

# # Índice de Massa Corporal (IMC) 

# In[26]:


nome_pessoa = 'Erick'
idade_pessoa = 29
peso_pessoa = 68.4
altura_pessoa = 1.78

#cálculo do IMC

altura_quadrado = altura_pessoa**2
imc = peso_pessoa / altura_quadrado

print('Nome: '+ nome_pessoa, '\nIdade: ' + str(idade_pessoa) + ' anos', '\nPeso: ' + str(peso_pessoa) +' kgs', '\nAltura: ' + str(altura_pessoa) + ' m', '\nO IMC desta pessoa é: ' + str(imc))

