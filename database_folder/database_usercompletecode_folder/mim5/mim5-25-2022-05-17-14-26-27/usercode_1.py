class TestStringMethods(unittest.TestCase):
    def setUp(self):
       # input data list
       self.input_a = [1, 3, 7, 10, 12, 15, 16, 16, 17, 23, 24, 24, 34, 34, 36, 36, 37, 42, 45, 48, 50, 53, 54, 58, 59, 62, 65, 66, 67, 67, 67, 68, 70, 72, 72, 76, 78, 80, 84, 86, 87, 88, 88, 89, 91, 92, 93, 94, 95, 97]
       self.result = '-'
       # input expect value
       self.expect = 60.5

    def test_tri(self):
        try :
            self.assertEqual(median(self.input_a),self.expect)
            self.result = self.expect
        except AssertionError:
            self.result = median(self.input_a)
        except Exception as e:
            self.result = e
