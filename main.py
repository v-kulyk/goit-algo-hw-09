import timeit

coins = [50, 25, 10, 5, 2, 1]

def find_coins_greedy(amount):
    result = {}

    for coin in coins:
        count = amount // coin
        if count > 0:
            result[coin] = count
            amount -= count * coin

    return result


def find_coins_dynamic(amount):
    used_coins = [float('inf')] * (amount + 1)
    used_coins[0] = 0
    for current_amount in range(1, amount + 1):
        for coin in coins:
            if current_amount >= coin:
                used_coins[current_amount] = min(used_coins[current_amount], used_coins[current_amount - coin] + 1)

    result = {}
    current_amount = amount
    for coin in coins:
        count = 0
        while current_amount >= coin and used_coins[current_amount] == used_coins[current_amount - coin] + 1:
            current_amount -= coin
            count += 1
        if count > 0:
            result[coin] = count
    return result


if __name__ == '__main__':
    total = int(input("Enter required amount:\n"))

    # Жадібний алгоритм
    time_greedy = timeit.timeit(lambda: find_coins_greedy(total), number=1)
    result_greedy = find_coins_greedy(total)

    # Динамічне програмування
    time_dynamic = timeit.timeit(lambda: find_coins_dynamic(total), number=1)
    result_dynamic = find_coins_dynamic(total)

    print(f"Greedy Result: {result_greedy}")
    print(f"Dynamic Result: {result_dynamic}")

    print(f"Greedy Time: {time_greedy} seconds")
    print(f"Dynamic Time: {time_dynamic} seconds")
