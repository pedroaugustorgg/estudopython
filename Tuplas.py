# -*- coding: utf-8 -*-

#Apresentação e descrição
print ("TUPLAS / TUPLES")
print ("\nAs Tuplas são bem semelhantes às listas, a principal diferença entre elas é que a lista é definida entre colchetes \"[]\" e a tupla é difinida entre parênteses \"()\", além disso a tupla é imutável (não sendo possível a utilização do método append por exemplo). Segue um exemplo de sintaxe da Tupla:")
print ("Numérica: n = (1, 2, 3, 4, 5)\nTipos variados: t = (\"one\", 123, 1.2, [1, 2, 3])")

#Teste1 = Tupla com elementos variados
print ("\nCompilação interna executada:")
t = ("one", 2, 123, 2, 1.2, [1, 2, 3], 2)
print (t)
#Explicacao resultado do Teste1 compilado
print ("\nExplicação: Neste caso acima nós temos um print com uma tupla composta por string, número inteiro, numero float e uma lista respectivamente em cada elemento")
print ("\n---x---\n")

#Teste2 = Tupla com identificação de índice específico
print ("Exemplo de print com identificação de índice específico:\nprint (t.index(1.2))")
print ("\nCompilação interna executada:")
print (t[4])
#Explicacao resultado do Teste2 compilado
print ("\nExplicação: Neste caso acima nós temos um print com ao elemento referente ao índice \'4\' que eu chamei no código.")
print ("\n---x---\n")

#Teste3 = Tupla com identificação de elemento chamando o índice
print ("Exemplo de print com identificação de elemento chamando o índice:\nprint (t.index(1.2))")
print ("\nCompilação interna executada:")
print (t.index(1.2))
#Explicacao resultado do Teste3 compilado
print ("\nExplicação: Neste caso acima nós temos um print com ao índice referente ao elemento \'1.2\' que eu chamei no código.")
print ("\n---x---\n")

#Teste4 = Tupla com identificação da quantidade de elementos iguais dentro dela
print ("Exemplo do método COUNT aplicado em uma tupla. Segue a sintaxe:\nprint t.count\nprint (t.index(1.2))")
print ("\nCompilação interna executada:")
print (t.count(2))
#Explicacao resultado do Teste4 compilado
print ("\nExplicação: Neste caso acima nós temos um print com o número de vezes que o elemento \'2\' está presente dentro da tupla t")
print ("\n---x---\n")