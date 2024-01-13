# -*- coding: utf-8 -*-

#Apresentação e descrição
print ("COMANDOS/FUNÇOES DE REPETIÇÃO | ESTRUTURAS DE REPETIÇÃO")
print ("Spoiler: No backend deste código já há uma zona de testes para você treinar as condicionais com operações básicas\n\n")

#Funcao WHILE
print ("Função WHILE:\nUtilizado para criar laços de repetiçao (estruturas de repetição) e repetem um trecho do código ENQUANTO uma condiçao avaliada for verdadeira. No teste prático é mais fácio de compreender a condição \"while\".")
print ("\nSintaxe do WHILE (exemplo):\nwhile condiçao:\n 	execute_esta_linha\n 	execute_esta_linha1\n*Muito cuidado para não acabar criando uma compilação infinita, isso pode resultar num erro ou até mesmo travar a máquina em questão. É por isso que foi colocado o \"x = x+1\" após o print (evitando o aparecimento do número \"1\" eternamente.\n\nZona de teste WHILE (Compilação interna executada):\n")
#Teste WHILE
x = 1
while x <= 10:
	print(x)
	x = x+3
#Explicacao resultado do WHILE compilado
print ("\nExplicaçao: Neste caso o resultado para o \"x <= 10\" está sendo impresso na tela")
print ("\n---x---\n")

#Funcao FOR
print ("\nFunção FOR:\nUtilizada para percorrer um conjunto de laços de repetição (estruturas de repetição) pré-estabelecidos. No teste prático é mais fácil de compreender a condição \"for\".")
print ("\nSintaxe do FOR (exemplo):\nfor i in range(0,5):\n	print i\n\nZona de teste WHILE (Compilação interna executada):\n")
#Teste FOR
lista1 = [1,2,3,4,5]
lista2 = ["ola","mundo","!"]
lista3 = [0,"ola","biscoito","bolacha",9.99,True]
for i in lista2:
	print (i)
#Explicacao resultado do FOR compilado
print ("\nExplicaçao: Neste caso os elementos contidos na \"lista2\" estão sendo impressos na tela (cada elemento em uma linha)")
print ("\n---x---\n")

#Funcao RANGE
print ("\nFunção RANGE:\nPerceba que no último exemplo foi utilizada a função RANGE, empregamos esta funçao para indicar um intervalo pré-estabelecido. Veremos um exemplo abaixo:")
print ("\nSintaxe do RANGE (exemplo:\nfor p in range(10):\n print p\n\nZona de teste RANGE (Compilação interna executada):\n")
#Teste RANGE
for p in range (10):
	print (p)
#Explicacao resultado do RANGE compilado
print ("\nExplicaçao: Neste caso os 10 elementos dentro do intervalo de 0 a 10 estão sendo impressos na tela\nObs.: Note que apenas foi impresso de 0 a 9, pois o Zero é considerado como um elemento desta RANGE.")
print ("\n---x---\n")