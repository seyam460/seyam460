li = [1, 2 ,3, 4]
li1 = [5,6,7]

li.extend(li1) 
print(li)

li2= [76,56,27]
li2.insert(56, 10)  
print(li2)

li3 = [34,65,98,46]
li3.insert(46, 28)
print(li3)

li4 = [2,5,9,6,5]
x= li.pop(3)
print(x)
print(li4)

li5= [1, 2, 3, 6,7,9,4]
li5.sort()
print(li5)
li5.reverse()
print(li5)

li6 = [1,2,3,4,5]
tpl = (1,4,6,8)
print(tpl)
print(type(tpl))
print(tpl[0],tpl[1],tpl[2],tpl[-1])
for item in tpl:
    print(item)

tpl = tuple()
print(tpl, type(tpl))
print(dir(tuple))

s = set()
type(s)
print(s.add(1))
print(s.add(2))
print(s.add(4))

s1= {1,2,4,5}
s2 = {7,9,1,4}
print(s1 | s2)
print(s1 & s2)
print(s1 - s2)
print(s1 ^ s2)

while True:
    q = input()
    print(s.upper())

li6 = [1, 2, 3, 4, 5, 6, 7, 8]     

max_number = float('-inf')

for num in li6:                     
    if num > max_number:
        max_number = num

print(max_number) 

 