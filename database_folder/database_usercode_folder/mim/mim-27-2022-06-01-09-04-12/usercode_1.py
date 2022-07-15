class TestStringMethods(unittest.TestCase):
    def setUp(self):
       # input data list
       self.input_data = [95,97,101,106,205,210,217,278,298,318,329,330,331,336,400]
       # input aim value
       self.aim = 101
       self.result = '-'
       # input expect index
       self.expect = 2

    def test_tri(self):
        try :
            self.assertEqual(interpolation_search(self.input_data,self.aim),self.expect)
            self.result = self.expect
        except AssertionError:
            self.result = interpolation_search(self.input_data,self.aim)
        except Exception as e:
            self.result = e
