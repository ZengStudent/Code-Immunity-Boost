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

import unittest,os,logging
path= 'c:\mypcload\myprogram\mypython\DjangoGameOnline/overarea_folder/overarea_User_Folder/D0808426/unittest_result_folder/'

order = 'original'
class TestStringMethods(unittest.TestCase):
    def setUp(self):
       # input length
       self.input_a = 5
       # input length
       self.input_b = 6.5
       # input length
       self.input_c = 5
       self.result = '-'
       # input expect type
       self.expect = 'Acute Isosceles'

    def test_tri(self):
        try :
            self.assertEqual(tri(self.input_a,self.input_b,self.input_c),self.expect)
            self.result = self.expect
        except AssertionError:
            self.result = tri(self.input_a,self.input_b,self.input_c)
        except Exception as e:
            self.result = e


        finally:
            file_dir =  path + 'unittest_'+str(order)+'.txt'
            f = open(file_dir, 'w+', encoding='UTF-8')
            f.write(str(self.result))
            f.seek(0)
            f.close()

            file_dir = path + 'unittest_expect_' + str(order) + '.txt'
            f = open(file_dir, 'w+', encoding='UTF-8')
            f.write(str(self.expect))
            f.seek(0)
            f.close()


if __name__ == '__main__':
    unittest.main()
