class TestStringMethods(unittest.TestCase):  
    def setUp(self):  
       self.input_a = 28  
       self.input_b = 14  
       self.result = '-'  
       self.expect = 14  
  
    def test_tri(self):  
        try :  
            self.assertEqual(EucGCD(self.input_a,self.input_b),self.expect)  
            self.result = self.expect  
        except AssertionError:  
            self.result = EucGCD(self.input_a,self.input_b)  
        except Exception as e:  
            self.result = e  
        finally:  
            file_dir =  path + 'unittest_'+str(order)+'.txt'  
            f = open(file_dir, 'w+', encoding='UTF-8')  
            f.write(str(self.result))  
            f.seek(0)  
            f.close()  
  
            file_dir = path + 'unittest_expect_' + str(order) + '.txt'  
            f = open(file_dir, 'w+', encoding='UTF-8')  
            f.write(str(self.expect))  
            f.seek(0)  
            f.close()  
  
  
if __name__ == '__main__':  
    unittest.main()