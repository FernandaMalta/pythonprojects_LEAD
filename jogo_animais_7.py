#!/usr/bin/env python
# coding: utf-8

# # Oficina Microlearning 12

# ##### Este código foi escrito pela aluna Fernanda Malta para a avaliação do tópico 3.2 do curso Introdução a lógica de programação em Python.

# In[34]:


class Animal:
    def __init__(self, nome = 'Gato', especie = 'Felis catus', fome = 10):
        self.nome = nome
        self.especie = especie
        self.fome = fome

    def __str__(self):
        return '\nO estado atual do seu bichinho é - Fome: {}'.format(self.fome)
    
    def comer(self, comida_dada):
        self.fome -= comida_dada 
        if self.fome < comida_dada:
            self.fome = 0
            print('Isso parece delicioso, mas estou saciado! :/')
            
    def andar(self):
        self.fome += 1
    
    def evento(self, acao):
        if acao == "alimentar":
            comida_dada = int(input('Adicione as unidades de comida que quer oferecer ao seu animal: '))
            self.comer(comida_dada)
        if acao == "andar":
            self.andar()
        elif acao == "estado atual":
            self.__str__()
            


# In[36]:


pet = Animal()

def main():
    
    print('Olá! Eu me chamo {}, sou da espécie {} e fui escolhido como o seu pet! :3'.format(pet.nome, pet.especie))
    votar = ""
    while not votar in ["1", "2", "3", "4"]:
        votar = input("""
                            1. Alimentar
                            2. Andar
                            3. Estado atual
                            4. Finalizar Execução
                             
                             """)
        if votar == "1":
            pet.evento("alimentar")
            print(pet.__str__())

        
        elif votar == "2":
            pet.evento("andar")
            print(pet.__str__())

        elif votar == "3":
            pet.evento("estado atual")
            print(pet.__str__())

        elif votar == "4":
            pet.evento("")

            
            
main()

