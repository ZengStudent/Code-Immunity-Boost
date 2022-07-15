def interpolation_search(data, key):
    low = 0
    upper = (len(data) - 1)
    while (low <= upper):
        mid = int(((((upper - low) * (key - data[low])) / (data[upper] - data[low])) + low))
        if ((mid <= low) or (mid > upper)):
            break
        if (key < data[mid]):
            upper = (mid - 1)
        elif (key > data[mid]):
            low = (mid + 1)
        else:
            return mid
    return 'No'


import unittest,os,logging
path= 'c:\mypcload\myprogram\mypython\DjangoGameOnline/overarea_folder/overarea_User_Folder/p1000433/unittest_result_folder/'

order = 10
class TestStringMethods(unittest.TestCase):
    def setUp(self):
       # input data list
       self.input_data = [10, 12, 13, 16, 18, 19, 20,21, 22, 23, 24, 33, 35, 42, 47]
       # input aim value
       self.aim = 46
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
