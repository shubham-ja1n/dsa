def min_unpayable_amount(coins):
    coins.sort()
    min_amount = 1

    for coin in coins:
        if coin <= min_amount:
            min_amount += coin
        else:
            break

    return min_amount
