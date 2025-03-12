def sort_by_template(nums, template):
    order = {num: i for i, num in enumerate(template)}
    return sorted(nums, key=lambda x: (order.get(x, float('inf')), x))

n  = int(input().strip())
nums = [int(i) for i in input().split()]
m = int(input().strip())
template = list(map(int, input().split()))
print(*sort_by_template(nums, template))