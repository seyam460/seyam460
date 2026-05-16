def characterreplacement (s:str , k:int) ->int :
    count = {}
    left = 0
    max_len = 0
    max_freq = 0

    for right in range(len(s)):
        char = s[right]
        count[char] = count.get(char, 0) + 1 
        max_freq = max(max_freq , count[char])
        
        window_size = right - left + 1 
        if window_size - max_freq > k :
            count[s[left]] -= 1
            left +=1

            max_len = max(max_len , right - left + 1)

    return max_len

print(characterreplacement("ABBA",2))

