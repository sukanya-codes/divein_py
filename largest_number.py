random_list = [12, 21, 24, 100, 61, 100, 27, 67, 69, 92]


def largest_number(x):
    print(x)
    largest = random_list[0]
    for y in x:
        if y > largest:
            largest = y
            # print (y)
    print(largest)


largest_number(random_list)
