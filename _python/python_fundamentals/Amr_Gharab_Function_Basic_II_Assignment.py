#1

def countdown(x):
    list = []
    for x in range(x, -1, -1):
        list.append(x)
    return list
print(countdown(5))
##################

#2
def print_and_return(list):
    print(list[0])
    return(list[1])

print_and_return([1,2])
#####################

#3
def first_plus_length(list):
    return list[0]+len(list)

print(first_plus_length([1,2,3,4,5]))
##############

#4
def values_greater_than_second(list):
    new_list = []
    if(len(list) < 2):
        return False
    else:
        for i in range(0, len(list), 1):
            if(list[i] > list[1]):
                new_list.append(list[i])
        return len(new_list), new_list
print(values_greater_than_second([5,2,3,2,1,4]))
###########################

#5
def length_and_value(x,y):
    list = []
    for x in range(x, 0, -1):
        list.append(y)
    return list
print(length_and_value(5,6))
