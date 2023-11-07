for i in range(0, 151, 1):
    print(i)

for i in range(5,1001,5):
    print(i)

for i in range(1,101,1):
    if(i%5==0):
        if(i%10==0):
            print('Coding Dojo')
            continue
        print('coding')
        
    else:
        print(i)

sum = 0
for i in range(0, 500001, 1):
    if(i%2):
        sum+=i
print(sum)

for i in range(2018, 0, -4):
    print(i)

lowNum = 9
highNum = 100
mult = 4
for lowNum in range(lowNum, highNum+1, 1):
    if(lowNum%mult==0):
        print(lowNum)
