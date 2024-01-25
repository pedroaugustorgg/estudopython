# -*- coding: utf-8 -*-
import random

#Apresentação e descrição
print ("Módulo \"Random\" para gerar dados aleatórios.")
print ("\nPara utilizar o módulo em questão, você vai precisar inserir a linha \"import random\" no início do código. Com isso vai ser possível utilizar diversos métodos que geram números aleatórios. Segue um exemplo com a sintaxe:\n")
print ("numero = random.randint(0,20)\nprint(numero)")

#Teste1
print ("\nCompilação interna executada:")
numero = random.randint(0,20)
print(numero)
print ("\n---x---\n")

#Teste2
print ("Também é possível escolher um número aleatório presente em uma lista. Para isso precisaremos utilizar o método \'choice\', como este exemplo abaixo:\n")
print ("lista = [6,80,35,2,11]\nnumero = random.choice(lista)\nprint(numero)")
print ("\nCompilação interna executada:")
lista = [6,80,35,2,11]
numero = random.choice(lista)
print(numero)
print ("\n---x---\n")