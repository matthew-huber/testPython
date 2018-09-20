def test_add_three():
    from exampleProblem import add_three
    result = add_three(5, 6, 7)
    assert result == 18


def test_divide_two():
    from exampleProblem import divide_two
    result = divide_two(18, 3)
    assert result == 6
