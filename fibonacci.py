def fibonacci(index):

    sequence = [0, 1]

    if index <= 1:
        return sequence[index]

    for i in range(0, index):
        sequence.append(sequence[-1]+sequence[-2])

        if len(sequence) == index + 1:
            return sequence[index]


answer = fibonacci(0)
assert answer == 0

answer = fibonacci(2)
assert answer == 1

answer = fibonacci(3)
assert answer == 2

answer = fibonacci(100)
assert answer == 354224848179261915075

print("passed!")