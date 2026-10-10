
number = [1, 2, 3, 4, 5, 6]
odd = list(filter(lambda x: x%2 != 0, number))
square=list(map(lambda x:x**2,odd))
print("odd no",odd)
print("square",square)
