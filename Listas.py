# -*- coding: utf-8 -*-

#Apresentação e descrição
print ("Listas / Lists")

#Funcao OPEN
print ("\nAs listas representam conjuntos de dados, podendo ser basicamente de dois tipos:")
print ("Numérica: [1, 2, 3, 4, 5]\nStrings: [\"bola\",\"sapato\",\"chuva\"]")

#Sintaxe
print ("\nAbaixo nós temos um exemplo prático para identificarmos a sintaxe e o resultado da compilação:\n")
print ("minha_lista = [\"abacaxi\",\"melancia\",\"abacate\"\nminha_lista_2 = [1,2,3,4,5]\nprint (minha_lista_1,\"\\n\",minha_lista_2)\nprint (minha_lista1[2])")

#Teste1
print ("\nCompilação interna executada:")
minha_lista1 = ["nome","cpf","idade","peso"]
minha_lista2 = [1,2,3,4,5]
print (minha_lista1,"\n",minha_lista2)
print (minha_lista1[2])

#Explicacao resultado do Teste1 compilado
print ("\nExplicação: Neste caso acima nós temos um print com as duas listas criadas e um print seguinte com apenas um dos elementos da primeira. Para isto foi necessário setar qual lista e qual elemento seria impresso, ficando assim:\n \"print (minha_lista1[2])\"")
print ("\n---x---\n")

#Teste2
print ("Outro exemplo do uso de listas é com a utilização da função LEN, neste caso é possível verificar o tamanho (quantos elementos) de uma lista. Segue o código e seu respectivo resultado de compilação:\n")
print ("minha_lista = [\"José\",\"Thiago\",\"Pedro\"]\ntamanho = len(minha_lista)\nprint(tamanho)")
print ("\nCompilação interna executada:")
minha_lista = ["José","Thiago","Pedro"]
tamanho = len(minha_lista)
print (tamanho)
print ("\n---x---\n")