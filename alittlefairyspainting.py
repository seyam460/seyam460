def last_cell_color(n, colors):
    color_set = set(colors)
    last_color = 0
    
    for i in range(n + 1, 1019):
        last_color = len(color_set)
        color_set.add(last_color)
    
    return last_color

t = int(input())
for _ in range(t):
    n = int(input())
    colors = list(map(int, input().split()))
    print(last_cell_color(n, colors))
