def main():
    num = 5  # TODO: change this value

    if num == 0:
        num += 2
        print('Your value is now ', num, '.', sep="")
    else:
        num += 4
        print('Your value is now ', num, '.', sep="")
    if num > 0:
        num -= 4
        print('Your value is now ', num, '.', sep="")


main()
