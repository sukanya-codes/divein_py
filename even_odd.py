def even_odd():
    x = input("what is your number?")
    x_as_int = int(x)
    remainder = x_as_int % 2
    if remainder == 0:
        print("even number")
    else:
        print("odd number")


even_odd()
