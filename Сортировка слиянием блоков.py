num = int(input().strip())
array = [int(i) for i in input().split()]
blocks = 0
max_so_far = 0
for i, ai in enumerate(array):
    max_so_far = max(max_so_far, ai)
    if max_so_far == i:
        blocks += 1
print(blocks)