# john m. Nicholson
#py4e web data week 2

import re

fin = open('actual.txt')
sumNum = 0
count = 0


for tline in fin:
    numbers = re.findall('[0-9]+',tline)
    if len(numbers) > 0:
        count = count + len(numbers)
        for j in numbers:
            sumNum = sumNum + int(j)
fin.close()
print('count = ' + str(count))
print('sum = ' + str(sumNum))
