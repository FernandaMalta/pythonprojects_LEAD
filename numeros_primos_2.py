#!/usr/bin/env python
# coding: utf-8

# Este código foi escrito pela aluna Fernanda Malta para a avaliação do tópico 1.5 do curso Introdução a lógica de programação em Python.

# # Números Primos

# In[1]:


for n_primo in range (2, 101):     
   
    for i in range(2, n_primo):
        if (n_primo % i) == 0:
            break
    
    else:
        print('Os números ' + str(n_primo) + ' é primo!')

