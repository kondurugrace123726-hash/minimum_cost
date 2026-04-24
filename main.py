
import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
a = [int(input()) for _ in range(n)]

MAXN = n + 5
freq = [0] * (n + 5)

cur_cost = 0
L = 0
R = -1

def add(x):
    global cur_cost
    if freq[x] > 0:
        cur_cost += 1
    freq[x] += 1

def remove(x):
    global cur_cost
    freq[x] -= 1
    if freq[x] > 0:
        cur_cost -= 1

def adjust(l, r):
    global L, R
    while R < r:
        R += 1
        add(a[R])
    while R > r:
        remove(a[R])
        R -= 1
    while L < l:
        remove(a[L])
        L += 1
    while L > l:
        L -= 1
        add(a[L])

INF = 10**18
dp_prev = [INF] * (n + 1)
dp_cur = [INF] * (n + 1)

dp_prev[0] = 0

def compute(l, r, optl, optr):
    if l > r:
        return
    
    mid = (l + r) // 2
    best_pos = -1
    dp_cur[mid] = INF

    for p in range(optl, min(mid, optr) + 1):
        adjust(p, mid - 1)
        val = dp_prev[p] + cur_cost

        if val < dp_cur[mid]:
            dp_cur[mid] = val
            best_pos = p

    compute(l, mid - 1, optl, best_pos)
    compute(mid + 1, r, best_pos, optr)

for _ in range(1, k + 1):
    compute(1, n, 0, n)
    dp_prev, dp_cur = dp_cur, [INF] * (n + 1)

print(dp_prev[n])