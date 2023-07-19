from itertools import combinations

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
chicken, house = [], []

for r in range(n):
    for c in range(n):
        if graph[r][c] == 1:
            house.append((r,c))
        elif graph[r][c] == 2:
            chicken.append((r,c))

def get_sum(candidate):
    result = 0
    for hx, hy in house:
        dist = 1e9
        for cx, cy in candidate:
            dist = min(dist, abs(hx-cx)+abs(hy-cy))
        result = result + dist
    return result

candidates = list(combinations(chicken, m))

result = 1e9
for candidate in candidates:
    result = min(result, get_sum(candidate))

print(result)