Estudo - Funcionamento do algoritmo:

def insertion_sort(v):
    for i in range(1, len(v)):
        x = v[i]
        j = i - 1
        while j >= 0 and x < v[j]:
            v[j+1] = v[j]
            j -= 1

        v[j+1] = x

lista = [8, 2, 5, 1]

i = 1

x = v[1] --> x = 2
j = 1-1 --> j = 0
j >=0? sim e x < v[j]? sim (2 < 8)
    v[0+1] = v[0]
    v[1] = v[0], então:
    lista = [8, 8, 5, 1] -> 2 está na variável x
    j -= 1 --> j = -1 --> sai do while
v[j+1] = x
v[-1+1] = x
v[0] = x
v[0] = 2, então
lista = [2, 8, 5, 1]

i = 2

x = v[2] --> x = 5
j = 2-1 --> j = 1
j >=0? sim e x < v[j]? sim (5 < 8)
    v[2] = v[1], então
    lista = [2, 8, 8, 1]
    j -=1 --> j = 0
j >=0? sim e x < v[j]? não (5 < 2) --> sai do while
v[j+1] = x
v[1] = x
v[1] = 5, então
lista = [2, 5, 8, 1]

i = 3

x = v[3] --> x = 1
j = 3-1 --> j = 2
j >=0? sim e x < v[j]? sim (1 < 2)
    v[3] = v[2], então
    lista = [2, 5, 8, 8]
    j -=1 --> j = 1

j >=0? sim e x < v[j]? sim (1 < 5) --> continua no while
v[1+1] = v[1]
v[2] = v[1], então
lista = [2, 5, 5, 8]
j -=1 --> j = 0

j >=0? sim e x < v[j]? sim (1 < 2) --> continua no while
v[0+1] = v[0]
v[1] = v[0], então
lista = [2, 2, 5, 8]
j -= 1 --> j = -1

j >=0? não --> sai do while
v[j+1] = x
v[-1+1] = x
v[0] = x
v[0] = 1, então
lista = [1, 2, 5, 8]





