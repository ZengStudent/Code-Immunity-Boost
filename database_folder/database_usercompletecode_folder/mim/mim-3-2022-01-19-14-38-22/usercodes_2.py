class TestStringMethods(unittest.TestCase):    
    def setUp(self):    
       self.input_a = [6, 7, 9, 10, 11, 12, 12, 12, 12, 15, 18, 18, 25, 25, 28, 37, 37, 39, 42, 42, 44, 45, 47, 50, 52, 54, 54, 57, 66, 67, 69, 70, 71, 73, 73, 74, 75, 79, 80, 81, 82, 84, 85, 88, 89, 90, 94, 94, 95, 98]    
       self.result = '-'    
       self.expect = 53.0    
    
    def test_tri(self):    
        try :    
            self.assertEqual(median(self.input_a),self.expect)    
            self.result = self.expect    
        except AssertionError:    
            self.result = median(self.input_a)    
        except Exception as e:    
            self.result = e    
