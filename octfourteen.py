my_list = []
my_list.append("this")
#print(my_list)

my_list.append("is")
#print(my_list)

my_list.append("my")
#print(my_list)
my_list.append("list")
#print(my_list)

print(len(my_list))
print(my_list[2])

for i in range(len(my_list)):
    print(my_list[i])

my_list.remove("this")
print(my_list)
my_list.pop()
print(my_list)