# -*- coding: utf-8 -*-
print ("COMANDOS DE REPETIÇÃO / ESTRUTURAS DE REPETIÇÃO\n")
print ("Spoiler: No backend deste código já há uma zona de testes para você treinar as condicionais com operações básicas\n\n")

#Comando WHILE
print ("Comando WHILE:\nUtilizado para criar laços de repetição (estruturas de repetição) e repetem um trecho do código ENQUANTO uma condição avaliada for verdadeira. No teste prático é mais fácio de compreender a condição \"while\".")
print ("\nSintaxe do WHILE (exemplo):\nwhile condição:\n 	execute_esta_linha\n 	execute_esta_linha1\n*Muito cuidado para não acabar criando uma compilação infinita para não travar a máquina em questão. É por isso que foi colocado o \"x = x+1\" após o print (evitando o aparecimento do número \"1\" eternamente.\n\nZona de teste WHILE:")

#Teste WHILE
x = 1
while x <= 10:
	print(x)
	x = x+3

#Comando FOR
print ("Comando for:\nUtilizado para percorrer um conjunto de laços de repetição (estruturas de repetição) pré-estabelecidos. No teste prático é mais fácil de compreender a condição \"for\".")
print ("\nSintaxe do FOR (exemplo):\nfor i in range(0,5):\n	print i\n\nZona de teste WHILE:")

#Teste FOR
lista1 = [1,2,3,4,5]
lista2 = ["ola","mundo","!"]
lista3 = [0,"ola","biscoito","bolacha",9.99,True]

for i in lista2:
	print (i)