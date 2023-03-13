try:
    num = int(input("Enter an integer number: "))
    x_square = lambda a: a ** 2
    print("The square of the number you entered is", x_square(num))

    x_cube = lambda a: a ** 3
    print("The cube of the number you entered is", x_cube(num))

    x_fourth_power = lambda a: a ** 4
    print("The fourth power of the number you entered is", x_fourth_power(num))

    x_fifth_power = lambda a: a ** 5
    print("The fifth power of the number you entered is", x_fifth_power(num))

except ValueError:
    print("invalid value")




