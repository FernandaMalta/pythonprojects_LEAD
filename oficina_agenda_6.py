#!/usr/bin/env python
# coding: utf-8

# # Oficina Microlearning 11

# ##### Este código foi escrito pela aluna Fernanda Malta para a avaliação do tópico 3.1 do curso Introdução a lógica de programação em Python.

# In[63]:


agenda = [

  ((2020, 1, 13), (11, 50), 'Renovar identidade'),

  ((2020, 1, 15), (16, 30), 'Fazer compras'),

  ((2020, 1, 25), (8, 45), 'Autenticar documentos'),

  ((2020, 2, 29), (14, 15), 'Prestar concurso'),

  ((2020, 3, 15), (17, 50), 'Buscar bolo pro aniversário da vovó'),

  ((2020, 3, 17), (13, 20), 'Consulta de revisão com dentista')]


# In[184]:


def imprimir_eventos(eventos, de_data=(1, 1, 1), ate_data=(9999, 12, 31)):
    """Retorna os eventos da agenda de acordo com a data estipulada."""
    for i in eventos:            
        datas = de_data
        datas_2 = ate_data
        if datas <= i[0] and datas_2 >= i[0]:
            print(formatar_data(i[0][0], i[0][1], i[0][2]) + ' - ' + formatar_hora(i[1][0], i[1][1]) + ': ' + i[2])
               
    
def zero_esq(x, n): #transforma o número x em uma string de comprimento n
    xs = str(x)
    return '0' * (n - len(xs)) + xs #adicionando 0 a esquerda para segurar o tamanho
 
def formatar_data(ano, mes, dia): #toma parâmetros numéricos e retorna uma string com a representação de uma data
    """Retorna uma data no formato dia/mês/ano"""
    
    meses = ('jan', 'fev', 'mar', 'abr', 'mai', 'jun',
             'jul', 'ago', 'set', 'out', 'nov', 'dez' )
    mes_extenso = meses[mes-1]
    
    return (zero_esq(dia, 2) 
    + '/' + (mes_extenso)
    + '/' + zero_esq(ano, 4)) 


def formatar_hora(hora, minuto):
    """Retorna o horário no formato hora:minuto"""
    
    return (zero_esq(hora, 2)
    + ':' + zero_esq(minuto, 2))

imprimir_eventos(agenda, ate_data = (2020, 3, 15))

