"""Dado o vetor nums = [3, 11, 6, 32, 15, 22, 4, 10, 5], criar uma
matriz 3x3 com os 3 maiores elementos na primeira linha, os 3
elementos intermediários na segunda linha, e os elementos
menores na terceira linha."""

"""
matriz1 = [
    [1, 4, 7], 
    [2, 5, 8], 
    [3, 6, 9]
    ]

    matriz1 = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
"""

nums = [3, 11, 6, 32, 15, 22, 4, 10, 5]    
nums.sort()
nums.reverse()

matrizNums = [
    [nums[0], nums[3], nums[6]],
    [nums[1], nums[4], nums[7]],
    [nums[2], nums[5], nums[8]], 
]

def ler(matrizNums):
     for y in matrizNums:
        print(y)

ler(matrizNums)
print("Positivo")


        


    
    
    
