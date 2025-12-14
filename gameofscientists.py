import sys

def query(b):
    print("?", b)
    print(flush=True)
    res = int(input())
    if res == -2:
        sys.exit(0) 
    return res

def solve_one_game(c):
    s2 = query(2)
    s3 = query(3)
    s4 = query(4)
    s5 = query(5)
    
    
    x = reconstruct_x(s2, s3, s4, s5)
    
    print("!", x)
    print(flush=True)
    r = int(input())
    if r == 0:
        sys.exit(0) 
    return
def reconstruct_x(s2, s3, s4, s5):
    return 1
t, k, c = map(int, input().split())
for _ in range(t):
    solve_one_game(c)
