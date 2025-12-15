def maximize_happiness(n, k, a):
    current_max = 0
    remaining = k
    happiness = 0

    for i in range(n):
        if a[i] > current_max and remaining > 0:
            increase = min(a[i] - current_max, remaining)
            current_max += increase
            remaining -= increase

        happiness += current_max

    return happiness
n = 5
k = 7
a = [1, 2, 3, 4, 5]

print(maximize_happiness(n, k, a))
