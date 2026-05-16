def lengthoflongestsubstring(s: str) -> int:
    seen = {}
    left = 0
    max_len = 0

    for right, char in enumerate(s):
        if char in seen and seen[char] >= left:
            left = seen[char] + 1
        seen[char] = right
        max_len = max(max_len, right - left + 1)

    return max_len

result = lengthoflongestsubstring("abccabacb")
print(result)
result1= lengthoflongestsubstring("cbddbcdcb")
print(result1)
result2 = lengthoflongestsubstring("sweeswwse")
print(result2)






