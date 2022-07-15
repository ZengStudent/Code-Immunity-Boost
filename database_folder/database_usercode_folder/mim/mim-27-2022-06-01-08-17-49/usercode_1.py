class TestStringMethods(unittest.TestCase):
    def setUp(self):
       # input data list
       self.input_data = [10,4,7,12,22,90,20,33,18,40]
       # input aim value
       self.aim = 88
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
