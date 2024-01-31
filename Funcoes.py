# -*- coding: utf-8 -*-

#Apresentação e descrição
print ("FUNÇÕES")
print ("\nSpoiler: No backend deste código já há uma zona de testes para você treinar as funcoes apresentadas.\n")
print ("Em Python são definidas pela palavra \"def\", ficando com a seguinte estrutura:\n")
print ("def NOME (parâmetros)\ncomandos\n\nCHAMADA:\nNOME(ARGUMENTOS)\n\nSegue um exemplo de sintaxe:\n")

#Teste1
print ("def soma(x, y):\n\treturn x+y\n\ns = soma(2,3)\nprint(s)\n\nZona de teste FUNCAO (Compilação interna executada):\n")
def soma(x, y):
        return x+y

s = soma(2,3)
print (s)
print ("\nExplicaçao: Perceba que, neste caso, foi impresso o que estava setado para retornar na funcao delimitada.")
print ("\n---x---\n")

#Python Avançado: Função enumerate
print ("Função ENUMERATE (conhecimento básico sobre listas recomendado)")
print ("Considerando que você já tenha um conhecimento sobre listas, é possível utilizar a função padrão \'enumerate\' para listar os índices e elementos de uma lista. Segue um exemplo de sintaxe:\n")
print ("lista = [\"abacate\", \"bola\", \"cachorro\"]\nfor i, nome in enumerate(lista):\n\tprint(i, nome)")

#Teste2
print ("\nCompilação interna executada:")
lista = ["abacate", "bola", "cachorro"]
for i, nome in enumerate(lista):
        print(i, nome)
print ("\nExplicaçao: Conseguimos verificar que, em apenas 3 linhas de código, foi possível criar uma lista e imprimir seus elementos com os respectivos indices.")
print ("\n---x---\n")