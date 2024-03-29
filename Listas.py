# -*- coding: utf-8 -*-

#Apresentação e descrição
print ("LISTAS / LISTS")
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
#Explicacao resultado do Teste2 compilado
print ("\nExplicação: Neste caso acima nós temos um print com literalmente o número de elementos contidos na lista devido a utilização da função LEN")
print ("\n---x---\n")

#Teste3
print ("Também é possível adicionar elementos a lista existentes, para que isto seja possível é necessário utilizarmos a função APPEND. Segue um exemplo de sintaxe:\n")
print ("minha_lista = [\"José\",\"Thiago\",\"Pedro\"]\nminha_lista.append(\"Adriano\")\nprint(minha_lista)")
print ("\nCompilação interna executada:")
minha_lista = ["José","Thiago","Pedro"]
minha_lista.append("Adriano")
print (minha_lista)
#Explicacao resultado do Teste3 compilado
print ("\nExplicação: Neste caso acima nós adicionamos o elemento \"Adriano\" (que não estava presente na lista anteriormente) utilizando a função APPEND")
print ("\n---x---\n")

#Teste4
print ("Ainda falando de listas, é possível validar se um elemento está presente dentro de uma lista ou não, para isso será necessário utilizarmos estruturas condicionais (ex.: IF). Segue um exemplo de sintaxe:\n")
print ("minha_lista = [\"José\",\"Thiago\",\"Pedro\"]\nminha_lista.append(\"Adriano\")\nprint(minha_lista)\nif \'Adriano\' in minha_lista:\n\tprint (\"O elemento \'Adriano\' foi adicionado a sua lista\")\nelse:\n\tprint (\"Não existem elementos com esta condição na sua lista\")")
print ("\nCompilação interna executada:")
if 'Adriano' in minha_lista:
    print ("O elemento \'Adriano\' foi adicionado a sua lista")   
else:
    print ("Não existem elementos com esta condição na sua lista")
#Explicacao resultado do Teste4 compilado
print ("\nExplicação: Neste caso acima nós adicionamos uma condicional pra validar se o elemento \'Adriano\' foi adicionado a lista do exemplo anterior.")
print ("\n---x---\n")

#Teste5
print ("Uma outra possibilidade é excluir um ou mais elementos dentro de uma lista, para isto é necessário utilizarmos a função \'del\'. Segue um exemplo de sintaxe:\n")
print ("minha_lista = [\"José\",\"Thiago\",\"Pedro\"]\nminha_lista.append(\"Bruno\")\ndel minha_lista[0:3]\nprint(minha_lista)")
print ("\nCompilação interna executada:")
minha_lista.append("Bruno")
del minha_lista[0:3]
print (minha_lista)
#Explicacao resultado do Teste5 compilado
print ("\nExplicação: Neste caso acima nós apagamos os 3 primeiros elementos.\n*Obs.: Caso queira apagar a lista inteira, basta deixar o intervalo vazio, exemplo:\ndel minha_lista[:]")
print ("\n---x---\n")

#Teste6
print ("Também é possível extrair um elemento da lista, para isto é necessário utilizarmos o método \'pop\' (que extrai por padrão o último elemento de uma lista). Segue um exemplo de sintaxe:\n")
print ("minha_lista3 = [\"Moises\",\"Matheus\",\"James\"]\nminha_lista.pop()\nprint(minha_lista)")
print ("\nCompilação interna executada:")
minha_lista3 = ["Moises","Matheus","James"]
minha_lista3.pop()
print (minha_lista3)
#Explicacao resultado do Teste6 compilado
print ("\nExplicação: Neste caso acima o último elemento da lista que era \"James\" foi retirado da lista e impresso na tela a lista sem ele, caso o usuário execute novamente o mesmo método, já não irá constar o último elemento da lista atual, que no caso seria o elemento \"Matheus\". Veja o exemplo abaixo:")
print ("\nCompilação interna executada:")
minha_lista3.pop()
print (minha_lista3)
print ("\n---x---\n")

#Bonus: Ordenação de Listas
print ("ORDENAÇÃO DE LISTAS / LIST SORT")
print ("A a ordenação de listas, é possível ordenar de forma crescente ou decrescente uma lista com elementos numéricos. Segue um exemplo de sintaxe:\n")
print ("lista = [153,45,862,85,50,3,1,5,90,10,28]\nlista.sort()\nprint (lista)")
print ("\nCompilação interna executada:")
lista = [153,45,862,85,50,3,1,5,90,10,28]
lista.sort()
print (lista)
#Explicacao resultado do Teste6
print ("\nExplicação: Neste caso acima nós tínhamos uma lista com números aleatórios e conseguimos imprimir ordenado de forma crescente.\n*Obs.:Caso queira mudar a ordenação (para forma decrescente por exemplo), baste inserir no parênteses do \'sort\' (se a lista for de Strings, será ordenado alfabeticamente). Segue a sintaxe:\n")
print ("lista.sort(reverse=True)")
print ("\nCompilação interna executada:")
lista.sort(reverse=True)
print (lista)
print ("\n*Dica.: Também é possível reverter a lista antes ou após realizar a ordenação, para isso, deverá ser utilizado método REVERSE. Segue o exemplo de sintaxe:\n\nlista.reverse()\nprint (lista)")
print ("\n---x---\n")

#Python avançado: List Comprehension
print ("COMPREENSÃO DE LISTAS / LISTS COMPREHENSION")
print ("A compreensão é muito útil para utilizarmos uma espécie de \'conversão automática\' de listas já pré-existentes. Segue um exemplo de sintaxe sem utilização do \'list comprehension\':\n")
print ("a = [1, 2, 3, 4, 5]\nb = []\n\nfor i in x:\n\ty.append(i**2)\nprint(x)\nprint(y)")

#Teste7
a = [1, 2, 3, 4, 5]
b = []

for i in a:
    b.append(i**2)
print ("\nCompilação interna executada (SEM list comprehension):")
print(a)
print(b)
#Explicacao resultado do Teste7
print ("\nExplicação: Neste caso a variável \'y\' foi compreendida como o quadrado dos indices (elementos) da lista presente na variável \'x\'.")
print ("\n---x---\n")

#Teste8
print ("Agora o mesmo exemplo anterior, porém com a utilização do \'list comprehension\'. Segue:\nx = [1, 2, 3, 4, 5]\ny = [i**2 for i in x]\nz = [i for i in x if i%2==1]")
x = [1, 2, 3, 4, 5]
y = [i**2 for i in x]
z = [i for i in x if i%2==1]
print ("\nCompilação interna executada (COM list comprehension):")
print(x)
print(y)
print(z)
#Explicacao resultado do Teste8
print ("\nExplicação: Neste caso conseguimos perceber que a compreensão feita diretamente na variável \'y\' deixou o código bem mais enxuto. Além disso, nós adicionamos a variável \'z\' com a impressão apenas dos números/índices ímpares presentes na lista")
print ("\n---x---\n")

