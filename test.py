data_sample = [(1, 2, 3, 5, 12), (4.4, 5.5, 6, 7),
               (0, 2.4, 6.5, 7.6), (21, 43, 25, 78)]

prices = []

for row in data_sample[1:]:  # get a subset of a list, removing the first element: (1, 2, 3, 5, 12)
    prices.append(row[2])  # from the new list, add the third element: row[2]

print(prices)

print(sum(prices))


def calculate_sum_succinct(data_sample):
    prices = [float(row[2]) for row in data_sample[1:]]  # is the same loop above, but using 'list comprehensions'
    return sum(prices)


data_sample = [(1, 2, 3, 5, 12), (4.4, 5.5, 6, 7),
               (0, 2.4, 6.5, 7.6), (21, 43, 25, 78)]

result = calculate_sum_succinct(data_sample)

print(result)
