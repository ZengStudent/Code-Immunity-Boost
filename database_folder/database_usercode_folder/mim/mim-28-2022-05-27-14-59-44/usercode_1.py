class TestStringMethods(unittest.TestCase):
    def setUp(self):
       # input length
       self.input_a = 6
       # input length
       self.input_b = 3
       # input length
       self.input_c = 6
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
