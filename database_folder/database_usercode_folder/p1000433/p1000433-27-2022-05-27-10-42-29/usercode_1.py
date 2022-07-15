class TestStringMethods(unittest.TestCase):
    def setUp(self):
       # input data list
       self.input_data = [7,7,8,9]
       # input aim value
       self.aim = 8
       self.result = '-'
       # input expect index
       self.expect = 3

    def test_tri(self):
        try :
            self.assertEqual(interpolation_search(self.input_data,self.aim),self.expect)
            self.result = self.expect
        except AssertionError:
            self.result = interpolation_search(self.input_data,self.aim)
        except Exception as e:
            self.result = e
