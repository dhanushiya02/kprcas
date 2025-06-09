a=10
b=20
c=50
if a>b or a>c:
    print("a is greater")
elif b>c or b>a:
    print("b is greater")
else:
    print("c is greater")

for i in range(1,10,2):
     print(i)
for i in range(2,20,2):
     print(i)

def add():
    print(10+20)
add()

list=[1,2,3,4,5,6,7]
for i in list:
    print(i)
print(type(list))

tuple=(9,8,7,6,5)
for i in tuple:
    print(i)
    print(type(tuple))

dictionary={"name":"dhanushiya","password":"0219"}
print(dictionary["name"])
print(type(dictionary))
for key in dictionary:
    print(dictionary[key])