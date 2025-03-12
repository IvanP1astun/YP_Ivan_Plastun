def get_res(nums):
    result = []
    for i in nums:
        count = 0
        for j in nums:
            if j < i:
                count += 1
        result.append(count)
    return ' '.join(str(n) for n in result)


nums = [int(i) for i in input().split()]
print(get_res(nums))