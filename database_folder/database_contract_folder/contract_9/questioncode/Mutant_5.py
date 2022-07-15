def EucGCD(input_a, input_b):
    r = (input_a % input_b)
    q = int((input_a / input_b))
    while (r != 0):
        input_a = input_b
        input_b = r
        q = int((input_a / input_b))
        r = (input_a - (input_b + q))
    return input_b
