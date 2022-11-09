 # The user enters the value and amount of money
# The program calculates the change and the number of small coins required for change


def short_change(inwallet, price):
    result = []
    denominations = [0.1, 0.5, 1, 2, 5, 10, 50, 100, 200, 500, 1000, 2000, 5000]
    l = len(denominations) - 1
    balance = inwallet - price

    if balance in denominations:
        result.append(balance)
        return result

    while sum(result) != balance:
        if sum(result) + denominations[l] > balance:
            l -= 1
        else:
            result.append(denominations[l])

    return result, balance


print(short_change(100, 11))
