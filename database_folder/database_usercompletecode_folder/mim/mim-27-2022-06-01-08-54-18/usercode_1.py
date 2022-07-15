class TestStringMethods(unittest.TestCase):
    def setUp(self):
       # input data list
       self.input_data = [1,4,5,6,7,8,9,10,11,12,13,54,55,56,95,97,101,106,205,210,217,278,298,318,329,330,331,336,400]
       # input aim value
       self.aim = 101
       self.result = '-'
       # input expect index
       self.expect = 16

    def test_tri(self):
        try :
            self.assertEqual(interpolation_search(self.input_data,self.aim),self.expect)
            self.result = self.expect
        except AssertionError:
            self.result = interpolation_search(self.input_data,self.aim)
        except Exception as e:
            self.result = e
