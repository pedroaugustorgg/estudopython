# -*- coding: utf-8 -*-

#Apresentação e descrição
print ("TRATAMENTO DE EXCEÇÕES")
print ("Existem alguns cenários onde uma compilação indevida pode levar a um compromentimento do código, seja com travamento, interrupção ou outo tipo de adversidade. Para tratar estes cenários, precisaremos utilizar o que é conhecido como \'Tratamento de exceções\'. Segue um exemplo:\n")
print ("a = 2\nb = 0\nprint (a/b)\n\n Neste caso não vai ser possível executar este código, então nós evitamos o erro tratando a exceção da seguinte forma:\n")
print ("a = 2\nb = 0\ntry:\n\tprint (a/b)\nexcept:\n\tprint(\"Mensagem impressa para o usuário referente ao erro\")")

#Teste
print ("\nCompilação interna executada:")
a = 2
b = 0
try:
    print (a/b)
except:
    print("Não é permitida a divisão por 0 (zero)")
print ("\n---x---\n")