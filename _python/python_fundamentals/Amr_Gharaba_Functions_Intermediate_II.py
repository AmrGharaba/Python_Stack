# 1.Update Values in Dictionaries and Lists
x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

#1
x[1][0]=15
#2
students[0]['last_name'] = 'Bryant'
#3
sports_directory['soccer'][0] = 'Andres'
#4
z[0]['y'] = 30
print(z)

# 2.Iterate Through a List of Dictionaries
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(some_list):
    for i in range(0, len(some_list), 1):
        print(f"first_name - {some_list[i]['first_name']}, last_name - {some_list[i]['last_name']}")

print(iterateDictionary(students))

# 3.Get Values From a List of Dictionaries
def iterateDictionary2(key_name, some_list):
    for i in range (0 , len(some_list), 1):
        print(some_list[i][key_name])

iterateDictionary2('first_name', students)

# 4.Iterate Through a Dictionary with List Values
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(some_dict):
    for key in some_dict.keys():
        print(len(some_dict[key]), key)
        
        for val in range(0, len(some_dict[key]), 1):
            print(some_dict[key][val])
        print('')

printInfo(dojo)

