nums = []
for i in range(6):
    num = int(input(f"Digite o {i + 1}º número:"))
    nums.append(num)

avg = sum(nums) / len(nums)
# "sum" soma todos da lista 
# "len" lê todos os npumeros da lista

avg_up = []
avg_down = []
for num in nums:
    if num >= avg:
        avg_up.append(num)
    else:
        avg_down.append(num)
        
print(f"Número abaixo da média: {avg_down}")
print(f"Número acima da média: {avg_up}")
