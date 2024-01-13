# -*- coding: utf-8 -*-
print ("STRINGS | Um tipo de dado que armazena coleções de caracteres (texto)\nObs.: Em Python, strings são objetos (é possível aplicar métodos à elas)\n")
print ("São declaradas entre aspas. Segue os exemplos:\n")
print ("var1 = 1\nvar2 = \"2\"\n")
print ("Neste exemplo acima var1 é um numeral, enquanto var2 é uma string")
print ("\n---x---\n")

#CONCATENACAO DE STRINGS
print ("[CONCATENAÇÃO DE STRINGS] Também existe a concatenação de strings, que ocorre quando duas variáveis do tipo String são \"somadas\", segue um exemplo:\n")
print ("Sintaxe de strings concatenadas:\nvariavel_1 = \"Ola, \"\nvariavel_2 = \"mundo!\"")
#Teste1
print ("\nCompilação interna executada:")
a = "Ola, "
b = "mundo!"
concatenar = a + b
print ("concatenar = variavel_1 + variavel_2 | Isso resultou em: ")
print (concatenar)
#Explicacao resultado do Teste1 compilado
print ("\nExplicaçao: Neste caso os elementos concatenados estão sendo impressos na tela (todos na mesma linha), onde os valores atribuidos são os mesmos utilizados na sintaxe apresentada anteriormente")
print ("\n---x---\n")

#Funcao LEN
print ("[FUNÇÃO LEN] Curiosidade: Existe uma funcao LEN que é útil para contagem de caracteres, pode ser útil quando utilizase variáveis do tipo STRING, segue um exemplo:\n")
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
print ("\n---x---\n")

#Navegando pelo Indice
print ("[NAVEGAÇÃO POR ÍNDICE] Também é possível navegar entre índices, que é basicamente escolher qual elemento você deseja setar dentre os que estão disponibilizados nas strings. Segue um exemplo:\n")
print ("Navegando entre os índices/elementos da string alocada na variável x. \nSintaxe:\nprint(x[0])\nprint(x[1])\nprint(x[2])\nprint(x[3])\nprint(x[4])")
#Teste3
print ("\nCompilação interna executada:")
print (x[0])
print (x[1])
print (x[2])
print (x[3])
print (x[4])
#Explicacao resultado do Teste3 compilado
print ("\nExplicação: Neste caso, cada linha está sendo impresso na tela um endereço específico que foi setado no código.")
print ("\n---x---\n")

#Imprimindo apenas parte de uma String
print ("[IMPRESSAO PARCIAL DE STRING] Do mesmo modo, é possível imprimir apenas uma parte de uma string. Para isso, será necessário colocar o intervalo do índices dentro do print. Segue um exemplo\n")
print ("Sintaxe:\n print(concatenar[0:14])")
#Teste4
print ("\nCompilação interna executada:")
print (concatenar[0:8])
#Explicacao resultado do Teste4 compilado
print ("\nExplicação: Acima podemos perceber que o intervalo do primeiro indice [0] até o [8] foram impressos na mesma linha.")
print ("\n---x---\n")

#[Utilizando método nas strings (1)] Alternando entre maiúsculo e minúsculo
print ("[APLICANDO MÉTODO EM STRINGS - upper e lower] Como mencionado no início deste arquivo sobre strings, estas são objetos e, consequentemente, é possível aplicar métodos a elas.\n")
print ("Segue um exemplo de aplicação dos métodos \"lower\" e \"upper\"utilizando as variáveis x e y já presentes no código para alternarmos os caracteres presentes nas strings entre caixa alta e baixa (minúsculo/maiúsculo).")
print ("\nSintaxe:\nprint (concatenar.lower())\nprint (concatenar.upper())")
#Teste5
print ("\nCompilação interna executada:")
print (concatenar.lower())
print (concatenar.upper())
print ("\nExplicação: Neste caso as variáveis permanecem inalteradas e, caso você queira atribuir às variáveis estes métodos, você precisará atribuir no código antes do print, da seguinte forma:\n")
print ("Sintaxe:\nconcatenar = concatenar.upper()\nprint (concatenar)")
#Teste5.1
print ("\nCompilação interna executada:")
concatenar = concatenar.upper()
print (concatenar)
print ("\nExplicação: Agora tudo o que chamar a variável \"concatenar\" daqui para frente irá considerar esta conversão de todos os caracteres para maiúsculo")
print ("\n---x---\n")

