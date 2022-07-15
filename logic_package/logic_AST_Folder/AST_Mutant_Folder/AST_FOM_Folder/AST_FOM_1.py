def tri(a, b, c):
    result = ''
    if ((a + b) <= c):
        result = 'N'
    elif (((a + a) + (b * b)) < (c * c)):
        result = 'Obtus'
    elif (((a * a) + (b * b)) == (c * c)):
        result = 'Righ'
    elif (((a * a) + (b * b)) > (c * c)):
        result = 'Acut'
    return result
