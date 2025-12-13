string = input("enter a string: ")

freq = {}

for ch in string :
    freq[ch] = freq.get(ch,0) + 1

min_count = min(freq.values())

for ch in freq:
    if freq[ch] == min_count:
        print("Least frequent character:", ch)
   