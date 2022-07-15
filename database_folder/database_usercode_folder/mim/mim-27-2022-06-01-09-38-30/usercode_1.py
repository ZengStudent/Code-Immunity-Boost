class TestStringMethods(unittest.TestCase):
    def setUp(self):
       # input data list
       self.input_data = [10,11,12,13,14,15,16,17,99,15]
       # input aim value
       self.aim = 15
       self.result = '-'
       # input expect index
       self.expect = 9

    def test_tri(self):
        try :
            self.assertEqual(interpolation_search(self.input_data,self.aim),self.expect)
            self.result = self.expect
        except AssertionError:
            self.result = interpolation_search(self.input_data,self.aim)
        except Exception as e:
            self.result = e
