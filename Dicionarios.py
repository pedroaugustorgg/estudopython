# -*- coding: utf-8 -*-

#Apresentação e descrição
print ("Dicionários")
print ("\nDefinição: São listas de associações compostos por uma chave e um valor correspondente. A principal diferença entre os dicionários e as Listas é que as listas possuem índices/elementos, já os dicionários possuem chaves. A forma de se inserir um dicionário do código também se difere, uma vez que é atribuido com chaves \"{}\", segue um exemplo didático:\n")

#Sintaxe
print ("Sintaxe: Utiliza os colchetes para buscar os valores. Segue um exemplo de sintaxe:\n")
print ("aminoacidos = {'ALA':'Alanina','CYS':'Cisteina'}\n print aminoacidos ['ALA']")
#Teste1
print ("Vamos realizar um teste com o seguinte código:\nmeu_dicionario = {\"A\":\"AMEIXA\", \"B\":\"BOLA\", \"C\":\"CACHORRO\"}")
print ("\nCompilação interna executada:")
meu_dicionario = {"A":"AMEIXA", "B":"BOLA", "C":"CACHORRO"}
print (meu_dicionario)
print (meu_dicionario["C"])
#Explicacao resultado do Teste1 compilado
print ("\nExplicação: Observe que, em uma lista normal nós utilizaríamos o \"print (meu_dicionario[2])\" para imprimir o terceiro índice/elemento, porém, em um dicionário nós não utilizamos e nem conseguimos imprimir por índices, sendo necessário imprimirmos o valor específico como foi feito acima (que no caso imprimiu a chave \"C\")")
print ("\n---x---\n")

#Navegando pelo dicionário
print ("É possível também navegar pelas chaves criadas utilizando o comando FOR. Segue um exemplo de sintaxe:\n")
#Teste2
print ("Vamos realizar um segundo teste com o seguinte complemento do código anterior:\n\nfor chave in meu_dicionario:\n\tprint(chave)\n\tprint(meu_dicionario[chave])")
print ("\nCompilação interna executada:")
for chave in meu_dicionario:
    print(chave)

for chave in meu_dicionario:
    print(meu_dicionario[chave])
#Explicacao resultado do Teste2 compilado
print ("\nExplicação: Neste caso foi impresso primeiro as chaves de cada e depois os respectivos valores de cada chave contida no dicionário")
print ("\n---x---\n")

#Exercitando com dicionários
print ("Para exercitar, você pode fazer uma melhoria na impressão das chaves e/ou valores impressos de dicionários.\n")
#Teste3
print ("Segue um exemplo de impressão utilizando o código anterior:\n\nfor chave in meu_dicionario:\n\tprint(chave+\"->\"+meu_dicionario[chave])")
print ("\nCompilação interna executada:")
for chave in meu_dicionario:
    print(chave+"->"+meu_dicionario[chave])
#Explicacao resultado do Teste3 compilado
print ("\nExplicação: Neste caso foi impresso tanto as chaves quanto os valores e ainda adicionamos um separador manual.")
print ("\n---x---\n")

#Funções em dicionários
print ("Também existem algums metodos que podem ser utilizados em dicionários. Segue alguns exemplos como os métodos \'items\' e \'values\'\n")
#Teste4
print ("Segue um exemplo de utilização destes métodos:\n\nfor i in meu_dicionario.items():\n\tprint(i)\nfor v in meu_dicionario.values():\n\tprint(v)")
print ("\nCompilação interna executada:")
for i in meu_dicionario.items():
    print(i)
for v in meu_dicionario.values():
    print(v)
#Explicacao resultado do Teste4 compilado
print ("\nExplicação: Neste caso a funcao \'items\' transformou as chaves e valores em itens (semelhante ao que ocorre com os índices nas listas) e a função \'values\' imprimiu apenas os valores presentes no dicionário setado.")
print ("\n*Obs.: Caso tenha interesse em imprimir apenas as chaves, basta utilizar o método \'keys\' ao invés de \'items\'.")
print ("\n---x---\n")
