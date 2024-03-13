def find_numbers(min, max):
    return list(filter(lambda x: (x % 7 == 0) and (x % 5 != 0), range(min, max + 1)))

print(find_numbers(10, 50))