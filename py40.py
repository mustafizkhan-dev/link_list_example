# 40. Demonstrate all list methods

numbers = [30, 10, 20, 10]

numbers.append(40)
print("append:", numbers)

numbers.extend([50, 60])
print("extend:", numbers)

numbers.insert(1, 15)
print("insert:", numbers)

numbers.remove(10)
print("remove:", numbers)

numbers.pop()
print("pop:", numbers)

numbers_copy = numbers.copy()
print("copy:", numbers_copy)

print("count:", numbers.count(10))
print("index:", numbers.index(20))

numbers.sort()
print("sort:", numbers)

numbers.reverse()
print("reverse:", numbers)

numbers.clear()
print("clear:", numbers)


