class TestStringMethods(unittest.TestCase):
    def setUp(self):
       # input data list
       self.input_data = [13,5,7,9]
       # input aim value
       self.aim = 1.5
       self.result = '-'
       # input expect index
       self.expect = 'No'

    def test_tri(self):
        try :
            self.assertEqual(interpolation_search(self.input_data,self.aim),self.expect)
            self.result = self.expect
        except AssertionError:
            self.result = interpolation_search(self.input_data,self.aim)
        except Exception as e:
            self.result = e
