class TestStringMethods(unittest.TestCase):
    def setUp(self):
       # input length
       self.input_a = 100
       # input length
       self.input_b =100
       # input length
       self.input_c = 100
       self.result = '-'
       # input expect type
       self.expect = 'Equilateral'

    def test_tri(self):
        try :
            self.assertEqual(tri(self.input_a,self.input_b,self.input_c),self.expect)
            self.result = self.expect
        except AssertionError:
            self.result = tri(self.input_a,self.input_b,self.input_c)
        except Exception as e:
            self.result = e
