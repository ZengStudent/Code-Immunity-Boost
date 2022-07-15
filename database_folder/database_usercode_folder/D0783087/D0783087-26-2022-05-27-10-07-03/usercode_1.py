class TestStringMethods(unittest.TestCase):
    def setUp(self):
       # input positive integer
       self.input_a = 99
       # input positive integer
       self.input_b = 15
       self.result = '-'
       # input expect common factor
       self.expect = 3

    def test_tri(self):
        try :
            self.assertEqual(EucGCD(self.input_a,self.input_b),self.expect)
            self.result = self.expect
        except AssertionError:
            self.result = EucGCD(self.input_a,self.input_b)
        except Exception as e:
            self.result = e
