

"""
example 1
w = ['cats' , 'windos' , 'defenestrate']

for i in w:
    print(i, len(i))

#range example

#for i in range(5):

for i in range(0,100,2):
    print(i)


#combine range() and len()

a = ['Mary', 'had', 'a', 'little', 'lamb']

for i in range(len(a)):
    print(i, a[i])



colors = ['blue', 'green', 'red', 'purple']
for c in colors:
    if c == "blue":
        continue
    elif c == "red":
        break
    print(c)

#A dictionary example:

>>> ages = {'kevin': 59, 'bob': 40, 'kayla': 21}
>>> for key in ages:
...     print(key)
...
kevin
bob
kayla


#Unpacking Multiple Items in a for Loop

list_of_points = [(1, 2), (2, 3), (3, 4)]
for x, y in list_of_points:
     print(f"x: {x}, y: {y}")

output:
x: 1, y: 2
x: 2, y: 3




for name, age in ages.items():
   print(f"Person Named: {name}")
   print(f"Age of: {age}")

Person Named: kevin
Age of: 59
Person Named: bob
Age of: 40
Person Named: kayla
Age of: 21

"""