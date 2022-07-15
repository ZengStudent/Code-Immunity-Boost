class TestStringMethods(unittest.TestCase):
    def setUp(self):
       self.input_a = 583
       self.input_b = 599
       self.input_c = 593
       self.result = '-'
       self.expect = 'Acute Scalane'

    def test_tri(self):
        try :
            self.assertEqual(tri(self.input_a,self.input_b,self.input_c),self.expect)
            self.result = self.expect
        except AssertionError:
            self.result = tri(self.input_a,self.input_b,self.input_c)
        except Exception as e:
            self.result = e
