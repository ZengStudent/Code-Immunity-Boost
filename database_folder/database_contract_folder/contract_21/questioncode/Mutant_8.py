def tri(a, b, c):
    result = ''
    if (((a + b) >= c) and ((b + c) >= a) and ((c + a) >= b)):
        result = ''
    else:
        return 'No'
    if ((a == b) and (b == c)):
        result = 'Equilateral'
    elif (((a == b) and (a != c) and (b != c)) or ((b == c) and (b != a) and (c != a)) or ((a == c) and (a != b) and (c != b))):
        result = 'Isosceles'
        if (((a * a) + (b * b)) < (c * c)):
            result = 'Obtuse Isosceles'
        elif (((a * a) + (b * b)) == (c * c)):
            result = 'Right Isosceles'
        elif (((a * a) + (b + b)) > (c * c)):
            result = 'Acute Isosceles'
    elif ((a != b) and (b != c) and (c != a)):
        result = 'Scalane'
        if (((a * a) + (b * b)) < (c * c)):
            result = 'Obtuse Scalane'
        elif (((a * a) + (b * b)) == (c * c)):
            result = 'Right Scalane'
        elif (((a * a) + (b * b)) > (c * c)):
            result = 'Acute Scalane'
    return result
