def main():
    summedNums = add_three(1, 2, 3)
    print('Sum result: {}'.format(summedNums))
    finalResult = divide_two(summedNums, 3)
    print('Division result: {}'.format(finalResult))


def add_three(v1, v2, v3):
    """Add three numbers

    :param v1: number one
    :param v2: number two
    :param v3: number three
    :returns: sum number
    """
    result = v1 + v2 + v3
    return(result)


def divide_two(v1, v2):
    """Divide two numbers

    :param v1: number one
    :param v2: number two
    :returns: division result
    """
    result = v1/v2
    return(result)


if __name__ == "__main__":
    main()
