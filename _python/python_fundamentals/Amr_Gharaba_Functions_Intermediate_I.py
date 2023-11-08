import random
def randInt(min = 0, max = 100):
    if(max < 0): max*=-1
    if(min < 0): min*=-1
    if(min > max):
        min, max = max , min
    num = round((random.random()) * (max - min))+min
    return num

print(randInt(-20, -15))

