def fibonacci_measurements(generation: int) -> int:
    if generation == 0 or generation == 1:
        return 1
    return fibonacci_measurements(generation - 1) + fibonacci_measurements(generation - 2)

if __name__ == '__main__':
    import sys
    input = sys.stdin.read
    generation = int(input().strip())
    result = fibonacci_measurements(generation)
    print(result)
