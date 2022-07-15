class TestStringMethods(unittest.TestCase):
    def setUp(self):
       # input data list
       self.input_data = [10, 12, 13, 16, 18, 19, 20,21, 22, 23, 24, 33, 35, 42, 47,52,55,56,57,58,59,60,62,63,65,68,72,73,75,77] 
       # input aim value
       self.aim = 99
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
