# -*- coding: utf-8 -*-
print ("COMANDOS CONDICIONAIS / ESTRUTURAS CONDICIONAIS\n")

#Comando IF
print ("Comando IF:\nRealiza testes condicionais;\nExecuta um bloco apenas SE uma determinada condição for atendida;\nAvalia se a condição é verdadeira ou não.\n\nSintaxe do IF (exemplo):\nif condição:\n 	execute_esta_linha")
print ("*Dentro deste código na zona de testes você consegue alterar valores atribuídos às variáveis X e Y para testar a função com condição IF. Caso o seu editor de texto não tabule automaticamente após o comando IF então você deve apertar a tecla \"TAB\" para dar o espaço correto.\n\nZona de teste IF:")

#Teste IF
x = 1
y = 45
if x > y:
	print("x é maior que y")
if y > x:
	print ("y é maior que x")

#Comando ELSE
print ("\n\nComando ELSE:\nEstrutura condicional que é executada caso a condição do comando if não seja atendida")
print ("\nSintaxe do ELSE (exemplo):\nif condição:\n 	execute_esta_linha\nelse:\n 	caso_if_falhe_execute_esta_outra_linha\n\nZona de teste ELSE:")

#Teste ELSE
x = -5
y = -1
if y > x:
	if y > 0:
		print ("y é maior que x e é positivo")
	else:
		print ("y é maior que x e é negativo")
else:
	print ("y é menor que x")

#Comando ELIF
print ("\n\nComando ELIF:\nUtilizado caso haja a necessidade de mais condições entre o IF e o ELSE.")
print ("\nSintaxe do ELIF (exemplo):\nif condição:\n 	execute_esta_linha0\nelif condição:\n 	execute_esta_linha1\nelse:\n 	execute_esta_linha2\n\nZona de teste ELIF:")

#Teste ELIF
x = 6
y = 4

if x == y:
	print ("x e y são números iguais")
elif x < y:
	print ("x é menor que y")
else:
	print ("x é maior que y")