#1

def countdown(x):
    list = []
    for i in range(x, -1, -1):
        list.append(i)
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
        for i in range(len(list)):
            if(list[i] > list[1]):
                new_list.append(list[i])
        print(len(new_list))
        return new_list
print(values_greater_than_second([5,2,3,2,1,4]))
###########################

#5. 
# This Length, That Value - Write a function that accepts two integers as parameters: size and value.
# The function should create and return a list whose length is equal to the given size, and whose values are all the given value.
# Example: length_and_value(4,7) should return [7,7,7,7]
# Example: length_and_value(6,2) should return [2,2,2,2,2,2]
def length_and_value(x,y):
    list = []
    for i in range(x, 0, -1):
        list.append(y)
    return list
print(length_and_value(5,6))
