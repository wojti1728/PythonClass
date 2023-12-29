def print_even(test_list) :
    for i in test_list:
        if i % 2 == 0:
            yield i


# initializing list
test_list = [1, 4, 5, 6, 7]

# printing initial list
print("The original list is : " + str(test_list))

# printing even numbers
print("The even numbers in list are : ", print_even(test_list))
for j in print_even(test_list):
    print(j*j, end=" ")


def nextSquare():
    i = 1
    # An Infinite loop to generate squares
    while True:
        yield i * i
        i += 1  # Next execution resumes
        # from this point

print('\n')
# Driver code
for num in nextSquare():
    if num > 100:
        break
    print(num, end=' ')