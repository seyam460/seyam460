string = input ("enter a string: ")

freq = {}

for ch in string:
    freq[ch] = freq.get(ch,0) + 1

max_count = max(freq.values())

for ch in string :
    if freq[ch] == max_count :
        print ("most frequent character: ",ch)