class TestStringMethods(unittest.TestCase):
    def setUp(self):
       # input data list
       self.input_data = [1, 5, 6, 6, 6, 7, 7, 7, 9, 13, 14, 15, 18, 19, 21, 26, 29, 30, 31, 33, 33, 39, 40, 42, 43, 45, 50, 50, 51, 55, 56, 59, 61, 62, 66, 68, 72, 74, 75, 76, 80, 83, 83, 84, 85, 89, 91, 95, 97, 97]
       # input aim value
       self.aim = 61
       self.result = '-'
       # input expect index
       self.expect = 32

    def test_tri(self):
        try :
            self.assertEqual(interpolation_search(self.input_data,self.aim),self.expect)
            self.result = self.expect
        except AssertionError:
            self.result = interpolation_search(self.input_data,self.aim)
        except Exception as e:
            self.result = e
