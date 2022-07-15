class TestStringMethods(unittest.TestCase):
    def setUp(self):
       # input data list
       self.input_data = [11,12,13,54,95,106,217,318,329]
       # input aim value
       self.aim = 91
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
