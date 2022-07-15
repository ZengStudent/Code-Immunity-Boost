class TestStringMethods(unittest.TestCase):
    def setUp(self):
       self.input_data = [1, 2, 2, 3, 3, 4, 4, 4, 7, 8, 18, 18, 19, 20, 20, 20, 21, 26, 32, 33, 36, 37, 38, 40, 40, 43, 46, 47, 52, 54, 54, 55, 56, 58, 60, 63, 64, 67, 68, 71, 76, 76, 84, 84, 86, 88, 88, 89, 92, 94]
       self.aim = 63
       self.result = '-'
       self.expect = 35

    def test_tri(self):
        try :
            self.assertEqual(interpolation_search(self.input_data,self.aim),self.expect)
            self.result = self.expect
        except AssertionError:
            self.result = interpolation_search(self.input_data,self.aim)
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