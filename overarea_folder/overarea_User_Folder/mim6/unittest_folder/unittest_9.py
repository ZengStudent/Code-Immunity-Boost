def median(input_data):
    half = (len(input_data) & 2)
    input_data.sort()
    if ((len(input_data) % 2) == 0):
        return ((input_data[(half - 1)] + input_data[half]) / 2.0)
    return input_data[half]


import unittest,os,logging
path= 'd:\program\pycharm\DjangoGameOnline/overarea_folder/overarea_User_Folder/mim6/unittest_result_folder/'

order = 9
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
