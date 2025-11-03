my_list = []
#creating the list
my_list.append("a")
#adding first value "a"
my_list.extend(["b","c","d","e"])
#adding b through e simultaneously

for item in my_list:
    #creating for loop to print each item separately
    print(item)
    #printing each item separately
print(my_list)
#printing whole list together

my_list.remove("e")
#removing last letter of list
x = my_list.copy()
#creating x representing the modified list
print(x)