#[Utilizando método nas strings (2)] Removendo espaço e caracteres especiais
print ("[APLICANDO MÉTODO EM STRINGS - strip] Removendo espaço em branco ou caracteres especiais no inicio/fim de uma string\nObs.: Necessariamente precisa estar no inicio ou no fim, caso contrário não funcionará com este método")
print ("Supondo que existe um \" \" ou até mesmo um \"\\n\" que você precisa que seja ignorado pois não pode remover do código. Neste caso ficaria assim, segue a sintaxe:\n")
print ("concatenar = x + y + z + \"\\n\"\nprint (concatenar.strip())")
#Teste6
print ("\nCompilação interna executada:")
nsc = "\n" + x + z
print (nsc.strip())
print ("\nExplicação: Perceba que foi impresso sem que houvesse o pulo de linha, mesmo o \"\\n\" estando como primeiro elemento da variável \"nsc\"")
print ("\n---x---\n")

#[Utilizando método nas strings (3)] Convertendo sequencia em uma lista
print ("[APLICANDO MÉTODO EM STRINGS - split] Convertendo uma string em uma lista\n")
print ("Caso você queira transformar uma única string em uma lista com vários elementos, segue um exemplo\n")
print ("Sintaxe:\nminha_string = \"O rato roeu a roupa do rei de Roma\"\nminha_lista = minha_string.split(" ")\nprint(minha_lista)")
#Teste7
print ("\nCompilação interna executada:")
minha_string = "O rato roeu a roupa do rei de Roma"
minha_lista = minha_string.split(" ")
print(minha_lista)
print ("\nExplicação: Verificamos que a string foi convertida em uma lista onde os índices foram separados pelo espaço \" \"\nObs.: É case sentitive, ou seja, caso você escolha por exemplo o caractere \"r\" como delimitador do split, o caractere \"R\" será desconsiderado\n")
print ("\n---x---\n")

#[Utilizando método nas strings (4)] Efetuando buscas dentro de listas
print ("[APLICANDO MÉTODO EM STRINGS - find] Efetuando uma busca em uma lista\n")
print ("Após de converter a string é lista, é possível efeturar uma busca dentro da lista criada, segue um exemplo\n")
print ("Sintaxe:\nbusca = minha_string.find(\"rei\")\nprint (busca)")
#Teste8
print ("\nCompilação interna executada:")
busca = minha_string.find("rei")
print (busca)
print ("\nExplicação: O que nos foi retornado é que o elemento da lista \"rei\" está alocado a partir do endereço 23.\nQual a utilidade disso? Você pode, por exemplo, solicitar que seja impresso apenas o que tem na lista após este endereço, segue o exemplo\n")
#Teste8.1
print ("Sintaxe:\nprint (minha_string[busca:])")
print ("\nCompilação interna executada:")
print (minha_string[busca:])
print ("\nExplicação: Neste caso, acima foi impresso o intervalo entre a variável \"busca\" (que se encontra no endereço 23) e o final da string \"minha_string\", uma vez que não foi delimitado um fim no intervalo após o \":\".")
print ("\n---x---\n")

#[Utilizando método nas strings (5)] Substituindo partes de uma string
print ("[APLICANDO MÉTODO EM STRINGS - replace] Substituindo partes de uma string\n")
print ("Para subistituir partes de uma string/lista é bem simples, basta utilizar o método \"replace\", segue\n")
print ("Sintaxe:\nminha_string = minha_string.replace(\"o rei\", \"a rainha\")\nprint (minha_string)")
#Teste9
print ("\nCompilação interna executada:")
minha_string = minha_string.replace("o rei", "a rainha")
print (minha_string)
print ("\nExplicação: O método replace no caso acima substituiu o intervalo \"o rei\" para \"a rainha\" no exemplo, que resultou na impressão já com a subtituição realizada na string \"minha_string\"")
print ("\n---x---\n")