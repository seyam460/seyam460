li = [1,2,3,4,5,6,7,8,9,10]

indx = li.index(3)
print(indx)
found = 5 in li
print(found)
li = [1,2,3,4,7,8,9]
key = 4
for item in li:
    if key == item:
        print("found")
        break

    print("not found")