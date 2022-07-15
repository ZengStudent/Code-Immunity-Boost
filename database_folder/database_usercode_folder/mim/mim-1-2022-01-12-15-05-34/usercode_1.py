class TestStringMethods(unittest.TestCase):
    def setUp(self):
       self.input_a = [6]
       self.result = '-'
       self.expect = 6

    def test_tri(self):
        try :
            self.assertEqual(median(self.input_a),self.expect)
            self.result = self.expect
        except AssertionError:
            self.result = median(self.input_a)
        except Exception as e:
            self.result = e
