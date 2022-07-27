#a lista precisa estar organizada antes de começar a busca

lista = sorted((14, 26, 25, 7, 33, 8, 29, 48, 57, 38, 32, 19, 44, 97,58, 78, 99, 54, 40, 25, 15, 74, 41, 25, 72, 23, 28, 76, 99, 9, 57, 21, 56, 75))

# def binarySearch(arr, low, high, x, count):
#     mid = (high + low) // 2
#     if high >= low:
#         if x == arr[mid]:
#             return (mid, count)
#         elif arr[mid] > x:
#             count += 1
#             return binarySearch(arr, low, mid -1, x, count)
#         else:
#             count += 1
#             return binarySearch(arr, mid + 1, high, x, count)
#     else:
#         return -1

# if __name__ == "__main__":
#     list_break = 0
#     resultado = binarySearch(lista, 0, len(lista), d, list_break)
#     print(lista)
#     if resultado != -1:
#         print('numero encontrado: ', resultado)
#         # for m, c in resultado:
#         #     print('o indice do meio e: ', m,' e o numero de quebras da lista e: ', c)
#     else:
#         print('numero inexistente ', resultado) 

def binarySearchIterative(arr,x):
    low = 0
    mid = 0
    high = len(arr)
    counter = 0
    while (low <= high):
        mid = (high + low)//2 
        if arr[mid] < x:
            counter += 1
            low = mid
        elif arr[mid] > x:
            counter += 1
            high = mid
        else:
            return (mid, counter)
    return -1


if __name__ == "__main__":
    d = int(input('digite o numero entre 7 e 99: '))
    resultado = binarySearchIterative(lista, d)
    if resultado != -1:
        mid,counter = resultado
        print('o numero ', mid,' foi achado e levou ', counter,' vezes para ser calculado')
    else:
        print('numero inexistente, codigo: ', resultado)

    