#1
def biggie_size(list):
    for i in range(0, len(list), 1):
        if(list[i]>0):
            list[i] = 'big'
    return list
print(biggie_size([-1, 3, 5, -5]))

#2
def count_positives(list):
    count = 0
    for i in range(0, len(list), 1):
        if(list[i]>0):
            count+=1
    return count
print(count_positives([-1,1,1,1]))
print(count_positives([1,6,-4,-2,-7,-2]))

#3
def sum_total(list):
    sum =0
    for i in range(0, len(list), 1):
        sum+=list[i]
    return sum
print(sum_total([1,2,3,4]))
print(sum_total([6,3,-2]))

#4
def average(list):
    sum = 0
    for i in range(0 ,len(list), 1):
        sum+=list[i]
    return sum/len(list)
print(average([1,2,3,4]))

#5
def length(list):
    return len(list)
print(length([37,2,1,-9]))
print(length([]))

#6
def minimum(list):
    if (len(list) == 0):
        return False
    else:
        min = list[0]
        for i in range(0, len(list), 1):
            if(min > list[i]):
                min = list[i]
        return min
print(minimum([37,2,1,-9]))
print(minimum([]))

#7
def maximum(list):
    if (len(list) == 0):
        return False
    else:
        max = list[0]
        for i in range(0, len(list), 1):
            if(max < list[i]):
                max = list[i]
        return max
print(maximum([37,2,1,-9]))
print(maximum([]))

#8
def ultimate_analysis(list):
    sum = 0
    max = 0
    min = 0
    if (len(list) == 0):
        return False
    else:
        for i in range(0 ,len(list), 1):
            if(max < list[i]):
                max = list[i]
            if(min > list[i]):
                min = list[i]
            sum+=list[i]
        return {'sumTotal': sum, 'average': sum/len(list), 'minimum': min, 'maximum': max, 'length': len(list)}
print(ultimate_analysis([37,2,1,-9]))

#9
def reverse_list(list):
    for i in range(0 , int(len(list)/2), 1):
        list[i], list[len(list)-1-i] = list[len(list)-1-i], list[i]
    return list
print(reverse_list([37,2,1,-9]))
    