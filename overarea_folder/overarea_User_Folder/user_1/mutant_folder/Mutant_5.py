def tri(a, b, c):
    result = ''
    if ((a + b) <= c):
        result = 'No'
    elif (((a * a) + (b * b)) < (c * c)):
        result = 'Obtuse'
    elif (((a * a) + (b + b)) == (c * c)):
        result = 'Right'
    elif (((a * a) + (b * b)) > (c * c)):
        result = 'Acute'
    return result
