def tri(a,b,c):
    result = ''
    # (1) Determine whether the sum of two sides is greater than the third side
    if a + b >= c and b + c >= a and c + a >= b:
        result = ''
    else:
        return 'No'

    # (2) Determine the type of triangle (angle, length)

    # equilateral triangle
    if(a==b and b==c):
        result = 'Equilateral'
    # isosceles triangle
    elif((a==b and a!=c and b!=c) or (b==c and b!=a and c!=a) or (a==c and a!=b and c!=b)):
        result = 'Isosceles'
        # obtuse triangle
        if (a * a + b * b < c * c):
            result = 'Obtuse Isosceles'
        # Right Isosceles
        elif (a * a + b * b == c * c):
            result = 'Right Isosceles'
        # Acute Isosceles
        elif (a * a + b * b > c * c):
            result = 'Acute Isosceles'
    # Scalane
    elif(a!=b and b!=c and c!=a):
        result = 'Scalane'
        # Obtuse Scalane
        if (a * a + b * b < c * c):
            result = 'Obtuse Scalane'
        # Right Scalane
        elif (a * a + b * b == c * c):
            result = 'Right Scalane'
        # Acute Scalane
        elif (a * a + b * b > c * c):
            result = 'Acute Scalane'

    return result