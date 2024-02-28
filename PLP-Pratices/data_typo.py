#int, float data type
a=100
b=32
c=3.14
print(a+b * 2)
print((a+b)*2)
print(a==b)
print(a>b)
print((a+b)*c)

#String data tpe
plp_str= "Welcome to PLP Academy"
print(plp_str)
print(plp_str[0])
print(plp_str[-1])
print(plp_str[11:14])
student_str= 'Python Class'
print(plp_str + student_str)
print(student_str * 3)

#list data Structure
academy_ls = ['Jack', 30, 3, 4.2, 5+7j, 'Thika']
student_ls = [30, 5+7j]
print(academy_ls)
print(academy_ls[0])
print(academy_ls[4:6])
print(academy_ls + student_ls)
print(student_ls * 5)

#Tuple data structure
tuple = ('abcd', 789, 2.23, 'John', 70.2)
tinytuple = 123, 5+6j, 'John'
print(tuple)
print(tuple[2:3])
print(tuple + tinytuple)
print(tinytuple * 3)

#Dictionary data structure
dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"
tinydict = {'name': 'John', 'Code':5968, 'dept':['sales']}
print(dict)
print(dict['one'])
print(tinydict)
print(tinydict.keys())
print(tinydict.values())


#Set in python
student_id = {112, 113, 114, 116, 111, 120}
print("Student Id:", student_id)

# #Creating an empty set
empty_set = set()
print("Data type of empty set", type(empty_set))
#Creating an empty dictionary
empty_dict = {}
print("Data type of empty Dictionary", type(empty_dict))

# #Union of two sets
#set a
A = {1,2,3}
#set b
B = {7,6,8}

# #Performing Union Operator using |
print('Union using |:', A | B)

#Performing Union Operation using union()
print('Union using union():', A.union(B))

#Set Intersection
#set a
C = {1,2,3}
#set b
D = {7,6,8}

#performing intersection using &
print('Intersection using &:', C & D)

#performing intersection using intersection()
print('Intersection using intersection():', C.intersection(D))

#Difference betweent to sets
#first set
E = {3,1,5}
#second set
F = {7,5,6}

#performing the difference using -
print('Difference using -:', E - F)

#performing the difference using difference()
print('difference using difference():', E.difference(F))

#Set Symmetric Difference
#first set
G = {9,8,6}
#second set
H = {4,5,6}

#performing set symmetric difference using ^
print('Set Symmetric Difference using ^:', G ^ H)

#performing set symmetric difference using symmetric difference()
print('Set Symmetric Difference using symmetric difference(): ', G.symmetric_difference(H))


#Check if two sets are equal
#first set
I = {5,4,6}
#second set
J = {8,9,7}

#performing equal set
if I == J:
    print('Set I and Set J are Equal')
else:
    print('Set I and Set J are not Equal')

