
import unittest,os
from overarea_folder.overarea_User_Folder.user_1.mutant_folder import Mutant_2 as mun
path= 'overarea_folder/overarea_User_Folder/user_1/unittest_result_folder/'
order = 2

class TestStringMethods(unittest.TestCase):
    def setUp(self):
       self.test_a = 5
       self.test_b = 5
       self.test_c = 5
       self.result = ''
       print('--------------Setup--------------')

    def test_tri(self):
        print('--------------test_tri--------------')
        try :
            self.assertEqual(mun.tri(self.test_a,self.test_b,self.test_c),'Acute')
            print('Pass')
            self.result='Pass'
        except AssertionError:
            print('Fail')
            self.result = 'Fail'
        except:
            print('Fail')
            self.result = 'Fail'
        finally:
            file_dir =  path + 'unittest_'+str(order)+'.txt'
            f = open(file_dir, 'w+', encoding='UTF-8')
            f.write(self.result)
            f.seek(0)
            f.close() 

if __name__ == '__main__':
    unittest.main()
        