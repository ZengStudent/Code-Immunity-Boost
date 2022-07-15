class TestStringMethods(unittest.TestCase):
    def setUp(self):
       self.input_a = [6, 7, 9, 10, 11, 12, 12, 12, 12, 15, 18, 18, 25, 25, 28, 37, 37, 39, 42, 42, 44, 45, 47, 50, 52, 54, 54, 57, 66, 67, 69, 70, 71, 73, 73, 74, 75, 79, 80, 81, 82, 84, 85, 88, 89, 90, 94, 94, 95, 98]
       self.result = '-'

    def test_tri(self):
        try :
            self.assertEqual(median(self.input_a),53.0)
        except AssertionError:
            self.result = 'AssertionError'
        except:
            self.result = 'ExceptError'
        finally:
            file_dir =  path + 'unittest_'+str(order)+'.txt'
            f = open(file_dir, 'w+', encoding='UTF-8')
            f.write(self.result)
            f.seek(0)
            f.close()


if __name__ == '__main__':
    unittest.main()