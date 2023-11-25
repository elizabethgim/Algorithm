
def solution(cap, n, deliveries, pickups):
    answer = 0
    delivery = [0 for _ in range(n)]
    pickup = [0 for _ in range(n)]

    delivery[0] = deliveries[0]
    pickup[0] = pickups[0]

    for i in range(1, n):
        delivery[i] = delivery[i-1] + deliveries[i]
        pickup[i] = pickup[i-1] + pickups[i]

    print(delivery)
    print(pickup)

    return answer

# 16
print(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]))

