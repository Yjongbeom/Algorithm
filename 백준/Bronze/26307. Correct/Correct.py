n, m = map(int, input().split())

start = 9 * 60
end = n * 60 + m

print(end - start)