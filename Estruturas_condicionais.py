# -*- coding: utf-8 -*-

#Apresentação e descrição
print ("COMANDOS/FUNCOES CONDICIONAIS | ESTRUTURAS CONDICIONAIS")
print ("Spoiler: No backend deste código já há uma zona de testes para você treinar as condicionais com operações básicas\n\n")

#Funcao IF
print ("Função IF:\nRealiza testes condicionais;\nExecuta um bloco apenas SE uma determinada condição for atendida;\nAvalia se a condição é verdadeira ou não.\n\nSintaxe do IF (exemplo):\nif condição:\n\texecute_esta_linha")
print ("\n*Dentro deste código na zona de testes você consegue alterar valores atribuídos às variáveis X e Y para testar a função com condição IF. Caso o seu editor de texto não tabule automaticamente após o comando IF então você deve apertar a tecla \"TAB\" para dar o espaço correto.\n\nZona de teste IF (Compilação interna executada):")
#Teste IF
x = 1
y = 45
if x > y:
	print("x maior que y")
if y > x:
	print ("y maior que x")
#Explicacao resultado do IF compilado
print ("\nExplicaçao: Neste caso o resultado apresenta que, internamente neste código, foi atribuido um valor maior para a variável y.")
print ("\n---x---\n")

#Funcao ELSE
print ("Função ELSE:\nEstrutura condicional que é executada caso a condição do if não seja atendida")
print ("\nSintaxe do ELSE (exemplo):\nif condição:\n\texecute_esta_linha\nelse:\n\tcaso_if_falhe_execute_esta_outra_linha\n\nZona de teste ELSE (Compilação interna executada):")
#Teste ELSE
x = -5
y = -1
if y > x:
	if y > 0:
		print ("y maior que x e é positivo")
	else:
		print ("y maior que x e é negativo")
else:
	print ("y menor que x")
#Explicacao resultado do ELSE compilado
print ("\nExplicaçao: Neste caso o resultado apresenta que, internamente neste código, foi atribuido um valor maior para a variável y, mesmo sendo valor negativo (ex.: -1 > -5).")
print ("\n---x---\n")

#Funcao ELIF
print ("Funcao ELIF:\nUtilizado caso haja a necessidade de mais condições entre o IF e o ELSE.")
print ("\nSintaxe do ELIF (exemplo):\nif condição:\n\texecute_esta_linha0\nelif condição:\n\texecute_esta_linha1\nelse:\n\texecute_esta_linha2\n\nZona de teste ELIF (Compilação interna executada):")
#Teste ELIF
x = 4
y = 6

if x == y:
	print ("x e y são números iguais")
elif x < y:
	print ("x menor que y")
else:
	print ("x maior que y")
#Explicacao resultado do ELIF compilado
print ("\nExplicaçao: Neste caso o resultado apresenta que, internamente neste código, uma das condições (elif) implica no valor da variável x < y")
print ("\n---x---\n")