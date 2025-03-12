def casting_with_recursion(n, k):
    if n == 1:
        return 1
    else:
        return (casting_with_recursion(n - 1, k) + k - 1) % n + 1

if __name__ == '__main__':
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])  # Количество претендентов
    k = int(data[1])  # Количество тактов

    result = casting_with_recursion(n, k)
    print(result)
