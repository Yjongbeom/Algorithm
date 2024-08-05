import heapq
import sys

heap = []

n = int(sys.stdin.readline())

for _ in range(n):
    s = int(sys.stdin.readline())
    if s == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(-heapq.heappop(heap))
    else:
        heapq.heappush(heap, -s)