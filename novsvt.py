'''
for i in range(1, 101):
    print(i)
for i in range(100, -1, -1):
    print(i)

x = 20%3
print(x)

'''
a = int(input("Write a number: "))
if a%15 == 0:
    print("Fizzbuzz")
elif a%5 == 0:
    print("Buzz")
elif a%3 == 0:
    print("Fizz")