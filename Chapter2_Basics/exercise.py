'''Exercise 2:
1.)
Write code that takes a list of integer numbers and an integer number a
and prints the index of the number if its in the list.

2.)
Write code that takes two integers (x, y) computes the following:
Sum up all integer numbers from x (inclusive) to y (non-inclusive) with a step width of 2.
'''


# exercise1
lst = [1, 2, 3]
a = 3

for idx in range(len(lst)):
    if lst[idx] == a:
        print(idx)


print(" ")

# exercise2
x = 2
y = 10

sum_x_to_y = 0
# range(start, stop, step)
for idx in range(x, y, 2):
    sum_x_to_y = sum_x_to_y + idx
    print(sum_x_to_y)
