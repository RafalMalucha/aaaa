import random

AandH = ['a', 'h']

haha = ''

seed = random.randint(1000000000, 99999999999)
lenght = int(seed // 100000000)

AorH = 0

if seed % 2 == 0:
    for i in range(1, lenght):
        if AorH % 2 == 0:
            haha += str(AandH[0])
            x = random.randint(1, 2)
            AorH += x
        if AorH % 2 != 0:
            haha += str(AandH[1])
            x = random.randint(1, 2)
            AorH += x
if seed % 2 != 0:
    for i in range(1, lenght):
        if AorH % 2 == 0:
            haha += str(AandH[1])
            x = random.randint(1, 2)
            AorH += x
        if AorH % 2 != 0:
            haha += str(AandH[0])
            x = random.randint(1, 2)
            AorH += x
        
        
print(haha)