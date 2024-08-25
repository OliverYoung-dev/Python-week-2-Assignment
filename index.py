my_list = []
print(my_list)

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

print(my_list)

#inserting into a specific index
my_list.insert(1, 15)

print(my_list)

#Extending my list with another list
my_list.extend([50, 60, 70])
print(my_list)

#removing an element from my list
my_list.remove(70)
print(my_list)

# soerting in ascending order
my_list.sort()
print(my_list)

# finding the index of an element
print(my_list.index(30))