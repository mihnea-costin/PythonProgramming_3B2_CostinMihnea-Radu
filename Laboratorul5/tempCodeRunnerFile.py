
    list = [0, 1]
    for i in range(2, 1000):
        list.append(list[i - 1] + list[i - 2])
    if "filters" in kwargs.keys():
        list = [flt for flt in list if all([p(flt) for p in kwargs["filters"]])]
    if "limit" in kwargs.keys():
        return list[:kwargs["limit"]]
    if "offset" in kwargs.keys():
        list = list[kwargs["offset"]:]
    return list   

def sum_digits(x):
    return sum(map(int, str(x)))

print(process(filters=[lambda item: item % 2 == 0, lambda item: item == 2 or 4 <= sum_digits(item) <= 20], limit=2, offset=2))
