# -*- coding: utf-8 -*-
print ("STRINGS | Um tipo de dado que armazena coleções de caracteres (texto)\n")
print ("São delcaradas entre aspas. Segue os exemplos:\n")
print ("var1 = 1\nvar2 = \"2\"\n")
print ("Neste exemplo acima var1 é um numeral, enquanto var2 é uma string\n")

#CONCATENACAO DE STRINGS
print ("\nTambém existe a concatenação de strings, que ocorre quando duas variáveis do tipo String são \"somadas\", segue um exemplo:\n")
print ("Sintaxe de strings concatenadas:\nvariavel_1 = \"Ola, \"\nvariavel_2 = \"mundo!\"")
#Teste1
print ("\nCompilação interna executada:")
a = "Ola, "
b = "mundo!"
concatenar = a + b
print ("concatenar = variavel_1 + variavel_2 | Isso resultou em: ")
print (concatenar)
#Explicacao resultado do Teste1 compilado
print ("\nExplicaçao: Neste caso os elementos concatenados estão sendo impressos na tela (todos na mesma linha), onde os valores atribuidos são os mesmos utilizados na sintaxe apresentada anteriormente\n")

#Funcao LEN
print ("\nCuriosidade: Existe uma funcao LEN que é útil para contagem de caracteres, pode ser útil quando utilizase variáveis do tipo STRING, segue um exemplo:\n")
print ("Sintaxe da função LEN presente em uma concatenaçao:\nx = \"Breno\"\ny = \" \"\nz = \"Pedro\"")
#Teste2
print ("\nCompilação interna executada:")
x = "Breno"
y = " "
z = "Pedro"
concatenar = x + y + z
tamanho = len(concatenar)
print ("concatenar = x + y + z\ntamanho = len(concatenar) | Isso resultou em: ")
print (tamanho)
#Explicacao resultado do Teste2 compilado
print ("\n*Importante: Perceba que o caractere vazio \" \" também foi contabilizado como um caractere e a função LEN retornou o resultado da soma de x+y+z")