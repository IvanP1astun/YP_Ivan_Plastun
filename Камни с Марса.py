def main(order, delivery):    
    order.sort()
    delivery.sort()
    count = 0
    for weight in delivery:
        k = 0
        while k < len(order):
            if order[k] <= weight:
                count += 1
                del order[k]
                break
            k += 1

    return count


if __name__ == '__main__':
    n = int(input())
    ordered = list(map(int, input().split()))
    m = int(input())
    delivered = list(map(int, input().split()))
    result = main(ordered, delivered)
    print(result)