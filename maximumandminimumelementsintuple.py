tup = tuple(map(int,input("enter tuple elements separated by space: ").split()))

k= int(input("enter the value of k: "))

sorted_tup = sorted(tup)

k_smallest = sorted_tup[:k]
k_largest = sorted_tup[-k:]

print ("k is smallest elements: ",tuple(k_smallest))
print ("k is largest elements: ",tuple(k_largest))
