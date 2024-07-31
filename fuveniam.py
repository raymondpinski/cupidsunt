from collections import Counter
my_list = [1, 2, 2, 3, 4, 4, 5, 6, 6]
counter = Counter(my_list)
print(list(counter.keys()))  # [1, 2, 3, 4, 5, 6]
