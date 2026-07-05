def insertion_sort(v):
    for i in range(1, len(v)):
        x = v[i]
        j = i - 1
        while j >= 0 and x < v[j]:
            v[j+1] = v[j]
            j -= 1

        v[j+1] = x

lista = [8, 2, 5, 1]

insertion_sort(lista)

print(lista)