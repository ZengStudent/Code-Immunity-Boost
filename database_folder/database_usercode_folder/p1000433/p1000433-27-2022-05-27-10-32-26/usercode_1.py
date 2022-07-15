class TestStringMethods(unittest.TestCase):
    def setUp(self):
       # input data list
       self.input_data = [1,2,3,4,5,6]
       # input aim value
       self.aim = 6
       self.result = '-'
       # input expect index
       self.expect = 6

    def test_tri(self):
        try :
            self.assertEqual(interpolation_search(self.input_data,self.aim),self.expect)
            self.result = self.expect
        except AssertionError:
            self.result = interpolation_search(self.input_data,self.aim)
        except Exception as e:
            self.result = e
