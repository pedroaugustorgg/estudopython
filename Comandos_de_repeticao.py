# -*- coding: utf-8 -*-
print ("COMANDOS DE REPETIÇÃO / ESTRUTURAS DE REPETIÇÃO\n")

#Comando WHILE
print ("Comando WHILE:\nUtilizado para criar laços de repetição (estruturas de repetição) e repetem um trecho do código ENQUANTO uma condição avaliada for verdadeira. No teste prático é mais fácio de compreender a condição \"while\".")
print ("\nSintaxe do WHILE (exemplo):\nwhile condição:\n 	execute_esta_linha\n 	execute_esta_linha1\n*Muito cuidado para não acabar criando uma compilação infinita para não travar a máquina em questão. É por isso que foi colocado o \"x = x+1\" após o print (evitando o aparecimento do número \"1\" eternamente.\n\nZona de teste WHILE:")

#Teste WHILE
x = 1
while x <= 10:
	print(x)
	x = x+3

#Comando FOR
