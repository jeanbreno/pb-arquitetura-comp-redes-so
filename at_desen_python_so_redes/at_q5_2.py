# -*- coding: utf-8 -*-
"""
Criado em 21/09/2021

@author: Jean 
"""

a = open('a.txt', 'r')
b = open('b.txt', 'r')
c = open('c.txt', 'w')



for linha in a:
    n1 = linha.split()

for linha in b:
    n2 = linha.split()

#verifica n2
if n1 < n2:
    tam2 = len(n2)
    tam1 = len(n1)
    dife1 = tam2 - tam1
    #print(dife1)
    print(tam2)
    print(tam1)
l = []
for iA, iB in zip(n1, n2):
    l.append(int(iA) + int(iB))
for i in iB:
    p = n2[tam1:tam2]
for i in p:
    l.append(int(i) + 0)


c.write(str(l))

a.close
b.close
c.close