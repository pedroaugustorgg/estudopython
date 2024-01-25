# -*- coding: utf-8 -*-
from math import sqrt

#Apresentação e descrição
print ("INPUTS")
print ("Ao invés de inserir valores ou caracteres diretamente no corpo do código, é possível deixar essa tarefa para o usuário que está visualizando o código já compilado. Segue um exemplo de sintaxe com input:\n")
print ("idade = int(input(\"Digite sua idade: \"))\nif idade >= 18:\n\tprint(\"Maior de idade\")\nelif idade < 18:\n\tprint(\"Menor de idade\")")

#Teste1
print ("\nCompilação interna executada:")
while True:
    idade = int(input("Digite sua idade: "))
    
    if idade >= 18:
        print("Maior de idade")
    elif idade < 18:
        print("Menor de idade")
    print ("\n---x---\n")

    #Teste2
    print ("Exemplo2: equação matemática de segundo grau")
    print ("\nCompilação interna executada:")
    a = int(input("Digite o valor de A: "))
    b = int(input("Digite o valor de B: "))
    c = int(input("Digite o valor de C: "))
    
    delta = b**2 - 4*a*c
    
    if delta < 0:
        print("Delta negativo")
    else:
        raiz_delta = sqrt(delta)
        x1 = (-b + raiz_delta)/2*a
        x2 = (-b - raiz_delta)/2*a
    
        print("As raízes são", x1, "e", x2)
    print ("\n---x---\n")

    #Teste3
    print ("Exemplo3: Crie uma expressão numerica e veja o resultado")
    n1 = int(input("Digite o primeiro número: "))
    sinal = input("Digite o sinal: ")
    n2 = int(input("Digite o segundo número: "))
    
    if sinal == "+":
        op = n1 + n2
    
    elif sinal == "-":
        op = n1 - n2
    
    elif sinal == "/":
        op = n1 / n2
    
    elif sinal == "*":
        op = n1 * n2
    
    else:
        print("Sinal inválido.")
    
    print("\nResultado:")
    print(op)
    print ("\n---x---\n")
    
    if input('Deseja reiniciar (S/N)? ') not in ('S', 's'):
        break # se digitar qualquer coisa diferente de "s" ou "S", sai do loop