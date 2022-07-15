# Testmachine (一對多)
# OTM
# One Editor To Many Opposites
import os, shutil, time
from threading import Timer
from logic_package.logic_Basic_package import logic_basic as lb
import subprocess

# 繼承於Testmachine
from logic_package.logic_Class_package.testmachine import Testmachine

CORE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class Testmachine_otm(Testmachine):
    # initial
    def __init__(self, username, usercode, contract):
        # 使用者
        self.username = username
        # 使用者的Code
        self.usercode = usercode
        # Contract
        self.contract = contract
        # 合約Oppostites數量
        self.contract_oppositescount = contract.get_oppositescount()
        # 合約 id
        self.contractid = self.contract.get_id()
        # 合約類型
        self.contractcategory = contract.get_category()
        # 合約基本通關條件類型
        self.contentcategory = contract.get_content().get_category()
        # 合約基本通關條件
        self.contentprecent = contract.get_content().get_precent()
        # 合約完美通關條件類型
        self.perfectcategory = contract.get_perfect().get_category()
        # 合約完美通關條件
        self.perfectprecent = contract.get_perfect().get_precent()

        # 使用者的【錯誤】訊息
        self.__errormessage = ''
        # 使用者的【輸出】訊息
        self.__outputmessage = ''

        # 是否編譯成功
        self.__checkcompiler = False
        # 整體完成數值
        self.__completeprecent = 0
        # 是否達到基本通關條件
        self.__checkbasic = False
        # 基本條件數值
        self.__basicprecent = 0
        # 是否達到完美通關條件
        self.__checkadvance = False
        # 完美條件數值
        self.__advanceprecent = 0
        # Square
        self.__squaredict = {}
        # Small Report
        self.__smallreport = {'basic': '', 'advance': ''}


        # Complete Score
        self.__completescore = 0
        # Complete Rank
        self.__completerank = ''
        # Basic Score
        self.__basiccompletescore = {'compiler':0,'basic':0,'score':0}
        # Advance Score
        self.__advancecompletescore = { 'advance': 0,'score':0}
        # Special Score
        self.__speicalcompletescore = {'survived':0,'killed':0,'runtime': {'time':0,'score':0}, 'usememory': {'memory':0,'score':0}}


    # 新建使用者在overarea_User_Folder的所有資料夾
    def __create_user_overarea(self):
        # 使用者在overarea_User_Folder的資料夾路徑
        root_path = CORE_DIR + '/overarea_folder/overarea_User_Folder/' + self.username

        # 新建使用者在overarea_User_Folder的資料夾路徑
        if (os.path.isdir(root_path) == False):
            os.makedirs(root_path)

        # 新建使用者在overarea_User_Folder的mutant資料夾
        if (os.path.isdir(root_path + '/mutant_folder') == False):
            os.makedirs(root_path + '/mutant_folder')

        # 新建使用者在overarea_User_Folder的測試案例資料夾
        if (os.path.isdir(root_path + '/testcase_folder') == False):
            os.makedirs(root_path + '/testcase_folder')

        # 新建使用者在overarea_User_Folder的單元測試py檔案資料夾
        if (os.path.isdir(root_path + '/unittest_folder') == False):
            os.makedirs(root_path + '/unittest_folder')

        # 新建使用者在overarea_User_Folder的執行單元測試py檔案的結果的資料夾
        if (os.path.isdir(root_path + '/unittest_result_folder') == False):
            os.makedirs(root_path + '/unittest_result_folder')

        # 新建使用者在overarea_User_Folder的整體報告資料夾
        if (os.path.isdir(root_path + '/report_folder') == False):
            os.makedirs(root_path + '/report_folder')

        # 新建使用者在overarea_User_Folder的程式碼比較資料夾
        if (os.path.isdir(root_path + '/codecompare_folder') == False):
            os.makedirs(root_path + '/codecompare_folder')

    # 刪除使用者在overarea_User_Folder的所有資料夾
    def __delete_user_overarea(self):
        # 使用者在overarea_User_Folder的資料夾路徑
        root_path = CORE_DIR + '/overarea_folder/overarea_User_Folder/' + self.username

        # 刪除使用者在overarea_User_Folder的資料夾路徑
        if (os.path.isdir(root_path) == True):
            shutil.rmtree(root_path)

    # 讀取Contract的TestCase(Aggression)
    def __read_testcase(self):
        # 使用者的資料夾路徑
        root_path = CORE_DIR + '/overarea_folder/overarea_User_Folder/' + str(self.username)
        # Contract的originalcode路徑
        originalcode_path = CORE_DIR + '/database_folder/database_contract_folder/contract_' + str(
            self.contractid) + '/originalcode/'
        # Contract的questioncode路徑
        questioncode_path = CORE_DIR + '/database_folder/database_contract_folder/contract_' + str(
            self.contractid) + '/questioncode/'

        # 來源位置
        sur = ''
        # 目標位置
        des = ''

        # 複製檔案(Original Code)
        sur = originalcode_path + 'OriginalCode.txt'
        des = root_path + '/mutant_folder/' + 'OriginalCode.py'
        shutil.copyfile(sur, des)

        # 複製檔案(User Code)
        des = root_path + '/mutant_folder/' + 'Mutant.py'
        f = open(des, 'w+', encoding='utf-8')
        f.write(self.usercode)
        f.close()

        # 複製檔案(Testcase)
        for name in os.listdir(questioncode_path):
            sur = questioncode_path + name
            des = root_path + '/testcase_folder/' + name
            shutil.copyfile(sur, des)

        return None

    # 讀取Contract的questioncode(Guard)
    def __read_mutant(self):
        # 使用者的變異體資料夾路徑
        root_path = CORE_DIR + '/overarea_folder/overarea_User_Folder/' + str(self.username)
        # Contract的originalcode路徑
        originalcode_path = CORE_DIR + '/database_folder/database_contract_folder/contract_' + str(
            self.contractid) + '/originalcode/'
        # Contract的questioncode路徑
        questioncode_path = CORE_DIR + '/database_folder/database_contract_folder/contract_' + str(
            self.contractid) + '/questioncode/'
        # 來源位置
        sur = ''
        # 目標位置
        des = ''

        # 複製檔案(Original Code)
        sur = originalcode_path + 'OriginalCode.txt'
        des = root_path + '/mutant_folder/' + 'OriginalCode.py'
        shutil.copyfile(sur, des)

        # 複製檔案(Mutant)
        for name in os.listdir(questioncode_path):
            sur = questioncode_path + name
            des = root_path + '/mutant_folder/' + name
            shutil.copyfile(sur, des)

        # 複製檔案(Testcase)
        des = root_path + '/testcase_folder/' + 'Testcase.py'
        f = open(des, 'w+', encoding='utf-8')
        f.write(self.usercode)
        f.close()

        return None

    # 建立單元測試py檔案(Guard)
    def __create_testcase_guard(self):
        # 變異體資料夾路徑
        user_mutant_path = CORE_DIR + '/overarea_folder/overarea_User_Folder/' + self.username + '/mutant_folder/'
        # 測試案例資料夾路徑
        user_testcase_path = CORE_DIR + '/overarea_folder/overarea_User_Folder/' + self.username + '/testcase_folder'
        # 單元測試py檔案的資料夾路徑
        user_unittest_path = CORE_DIR + '/overarea_folder/overarea_User_Folder/' + self.username + '/unittest_folder/'
        # 執行單元測試py檔案的結果的資料夾路徑
        user_unittest_result_path = '\'' + CORE_DIR + '/overarea_folder/overarea_User_Folder/' + self.username + '/unittest_result_folder/\''
        # 單元測試最後的Finally Code
        user_finally_code_path = CORE_DIR + '/database_folder/database_common_folder/' + 'finally_code.txt'

        # 允許讀取的檔案類型
        allowtype = ['.py']

        import_unittest = '''
import unittest,os,logging
'''

        import_path = 'path= ' + user_unittest_result_path + '\n\n'

        import_order = ''''''

        import_class = ''''''

        import_finally_code = ''

        # 讀取finally code
        ff = open(user_finally_code_path, 'r+', encoding='utf-8')
        import_finally_code = '\n\n' + ff.read() + '\n'
        ff.close()



        # 建立TestCase(Original Code)
        ff = open(user_mutant_path + 'OriginalCode.py', 'r+', encoding='UTF-8')
        import_mutnat = ff.read() + '\n'
        ff.close()
        import_order = 'order = ' + '\'original\'' + '\n'

        file_dir = user_unittest_path + 'unittest_original' + '.py'
        f = open(file_dir, 'w+', encoding='UTF-8')
        # 依照使用者寫入的code，生成單元測試py檔案
        f.write(import_mutnat + import_unittest + import_path + import_order + self.usercode + import_finally_code)
        f.seek(0)
        f.close()



        # 建立TestCase(Mutant)
        for name in os.listdir(user_mutant_path):
            if ('Mutant' not in name):
                continue
            _position = name.find('_')
            ff = open(user_mutant_path + name, encoding='UTF-8')
            import_mutnat = ff.read() + '\n'
            ff.close()
            import_order = 'order = ' + str(name[_position + 1:-3]) + '\n'

            file_dir = user_unittest_path + 'unittest_' + str(name[_position + 1:-3]) + '.py'
            f = open(file_dir, 'w+', encoding='UTF-8')
            # 依照使用者寫入的code，生成單元測試py檔案
            f.write(import_mutnat + import_unittest + import_path + import_order + self.usercode + import_finally_code)
            f.seek(0)
            f.close()

        return None

    # 建立單元測試py檔案(Aggression)
    def __create_testcase_aggression(self):
        # 變異體資料夾路徑
        user_mutant_path = CORE_DIR + '/overarea_folder/overarea_User_Folder/' + self.username + '/mutant_folder/'
        # 測試案例資料夾路徑
        user_testcase_path = CORE_DIR + '/overarea_folder/overarea_User_Folder/' + self.username + '/testcase_folder/'
        # 單元測試py檔案的資料夾路徑
        user_unittest_path = CORE_DIR + '/overarea_folder/overarea_User_Folder/' + self.username + '/unittest_folder/'
        # 執行單元測試py檔案的結果的資料夾路徑
        user_unittest_result_path = '\'' + CORE_DIR + '/overarea_folder/overarea_User_Folder/' + self.username + '/unittest_result_folder/\''
        # 單元測試最後的Finally Code
        user_finally_code_path = CORE_DIR + '/database_folder/database_common_folder/' + 'finally_code.txt'

        # 允許讀取的檔案類型
        allowtype = ['.txt']
        # 計算檔案數量(測試案例)
        user_testcase_number = lb.cal_filenumber(user_testcase_path, allowtype)

        import_unittest = '''
import unittest,os,logging
'''

        import_path = 'path= ' + user_unittest_result_path + '\n'

        import_order = ''''''

        import_class = ''''''

        import_finally_code = ''

        # 讀取finally code
        ff = open(user_finally_code_path, 'r+', encoding='utf-8')
        import_finally_code = '\n\n' + ff.read() + '\n'
        ff.close()

        # 建立TestCase(Original Code)
        ff = open(user_mutant_path + 'OriginalCode.py', 'r+', encoding='UTF-8')
        import_mutnat = ff.read() + '\n'
        ff.close()
        for number in range(1, user_testcase_number + 1):
            t = open(user_testcase_path + 'Testcase_' + str(number) + '.txt', encoding='utf-8')
            import_class = t.read()
            import_order = 'order = \'original_' + str(number) + '\'' + '\n'

            file_dir = user_unittest_path + 'unittest_original_' + str(number) + '.py'
            f = open(file_dir, 'w+', encoding='UTF-8')
            # 測試用
            f.write(import_mutnat + import_unittest + import_path + import_order + import_class + import_finally_code)
            f.seek(0)
            f.close()

        # 建立TestCase(User Code)
        ff = open(user_mutant_path + 'Mutant.py', 'r+', encoding='UTF-8')
        import_mutnat = ff.read() + '\n'
        ff.close()
        for number in range(1, user_testcase_number + 1):
            t = open(user_testcase_path + 'Testcase_' + str(number) + '.txt', encoding='utf-8')
            import_class = t.read()
            import_order = 'order = ' + str(number) + '\n'

            file_dir = user_unittest_path + 'unittest_' + str(number) + '.py'
            f = open(file_dir, 'w+', encoding='UTF-8')
            # 測試用
            f.write(import_mutnat + import_unittest + import_path + import_order + import_class + import_finally_code)
            f.seek(0)
            f.close()

        return None

    # 執行單元測試
    def __do_unittest(self):
        # 單元測試的py檔案路徑
        user_unittest_path = CORE_DIR + '/overarea_folder/overarea_User_Folder/' + self.username + '/unittest_folder/'

        # stdout的結果
        outmessage_list = {}
        # stderr的結果
        errormessage_list = {}
        # 編譯結果(-1:尚未編譯)
        retcode = {}

        # Category:Guard
        if (self.contractcategory == 'G'):
            # 單元測試(Original Code)
            file_dir = user_unittest_path + 'unittest_original.py'

            # 使用subprocess.Popen來執行unittest_original.py
            xxx = open(file_dir)
            print(xxx)
            try:
                f = subprocess.run(["python"], stdin=xxx, stderr=subprocess.PIPE, stdout=subprocess.PIPE, timeout=2.0)
                retcode['unittest_original.py'] = f.returncode
                outmessage_list['unittest_original.py'] = f.stdout.decode('cp950')
                errormessage_list['unittest_original.py'] = f.stderr.decode('cp950')

            except subprocess.TimeoutExpired:
                retcode['unittest_original.py'] = 2
                errpath = CORE_DIR + '/overarea_folder/overarea_User_Folder/' + self.username + '/unittest_result_folder/'
                file_dir = errpath + 'unittest_original.txt'

                # 如果失敗，則不會產生結果文件
                # 預設為是發生While Loop
                # 由於無法抵達TestCase的finally，需在外部自行建立單元測試結果
                f = open(file_dir, 'w+', encoding='UTF-8')
                f.write('infiniteloop')
                f.seek(0)
                f.close()
                outmessage_list['unittest_original.py'] = 'TimeoutExpired'
                errormessage_list['unittest_original.py'] = 'TimeoutExpired'

                file_dir = errpath + 'unittest_expect_original.txt'
                f = open(file_dir, 'w+', encoding='UTF-8')
                f.write('loop')
                f.seek(0)
                f.close()

            # 檢查是否編譯成功
            self.__checkcompiler = self.__do_checkcompiler(retcode)

            # 如果original code不通過編譯
            if (self.__checkcompiler == False):
                self.__do_report(outmessage_list, errormessage_list)
            # 如果original code通過編譯
            elif (self.__checkcompiler == True):
                # 通過編譯分數
                self.__basiccompletescore['compiler'] = 5000
                # 讀取單元測試結果
                user_original_unittest_result_path = CORE_DIR + '/overarea_folder/overarea_User_Folder/' + self.username + '/unittest_result_folder/unittest_original.txt'
                user_original_unittest_expect_path = CORE_DIR + '/overarea_folder/overarea_User_Folder/' + self.username + '/unittest_result_folder/unittest_expect_original.txt'
                # 讀檔(original code)
                with open(user_original_unittest_result_path, 'r', encoding='utf-8') as of:
                    originalresult = of.readline()
                # 讀檔(original expect code)
                with open(user_original_unittest_expect_path, 'r', encoding='utf-8') as of:
                    originalexpect = of.readline()
                # 如果original code的測試結果不為Pass，表示測試失敗，不繼續執行後續步驟
                if (originalresult != originalexpect):
                    outmessage_list['unittest_original.py'] = 'original code is ' + originalresult
                    errormessage_list['unittest_original.py'] = 'original code is ' + originalresult
                    self.__do_report(outmessage_list, errormessage_list)
                    return None
            # 如果original code的測試結果為Pass，表示測試成功，繼續執行後續步驟
            self.__do_report(outmessage_list, errormessage_list)
            self.__do_unittest_common(user_unittest_path)

        # Category:Aggression
        elif (self.contractcategory == 'A'):

            # 單元測試(Original Code)
            for name in os.listdir(user_unittest_path):
                if ('original' not in name):
                    continue
                # 單元測試(Original Code)
                file_dir = user_unittest_path + name

                # 使用subprocess.Popen來執行unittest_original.py
                xxx = open(file_dir)

                try:
                    f = subprocess.run(["python"], stdin=xxx, stderr=subprocess.PIPE, stdout=subprocess.PIPE,
                                       timeout=2.0)
                    retcode[name] = f.returncode
                    outmessage_list[name] = f.stdout.decode('cp950')
                    errormessage_list[name] = f.stderr.decode('cp950')

                except subprocess.TimeoutExpired:
                    retcode[name] = 2
                    errpath = CORE_DIR + '/overarea_folder/overarea_User_Folder/' + self.username + '/unittest_result_folder/'
                    file_dir = errpath + 'unittest_original.txt'

                    # 如果失敗，則不會產生結果文件
                    # 預設為是發生While Loop
                    # 由於無法抵達TestCase的finally，需在外部自行建立單元測試結果
                    f = open(file_dir, 'w+', encoding='UTF-8')
                    f.write('infiniteloop')
                    f.seek(0)
                    f.close()
                    outmessage_list[name] = 'TimeoutExpired'
                    errormessage_list[name] = 'TimeoutExpired'



                    file_dir = errpath + 'unittest_expect_original.txt'
                    f = open(file_dir, 'w+', encoding='UTF-8')
                    f.write('loop')
                    f.seek(0)
                    f.close()

                # 檢查是否編譯成功
                self.__checkcompiler = self.__do_checkcompiler(retcode)

                # 如果original code不通過編譯
                if (self.__checkcompiler == False):
                    self.__do_report(outmessage_list, errormessage_list)

                # 如果original code通過編譯
                elif (self.__checkcompiler == True):
                    # 通過編譯分數
                    self.__basiccompletescore['compiler'] = 5000
                    #
                    rightposition = name.rfind('_')
                    # 讀取單元測試結果
                    user_original_unittest_result_path = CORE_DIR + '/overarea_folder/overarea_User_Folder/' + self.username + '/unittest_result_folder/' + 'unittest_original_' + name[
                                                                                                                                                                                   rightposition + 1:-3] + '.txt'
                    user_original_unittest_expect_path = CORE_DIR + '/overarea_folder/overarea_User_Folder/' + self.username + '/unittest_result_folder/' + 'unittest_expect_original_' + name[
                                                                                                                                                                                          rightposition + 1:-3] + '.txt'
                    # 讀檔(original code)
                    with open(user_original_unittest_result_path, 'r', encoding='utf-8') as of:
                        originalresult = of.readline()
                    # 讀檔(original expect code)
                    with open(user_original_unittest_expect_path, 'r', encoding='utf-8') as of:
                        originalexpect = of.readline()
                    # 如果original code的測試結果不為Pass，表示測試失敗，不繼續執行後續步驟
                    if (originalresult != originalexpect):
                        outmessage_list[name] = name[:-3] + ' code is ' + originalresult
                        errormessage_list[name] = name[:-3] + ' code is ' + originalresult
                        self.__do_report(outmessage_list, errormessage_list)
                        return None

            # 如果original code的測試結果為Pass，表示測試成功，繼續執行後續步驟
            self.__do_report(outmessage_list, errormessage_list)
            self.__do_unittest_common(user_unittest_path)

        return None

    # unittest共通部份
    def __do_unittest_common(self, unittest_path):
        # stdout的結果
        outmessage_list = {}
        # stderr的結果
        errormessage_list = {}
        # 編譯結果(-1:尚未編譯)
        retcode = {}

        # 進行單元測試
        for name in os.listdir(unittest_path):
            # 不要測試unittest_original.py
            if ("original" in name):
                continue
            file_dir = unittest_path + name
            xxx = open(file_dir)
            # 使用subprocess.run
            try:
                f = subprocess.run(["python"], stdin=xxx, stderr=subprocess.PIPE, stdout=subprocess.PIPE, timeout=2.0)
                retcode[name] = f.returncode
                outmessage_list[name] = f.stdout.decode('cp950')
                errormessage_list[name] = f.stderr.decode('cp950')
            except subprocess.TimeoutExpired:
                retcode[name] = 2
                errpath = CORE_DIR + '/overarea_folder/overarea_User_Folder/' + self.username + '/unittest_result_folder/'
                file_dir = errpath + str(name)[:-3] + '.txt'

                # 如果失敗，則不會產生結果文件
                # 預設為是發生While Loop
                # 由於無法抵達TestCase的finally，需在外部自行建立單元測試結果
                f = open(file_dir, 'w+', encoding='UTF-8')
                f.write('infiniteloop')
                f.seek(0)
                f.close()
                outmessage_list[name] = 'TimeoutExpired'
                errormessage_list[name] = 'TimeoutExpired'

                name = name[:-3]
                name = name.replace('unittest_','')
                file_dir = errpath  + 'unittest_expect_' + str(name) + '.txt'
                f = open(file_dir, 'w+', encoding='UTF-8')
                f.write('loop')
                f.seek(0)
                f.close()

        # 檢查是否編譯成功
        self.__checkcompiler = self.__do_checkcompiler(retcode)

        #
        self.__do_report(outmessage_list, errormessage_list)
        # 如果編譯成功，檢查是否達到通關條件
        if (self.__checkcompiler == True):
            self.__do_checkcontract()

        return None

    # 整體報告
    def __do_report(self, out, err):
        # 整體報告路徑
        user_report_path = CORE_DIR + '/overarea_folder/overarea_User_Folder/' + self.username + '/report_folder'

        # 寫入【輸出】結果
        file_dir = user_report_path + '/outputmessage.txt'
        for name, content in out.items():
            f = open(file_dir, 'a+', encoding='UTF-8')
            f.write(name + '\n' + content + '\n')
            f.close()
            self.__outputmessage = self.__outputmessage + name + '\n' + str(content) + '\n\n'

        # 寫入【錯誤】結果
        file_dir = user_report_path + '/errormessage.txt'
        for name, content in err.items():
            f = open(file_dir, 'a+', encoding='UTF-8')
            f.write(name + '\n' + content + '\n')
            f.close()
            self.__errormessage = self.__errormessage + name + '\n' + str(content) + '\n\n'

        return None

    # 檢查是否編譯成功(checkcode:檢查碼，0=Compiler Success，非0整數=Compiler Fail)
    def __do_checkcompiler(self, checkcode):
        for name, content in checkcode.items():
            # 如果任何一項編譯失敗
            if (content != 0 and content!=2):
                print(checkcode, 'Compiler Fail')
                return False
        print(checkcode, 'Compiler Success!!!!')
        # 全部編譯成功
        return True

    # 檢查是否達到通關條件(統整)
    def __do_checkcontract(self):

        # 檢查是否達到通關條件(基本)
        self.__checkbasic = self.__do_checkcontract_basic()
        # 檢查是否達到通關條件(完美)
        if(self.__checkbasic == True):
            self.__checkadvance = self.__do_checkcontract_advance()

        return None

    # 檢查是否達到通關條件(基本)
    def __do_checkcontract_basic(self):
        if (self.contractcategory == 'G'):
            if (self.contentcategory == 'ut'):
                return self.__do_checkcontract_basic_guard_ut()
            elif (self.contentcategory == 'cov'):
                return self.__do_checkcontract_basic_guard_cov()
            elif (self.contentcategory == 'ms'):
                return self.__do_checkcontract_basic_guard_ms()
            else:
                print('testmachine_mto ||| __do_checkcontract_basic Guard Mistake!!!')
        elif (self.contractcategory == 'A'):
            if (self.contentcategory == 'ut'):
                return self.__do_checkcontract_basic_Aggression_ut()
            elif (self.contentcategory == 'cov'):
                return self.__do_checkcontract_basic_Aggression_cov()
            elif (self.contentcategory == 'ms'):
                return self.__do_checkcontract_basic_Aggression_ms()
            else:
                print('testmachine_mto ||| __do_checkcontract_basic Aggression Mistake!!!')
        else:
            print('testmachine_mto ||| __do_checkcontract_basic Mistake!!!')
        return None

    # 檢查是否達到通關條件(基本，Guard，Unittest)
    def __do_checkcontract_basic_guard_ut(self):
        print('contentcategory guard')

        # 讀取單元測試結果
        user_unittest_path = CORE_DIR + '/overarea_folder/overarea_User_Folder/' + self.username + '/unittest_result_folder/'
        # 允許讀取的檔案類型
        allowtype = ['.txt']
        # 計算檔案數量
        numbers = lb.cal_filenumber(user_unittest_path, allowtype)

        originalresult = ''
        # killed數量
        local_killed = 0
        # nokilled數量
        local_nokilled = 0

        # 讀檔(original code)
        file_path = user_unittest_path + 'unittest_original.txt'
        with open(file_path, 'r', encoding='utf-8') as of:
            originalresult = of.readline()

        # 讀檔(others)
        for i in range(1, numbers):
            file_path = user_unittest_path + 'unittest_' + str(i) + '.txt'
            if os.path.isfile(file_path) == False:
                continue
            self.__squaredict['unittest_' + str(i)] = {'usercodename': '', 'originalcodename': '', 'mutantcodename': '',
                                                       'scorecodename': ''}
            with open(file_path, 'r', encoding='utf-8') as f:
                result = f.readline()
                # 結果相同
                if (result == originalresult):
                    local_nokilled = local_nokilled + 1
                    self.__squaredict['unittest_' + str(i)]['usercodename'] = str(i)
                    self.__squaredict['unittest_' + str(i)]['originalcodename'] = originalresult
                    self.__squaredict['unittest_' + str(i)]['mutantcodename'] = result
                    self.__squaredict['unittest_' + str(i)]['scorecodename'] = '---'
                    self.__speicalcompletescore['survived'] = self.__speicalcompletescore['survived'] - 2500
                # 結果不同
                else:
                    local_killed = local_killed + 1
                    self.__squaredict['unittest_' + str(i)]['usercodename'] = str(i)
                    self.__squaredict['unittest_' + str(i)]['originalcodename'] = originalresult
                    self.__squaredict['unittest_' + str(i)]['mutantcodename'] = result
                    self.__squaredict['unittest_' + str(i)]['scorecodename'] = '+++'
                    self.__speicalcompletescore['killed'] =  self.__speicalcompletescore['killed'] + 2500

        self.__basicprecent = (local_killed / self.contract_oppositescount) * 100.0

        # Small Report
        self.__smallreport['basic'] = '完成度【基本】\n測試案例總共發現變異體 : ' + str(local_killed) + ' 個\n'
        self.__smallreport['basic'] = self.__smallreport['basic'] + '本關卡要找出 : ' + str(
            int(self.contract_oppositescount * (self.contentprecent / 100.0))) + ' 個變異體\n'
        self.__smallreport['basic'] = self.__smallreport['basic'] + '本次得分為 : ' + str(local_killed) + ' / ' + str(
            int(self.contract_oppositescount * (self.contentprecent / 100.0))) + ' = '

        if (self.__basicprecent >= self.contentprecent):
            self.__basicprecent = self.__basicprecent / (self.contentprecent / 100.0)
            self.__smallreport['basic'] = self.__smallreport['basic'] + str(self.__basicprecent) + '(超過100%，視為100%)\n'
            if (self.__basicprecent >= 100.0): self.__basicprecent = 100.0
            self.__checkbasic = True
            # 通過基本條件分數
            self.__basiccompletescore['basic'] = 10000
            print('Basic Pass.')
            return True
        else:
            self.__basicprecent = self.__basicprecent / (self.contentprecent / 100.0)
            self.__smallreport['basic'] = self.__smallreport['basic'] + str(self.__basicprecent) + '(超過100%，視為100%)\n'
            self.__checkbasic = False
            print('Basic Fail.')
            return False

    # 檢查是否達到通關條件(基本，Guard，Coverage)
    def __do_checkcontract_basic_guard_cov(self):
        return None

    # 檢查是否達到通關條件(基本，Guard，MutationScore)
    def __do_checkcontract_basic_guard_ms(self):
        print('contentcategory guard')

        # 讀取單元測試結果
        user_unittest_path = CORE_DIR + '/overarea_folder/overarea_User_Folder/' + self.username + '/unittest_result_folder/'
        # 允許讀取的檔案類型
        allowtype = ['.txt']
        # 計算檔案數量
        numbers = lb.cal_filenumber(user_unittest_path, allowtype)

        originalresult = ''
        # killed數量
        local_killed = 0
        # nokilled數量
        local_nokilled = 0

        # 讀檔(original code)
        file_path = user_unittest_path + 'unittest_original.txt'
        with open(file_path, 'r', encoding='utf-8') as of:
            originalresult = of.readline()

        # 讀檔(others)
        for i in range(1, numbers):
            file_path = user_unittest_path + 'unittest_' + str(i) + '.txt'
            if os.path.isfile(file_path) == False:
                continue
            self.__squaredict['unittest_' + str(i)] = {'usercodename': '', 'originalcodename': '', 'mutantcodename': '',
                                                       'scorecodename': ''}
            with open(file_path, 'r', encoding='utf-8') as f:
                result = f.readline()
                # 結果相同
                if (result == originalresult):
                    local_nokilled = local_nokilled + 1
                    self.__squaredict['unittest_' + str(i)]['usercodename'] = str(i)
                    self.__squaredict['unittest_' + str(i)]['originalcodename'] = originalresult
                    self.__squaredict['unittest_' + str(i)]['mutantcodename'] = result
                    self.__squaredict['unittest_' + str(i)]['scorecodename'] = '---'
                    self.__speicalcompletescore['survived'] = self.__speicalcompletescore['survived'] - 2500
                # 結果不同
                else:
                    local_killed = local_killed + 1
                    self.__squaredict['unittest_' + str(i)]['usercodename'] = str(i)
                    self.__squaredict['unittest_' + str(i)]['originalcodename'] = originalresult
                    self.__squaredict['unittest_' + str(i)]['mutantcodename'] = result
                    self.__squaredict['unittest_' + str(i)]['scorecodename'] = '+++'
                    self.__speicalcompletescore['killed'] = self.__speicalcompletescore['killed'] + 2500

        self.__basicprecent = (local_killed / self.contract_oppositescount) * 100.0

        # Small Report
        self.__smallreport['basic'] = '完成度【基本】\n測試案例總共殺死變異體 : ' + str(local_killed) + ' 個\n'
        self.__smallreport['basic'] = self.__smallreport['basic'] + '本關卡要變異分數達 : ' + str(
            self.contentprecent) + '%' + '\n'
        self.__smallreport['basic'] = self.__smallreport['basic'] + '本次變異分數為 : ' + str(local_killed) + ' / ' + str(
            self.contract_oppositescount) + ' = '

        if (self.__basicprecent >= self.contentprecent):
            self.__basicprecent = self.__basicprecent / (self.contentprecent / 100.0)
            self.__smallreport['basic'] = self.__smallreport['basic'] + str((local_killed / self.contract_oppositescount) * 100.0) + '%' + '\n'
            self.__smallreport['basic'] = self.__smallreport['basic'] + '該關卡完成度【基本】為 ' + str((local_killed / (self.contract_oppositescount * (self.contentprecent / 100.0))) * 100.0) + '(超過100%，視為100%)\n'
            self.__basiccompletescore['score'] = str((local_killed / self.contract_oppositescount) * 100.0) + '%'
            self.__completeprecent = ((local_killed / self.contract_oppositescount) * 100.0)
            if (self.__basicprecent >= 100.0):
                self.__basicprecent = 100.0
            self.__checkbasic = True
            # 通過基本條件分數
            self.__basiccompletescore['basic'] = 10000
            print('Basic Pass.')
            return True
        else:
            self.__basicprecent = self.__basicprecent / (self.contentprecent / 100.0)
            self.__smallreport['basic'] = self.__smallreport['basic'] + str(
                (local_killed / self.contract_oppositescount) * 100.0) + '%' + '\n'
            self.__smallreport['basic'] = self.__smallreport['basic'] + '該關卡完成度【基本】為 ' + str((local_killed / (
                        self.contract_oppositescount * (self.contentprecent / 100.0))) * 100.0) + '(超過100%，視為100%)\n'
            self.__completeprecent = ((local_killed / self.contract_oppositescount) * 100.0)
            self.__checkbasic = False
            print('Basic Fail.')
            return False

    # 檢查是否達到通關條件(基本，Aggression，Unittest)
    def __do_checkcontract_basic_Aggression_ut(self):
        print('contentcategory Aggression')
        # 測試案例資料夾路徑
        user_testcase_path = CORE_DIR + '/overarea_folder/overarea_User_Folder/' + self.username + '/testcase_folder/'
        # 讀取單元測試結果
        user_unittest_path = CORE_DIR + '/overarea_folder/overarea_User_Folder/' + self.username + '/unittest_result_folder/'

        originalresult = []
        normalresult = []
        # killed數量
        local_killed = 0
        # nokilled數量
        local_nokilled = 0

        # 讀檔(結果)
        for name in os.listdir(user_unittest_path):

            f = open(user_unittest_path + name, 'r', encoding='utf-8')
            # (original)
            if (('original' in name) and ('expect' not in name)):
                originalresult.append(f.read())
            # (normal)
            elif (('original' not in name) and ('expect' not in name)):
                normalresult.append(f.read())
            f.close()

        # 比較結果
        for index in range(0, len(originalresult)):
            self.__squaredict['unittest_' + str(index + 1)] = {'usercodename': '', 'originalcodename': '',
                                                               'mutantcodename': '', 'scorecodename': ''}
            # 結果相同
            if (originalresult[index] == normalresult[index]):
                local_nokilled = local_nokilled + 1
                self.__squaredict['unittest_' + str(index + 1)]['usercodename'] = str(index + 1)
                self.__squaredict['unittest_' + str(index + 1)]['originalcodename'] = originalresult[index]
                self.__squaredict['unittest_' + str(index + 1)]['mutantcodename'] = normalresult[index]
                self.__squaredict['unittest_' + str(index + 1)]['scorecodename'] = '+++'
                self.__speicalcompletescore['survived'] = self.__speicalcompletescore['survived'] + 2500
            # 結果不同
            else:
                local_killed = local_killed + 1
                self.__squaredict['unittest_' + str(index + 1)]['usercodename'] = str(index + 1)
                self.__squaredict['unittest_' + str(index + 1)]['originalcodename'] = originalresult[index]
                self.__squaredict['unittest_' + str(index + 1)]['mutantcodename'] = normalresult[index]
                self.__squaredict['unittest_' + str(index + 1)]['scorecodename'] = '---'
                self.__speicalcompletescore['killed'] = self.__speicalcompletescore['killed'] - 2500

        self.__basicprecent = (local_nokilled / self.contract_oppositescount) * 100.0

        # Small Report
        self.__smallreport['basic'] = '完成度【基本】\n變異體總共沒有被 : ' + str(local_nokilled) + ' 個測試案例發現錯誤\n'
        self.__smallreport['basic'] = self.__smallreport['basic'] + '本關卡要不被 : ' + str(
            int(self.contract_oppositescount * (self.contentprecent / 100.0))) + ' 個測試案例發現錯誤\n'
        self.__smallreport['basic'] = self.__smallreport['basic'] + '本次得分為 : ' + str(local_nokilled) + ' / ' + str(
            int(self.contract_oppositescount * (self.contentprecent / 100.0))) + ' = '

        if (self.__basicprecent >= self.contentprecent):
            self.__basicprecent = self.__basicprecent / (self.contentprecent / 100.0)
            self.__smallreport['basic'] = self.__smallreport['basic'] + str(self.__basicprecent) + '(超過100%，視為100%)\n'
            if (self.__basicprecent >= 100.0): self.__basicprecent = 100.0
            self.__checkbasic = True
            # 通過基本條件分數
            self.__basiccompletescore['basic'] = 10000
            print('Basic Pass.')
            return True
        else:
            self.__basicprecent = self.__basicprecent / (self.contentprecent / 100.0)
            self.__smallreport['basic'] = self.__smallreport['basic'] + str(self.__basicprecent) + '(超過100%，視為100%)\n'
            self.__checkbasic = False
            print('Basic Fail.')
            return False

    # 檢查是否達到通關條件(基本，Aggression，Coverage)
    def __do_checkcontract_basic_Aggression_cov(self):
        return None

    # 檢查是否達到通關條件(基本，Aggression，MutationScore)
    def __do_checkcontract_basic_Aggression_ms(self):
        print('contentcategory Aggression')

        # 測試案例資料夾路徑
        user_testcase_path = CORE_DIR + '/overarea_folder/overarea_User_Folder/' + self.username + '/testcase_folder/'
        # 讀取單元測試結果
        user_unittest_path = CORE_DIR + '/overarea_folder/overarea_User_Folder/' + self.username + '/unittest_result_folder/'

        originalresult = []
        normalresult = []
        # killed數量
        local_killed = 0
        # nokilled數量
        local_nokilled = 0

        # 讀檔(結果)
        for name in os.listdir(user_unittest_path):

            f = open(user_unittest_path + name, 'r', encoding='utf-8')
            # (original)
            if (('original' in name) and ('expect' not in name)):
                originalresult.append(f.read())
            # (normal)
            elif (('original' not in name) and ('expect' not in name)):
                normalresult.append(f.read())
            f.close()

        # 比較結果
        for index in range(0, len(originalresult)):
            self.__squaredict['unittest_' + str(index + 1)] = {'usercodename': '', 'originalcodename': '',
                                                               'mutantcodename': '', 'scorecodename': ''}
            # 結果相同
            if (originalresult[index] == normalresult[index]):
                local_nokilled = local_nokilled + 1
                self.__squaredict['unittest_' + str(index + 1)]['usercodename'] = str(index + 1)
                self.__squaredict['unittest_' + str(index + 1)]['originalcodename'] = originalresult[index]
                self.__squaredict['unittest_' + str(index + 1)]['mutantcodename'] = normalresult[index]
                self.__squaredict['unittest_' + str(index + 1)]['scorecodename'] = '+++'
                self.__speicalcompletescore['survived'] = self.__speicalcompletescore['survived'] + 2500
            # 結果不同
            else:
                local_killed = local_killed + 1
                self.__squaredict['unittest_' + str(index + 1)]['usercodename'] = str(index + 1)
                self.__squaredict['unittest_' + str(index + 1)]['originalcodename'] = originalresult[index]
                self.__squaredict['unittest_' + str(index + 1)]['mutantcodename'] = normalresult[index]
                self.__squaredict['unittest_' + str(index + 1)]['scorecodename'] = '---'
                self.__speicalcompletescore['killed'] = self.__speicalcompletescore['killed'] - 2500

        self.__basicprecent = (local_nokilled / self.contract_oppositescount) * 100.0

        # Small Report
        self.__smallreport['basic'] = '完成度【基本】\n總共有變異體 : ' + str(local_killed) + ' 個被測試案例發現錯誤\n'
        self.__smallreport['basic'] = self.__smallreport['basic'] + '本關卡脆弱值要低於 : ' + str(
            self.contentprecent/100.0) +  '\n'
        self.__smallreport['basic'] = self.__smallreport['basic'] + '本次脆弱值為 : ' + str(local_killed) + ' / ' + str(self.contract_oppositescount) + ' = '

        if (self.__basicprecent >= self.contentprecent):
            self.__basicprecent = self.__basicprecent / (self.contentprecent / 100.0)
            self.__smallreport['basic'] = self.__smallreport['basic'] + str(((local_killed / self.contract_oppositescount)) * 100.0)  + '\n'
            self.__basiccompletescore['score'] = str(((local_killed / self.contract_oppositescount)) * 100.0)
            try:
                self.__smallreport['basic'] = self.__smallreport['basic'] + '該關卡完成度【基本】為 ' + str((self.contentprecent / ((local_killed / self.contract_oppositescount)))) + '(超過100%，視為100%)\n'
            except ZeroDivisionError:
                self.__smallreport['basic'] = self.__smallreport['basic'] + '該關卡完成度【基本】為 ' + str((self.contentprecent / 1.0) * 100.0) + '(超過100%，視為100%)\n'
            self.__completeprecent = (((local_killed / self.contract_oppositescount)) * 100.0)
            if (self.__basicprecent >= 100.0):
                self.__basicprecent = 100.0
            self.__checkbasic = True
            # 通過基本條件分數
            self.__basiccompletescore['basic'] = 10000
            print('Basic Pass.')
            return True
        else:
            self.__basicprecent = self.__basicprecent / (self.contentprecent / 100.0)
            self.__smallreport['basic'] = self.__smallreport['basic'] + str(((local_killed / self.contract_oppositescount)) * 100.0) + '\n'
            try:
                self.__smallreport['basic'] = self.__smallreport['basic'] + '該關卡完成度【基本】為 ' + str((self.contentprecent / ((local_killed / self.contract_oppositescount)))) + '(超過100%，視為100%)\n'
            except ZeroDivisionError:
                self.__smallreport['basic'] = self.__smallreport['basic'] + '該關卡完成度【基本】為 ' + str((self.contentprecent / 1.0) * 100.0) + '(超過100%，視為100%)\n'
            self.__completeprecent = (((local_killed / self.contract_oppositescount)) * 100.0)
            self.__checkbasic = False
            print('Basic Fail.')
            return False

    # 檢查是否達到通關條件(完美)
    def __do_checkcontract_advance(self):
        if (self.contractcategory == 'G'):
            if (self.perfectcategory == 'ut'):
                return self.__do_checkcontract_advance_guard_ut()
            elif (self.perfectcategory == 'cov'):
                return self.__do_checkcontract_advance_guard_cov()
            elif (self.perfectcategory == 'ms'):
                return self.__do_checkcontract_advance_guard_ms()
            else:
                print('testmachine_mto ||| __do_checkcontract_advance Guard Mistake!!!')
        elif (self.contractcategory == 'A'):
            if (self.perfectcategory == 'ut'):
                return self.__do_checkcontract_advance_Aggression_ut()
            elif (self.perfectcategory == 'cov'):
                return self.__do_checkcontract_advance_Aggression_cov()
            elif (self.perfectcategory == 'ms'):
                return self.__do_checkcontract_advance_Aggression_ms()
            else:
                print('testmachine_mto ||| __do_checkcontract_advance Aggression Mistake!!!')
        else:
            print('testmachine_mto ||| __do_checkcontract_advance Mistake!!!')
        return None

    # 檢查是否達到通關條件(完美，Guard，Unittest)
    def __do_checkcontract_advance_guard_ut(self):
        print('perfectcategory guard')

        # 讀取單元測試結果
        user_unittest_path = CORE_DIR + '/overarea_folder/overarea_User_Folder/' + self.username + '/unittest_result_folder/'

        # 允許讀取的檔案類型
        allowtype = ['.txt']
        # 計算檔案數量
        numbers = lb.cal_filenumber(user_unittest_path, allowtype)

        originalresult = ''
        # killed數量
        local_killed = 0
        # nokilled數量
        local_nokilled = 0

        # 讀檔(original code)
        file_path = user_unittest_path + 'unittest_original.txt'
        with open(file_path, 'r', encoding='utf-8') as of:
            originalresult = of.readline()

        # 讀檔(others)
        for i in range(1, numbers):
            file_path = user_unittest_path + 'unittest_' + str(i) + '.txt'
            if os.path.isfile(file_path) == False:
                continue
            with open(file_path, 'r', encoding='utf-8') as f:
                result = f.readline()
                if (result == originalresult):
                    local_nokilled = local_nokilled + 1
                else:
                    local_killed = local_killed + 1

        self.__advanceprecent = (local_killed / self.contract_oppositescount) * 100.0

        # Small Report
        self.__smallreport['advance'] = '\n\n完成度【進階】\n測試案例總共發現變異體 : ' + str(local_killed) + ' 個\n'
        self.__smallreport['advance'] = self.__smallreport['advance'] + '本關卡要找出 : ' + str(
            int(self.contract_oppositescount * (self.perfectprecent / 100.0))) + ' 個變異體\n'
        self.__smallreport['advance'] = self.__smallreport['advance'] + '本次得分為 : ' + str(local_killed) + ' / ' + str(
            int(self.contract_oppositescount * (self.perfectprecent / 100.0))) + ' = '

        if (self.__advanceprecent >= self.perfectprecent):
            self.__advanceprecent = self.__advanceprecent / (self.perfectprecent / 100.0)
            self.__smallreport['advance'] = self.__smallreport['advance'] + str(
                self.__advanceprecent) + '(超過100%，視為100%)\n'
            if (self.__advanceprecent >= 100.0): self.__advanceprecent = 100.0
            self.__checkadvance = True
            print('Advance Pass.')
            # 通過進階條件分數
            self.__advancecompletescore['advance'] = 10000
            return True
        else:
            self.__advanceprecent = self.__advanceprecent / (self.perfectprecent / 100.0)
            self.__smallreport['advance'] = self.__smallreport['advance'] + str(
                self.__advanceprecent) + '(超過100%，視為100%)\n'
            self.__checkadvance = False
            print('Advance Fail.')
            return False

    # 檢查是否達到通關條件(完美，Guard，Coverage)
    def __do_checkcontract_advance_guard_cov(self):
        return None

    # 檢查是否達到通關條件(完美，Guard，MutationScore)
    def __do_checkcontract_advance_guard_ms(self):
        print('perfectcategory guard')

        # 讀取單元測試結果
        user_unittest_path = CORE_DIR + '/overarea_folder/overarea_User_Folder/' + self.username + '/unittest_result_folder/'

        # 允許讀取的檔案類型
        allowtype = ['.txt']
        # 計算檔案數量
        numbers = lb.cal_filenumber(user_unittest_path, allowtype)

        originalresult = ''
        # killed數量
        local_killed = 0
        # nokilled數量
        local_nokilled = 0

        # 讀檔(original code)
        file_path = user_unittest_path + 'unittest_original.txt'
        with open(file_path, 'r', encoding='utf-8') as of:
            originalresult = of.readline()

        # 讀檔(others)
        for i in range(1, numbers):
            file_path = user_unittest_path + 'unittest_' + str(i) + '.txt'
            if os.path.isfile(file_path) == False:
                continue
            with open(file_path, 'r', encoding='utf-8') as f:
                result = f.readline()
                if (result == originalresult):
                    local_nokilled = local_nokilled + 1
                else:
                    local_killed = local_killed + 1

        self.__advanceprecent = (local_killed / self.contract_oppositescount) * 100.0

        # Small Report
        self.__smallreport['advance'] = '完成度【進階】\n測試案例總共殺死變異體 : ' + str(local_killed) + ' 個\n'
        self.__smallreport['advance'] = self.__smallreport['advance'] + '本關卡要變異分數達 : ' + str(
            self.perfectprecent) + '%' + '\n'
        self.__smallreport['advance'] = self.__smallreport['advance'] + '本次變異分數為 : ' + str(local_killed) + ' / ' + str(
            self.contract_oppositescount) + ' = '

        if (self.__advanceprecent >= self.perfectprecent):
            self.__advanceprecent = self.__advanceprecent / (self.perfectprecent / 100.0)
            self.__smallreport['advance'] = self.__smallreport['advance'] + str( (local_killed / self.contract_oppositescount) * 100.0) + '%' + '\n'
            self.__smallreport['advance'] = self.__smallreport['advance'] + '該關卡完成度【進階】為 ' + str((local_killed / (self.contract_oppositescount * (self.perfectprecent / 100.0))) * 100.0) + '(超過100%，視為100%)\n'
            self.__advancecompletescore['score'] = str( (local_killed / self.contract_oppositescount) * 100.0) + '%'
            self.__completeprecent = ((local_killed / self.contract_oppositescount) * 100.0)
            if (self.__advanceprecent >= 100.0):
                self.__advanceprecent = 100.0
            self.__checkadvance = True
            # 通過進階條件分數
            self.__advancecompletescore['advance'] = 10000
            print('Advance Pass.')
            return True
        else:
            self.__advanceprecent = self.__advanceprecent / (self.perfectprecent / 100.0)
            self.__smallreport['advance'] = self.__smallreport['advance'] + str((local_killed / self.contract_oppositescount) * 100.0) + '%' + '\n'
            self.__smallreport['advance'] = self.__smallreport['advance'] + '該關卡完成度【進階】為 ' + str((local_killed / (self.contract_oppositescount * (self.perfectprecent / 100.0))) * 100.0) + '(超過100%，視為100%)\n'
            self.__completeprecent = ((local_killed / self.contract_oppositescount) * 100.0)
            self.__checkadvance = False
            print('Advance Fail.')
            return False

    # 檢查是否達到通關條件(完美，Aggression，Unittest)
    def __do_checkcontract_advance_Aggression_ut(self):
        print('contentcategory Aggression')

        # 測試案例資料夾路徑
        user_testcase_path = CORE_DIR + '/overarea_folder/overarea_User_Folder/' + self.username + '/testcase_folder/'
        # 讀取單元測試結果
        user_unittest_path = CORE_DIR + '/overarea_folder/overarea_User_Folder/' + self.username + '/unittest_result_folder/'

        originalresult = []
        normalresult = []
        # killed數量
        local_killed = 0
        # nokilled數量
        local_nokilled = 0

        # 讀檔(結果)
        for name in os.listdir(user_unittest_path):
            f = open(user_unittest_path + name, 'r', encoding='utf-8')
            # (original)
            if (('original' in name) and ('expect' not in name)):
                originalresult.append(f.read())
            # (normal)
            elif (('original' not in name) and ('expect' not in name)):
                normalresult.append(f.read())
            f.close()

        # 比較結果
        for index in range(0, len(originalresult)):
            if (originalresult[index] == normalresult[index]):
                local_nokilled = local_nokilled + 1
            else:
                local_killed = local_killed + 1

        self.__advanceprecent = (local_nokilled / self.contract_oppositescount) * 100.0

        # Small Report
        self.__smallreport['advance'] = '\n\n完成度【進階】\n變異體總共沒有被 : ' + str(local_nokilled) + ' 個測試案例發現錯誤\n'
        self.__smallreport['advance'] = self.__smallreport['advance'] + '本關卡要不被 : ' + str(
            int(self.contract_oppositescount * (self.perfectprecent / 100.0))) + ' 個測試案例發現錯誤\n'
        self.__smallreport['advance'] = self.__smallreport['advance'] + '本次得分為 : ' + str(local_nokilled) + ' / ' + str(
            int(self.contract_oppositescount * (self.perfectprecent / 100.0))) + ' = '

        if (self.__advanceprecent >= self.perfectprecent):
            self.__advanceprecent = self.__advanceprecent / (self.perfectprecent / 100.0)
            self.__smallreport['advance'] = self.__smallreport['advance'] + str(
                self.__advanceprecent) + '(超過100%，視為100%)\n'
            if (self.__advanceprecent >= 100.0): self.__advanceprecent = 100.0
            self.__checkadvance = True
            # 通過進階條件分數
            self.__advancecompletescore['advance'] = 10000
            print('Advance Pass.')
            return True
        else:
            self.__advanceprecent = self.__advanceprecent / (self.perfectprecent / 100.0)
            self.__smallreport['advance'] = self.__smallreport['advance'] + str(
                self.__advanceprecent) + '(超過100%，視為100%)\n'
            self.__checkadvance = False
            print('Advance Fail.')
            return False

    # 檢查是否達到通關條件(完美，Aggression，Coverage)
    def __do_checkcontract_advance_Aggression_cov(self):
        return None

    # 檢查是否達到通關條件(完美，Aggression，MutationScore)
    def __do_checkcontract_advance_Aggression_ms(self):
        print('contentcategory Aggression')

        # 測試案例資料夾路徑
        user_testcase_path = CORE_DIR + '/overarea_folder/overarea_User_Folder/' + self.username + '/testcase_folder/'
        # 讀取單元測試結果
        user_unittest_path = CORE_DIR + '/overarea_folder/overarea_User_Folder/' + self.username + '/unittest_result_folder/'

        originalresult = []
        normalresult = []
        # killed數量
        local_killed = 0
        # nokilled數量
        local_nokilled = 0

        # 讀檔(結果)
        for name in os.listdir(user_unittest_path):
            f = open(user_unittest_path + name, 'r', encoding='utf-8')
            # (original)
            if (('original' in name) and ('expect' not in name)):
                originalresult.append(f.read())
            # (normal)
            elif (('original' not in name) and ('expect' not in name)):
                normalresult.append(f.read())
            f.close()

        # 比較結果
        for index in range(0, len(originalresult)):
            if (originalresult[index] == normalresult[index]):
                local_nokilled = local_nokilled + 1
            else:
                local_killed = local_killed + 1

        self.__advanceprecent = (local_nokilled / self.contract_oppositescount) * 100.0

        # Small Report
        self.__smallreport['advance'] = '完成度【進階】\n總共有變異體 : ' + str(local_killed) + ' 個被測試案例發現錯誤\n'
        self.__smallreport['advance'] = self.__smallreport['advance'] + '本關卡脆弱值要低於 : ' + str(
            self.perfectprecent/100.0) +  '\n'
        self.__smallreport['advance'] = self.__smallreport['advance'] + '本次脆弱值為 : ' + str(local_killed) + ' / ' + str(self.contract_oppositescount) + ' = '

        if (self.__advanceprecent >= self.perfectprecent):
            self.__advanceprecent = self.__advanceprecent / (self.perfectprecent / 100.0)
            self.__smallreport['advance'] = self.__smallreport['advance'] + str(((local_killed / self.contract_oppositescount) * 100.0))  + '\n'
            self.__advancecompletescore['score'] = str(((local_killed / self.contract_oppositescount) * 100.0))
            try:
                self.__smallreport['advance'] = self.__smallreport['advance'] + '該關卡完成度【進階】為 ' + str((self.perfectprecent / ((local_killed / self.contract_oppositescount)))) + '(超過100%，視為100%)\n'
            except ZeroDivisionError:
                self.__smallreport['advance'] = self.__smallreport['advance'] + '該關卡完成度【進階】為 ' + str((self.perfectprecent / 1.0) * 100.0) + '(超過100%，視為100%)\n'
            self.__completeprecent = ((local_killed / self.contract_oppositescount) * 100.0)
            if (self.__advanceprecent >= 100.0):
                self.__advanceprecent = 100.0
            self.__checkadvance = True
            # 通過進階條件分數
            self.__advancecompletescore['advance'] = 10000
            print('Advance Pass.')
            return True
        else:
            self.__advanceprecent = self.__advanceprecent / (self.perfectprecent / 100.0)
            self.__smallreport['advance'] = self.__smallreport['advance'] + str(((local_killed / self.contract_oppositescount) * 100.0))  + '\n'
            try:
                self.__smallreport['advance'] = self.__smallreport['advance'] + '該關卡完成度【進階】為 ' + str((self.perfectprecent / ((local_killed / self.contract_oppositescount)))) + '(超過100%，視為100%)\n'
            except ZeroDivisionError:
                self.__smallreport['advance'] = self.__smallreport['advance'] + '該關卡完成度【進階】為 ' + str((self.perfectprecent / 1.0) * 100.0) + '(超過100%，視為100%)\n'
            self.__completeprecent = ((local_killed / self.contract_oppositescount) * 100.0)
            self.__checkadvance = False
            print('Advance Fail.')
            return False

    # 增加CompleteScore
    def __do_increasecompletescore(self):
        # Basic Score
        self.__completescore = self.__completescore + self.__basiccompletescore['compiler']
        self.__completescore = self.__completescore + self.__basiccompletescore['basic']
        # Advance Score
        self.__completescore = self.__completescore + self.__advancecompletescore['advance']
        # Special Score
        self.__completescore = self.__completescore + self.__speicalcompletescore['survived']
        self.__completescore = self.__completescore + self.__speicalcompletescore['killed']

        # print(self.__basiccompletescore['compiler'])
        # print(self.__basiccompletescore['basic'])
        # print(self.__advancecompletescore['advance'])
        # print(self.__speicalcompletescore['survived'])
        # print(self.__speicalcompletescore['killed'])

        return None

    # 確認Rank
    def __do_increasecompleterank(self):
        if(self.__completescore >= 40000):
            self.__completerank = 'S'
        elif(self.__completescore < 40000 and self.__completescore >= 32000):
            self.__completerank = 'A'
        elif (self.__completescore < 32000 and self.__completescore >= 24000):
            self.__completerank = 'B'
        elif (self.__completescore < 24000 and self.__completescore >= 16000):
            self.__completerank = 'C'
        else :
            self.__completerank = 'D'

        return None

    # 統整
    def do_main(self):
        # (0) 刪除使用者資料夾(防止殘留檔案)
        self.__delete_user_overarea()
        # (1)新建使用者資料夾
        self.__create_user_overarea()
        # (2)(3)
        if (self.contractcategory == 'G'):
            # (2)讀取Contract的變異體
            self.__read_mutant()
            # (3)建立測試案例
            self.__create_testcase_guard()
        elif (self.contractcategory == 'A'):
            # (2)讀取Contract的測試案例
            self.__read_testcase()
            # (3)建立測試案例
            self.__create_testcase_aggression()
        else:
            print('mto error!!!')
        # (4)執行單元測試
        self.__do_unittest()
        # (5)計算分數
        self.__do_increasecompletescore()
        # (6)確認Rank
        self.__do_increasecompleterank()
        return None

    # ===================================================================================
    # Getter
    # ===================================================================================

    # Getter:username
    def get_username(self):
        return self.username

    # Getter:usercode
    def get_usercode(self):
        return self.usercode

    # Getter:__errormessage
    def get_errormessage(self):
        return self.__errormessage

    # Getter:__outputmessage
    def get_outputmessage(self):
        return self.__outputmessage

    # Getter:__checkcompiler
    def get_checkcompiler(self):
        return self.__checkcompiler

    # Getter:__completeprecent
    def get_completeprecent(self):
        return self.__completeprecent

    # Getter:__checkbasic
    def get_checkbasic(self):
        return self.__checkbasic

    # Getter:__basicprecent
    def get_basicprecent(self):
        return self.__basicprecent

    # Getter:__checkadvance
    def get_checkadvance(self):
        return self.__checkadvance

    # Getter:__advanceprecent
    def get_advanceprecent(self):
        return self.__advanceprecent

    # Getter:__squaredict
    def get_squaredict(self):
        return self.__squaredict

    # Getter:__smallreport
    def get_smallreport(self):
        return self.__smallreport

    # Getter:__basiccompletescore
    def get_basiccompletescore(self):
        return self.__basiccompletescore

    # Getter:__advancecompletescore
    def get_advancecompletescore(self):
        return self.__advancecompletescore

    # Getter:__speicalcompletescore
    def get_speicalcompletescore(self):
        return self.__speicalcompletescore

    # Getter:__completescore
    def get_completescore(self):
        return self.__completescore

    # Getter:__completerank
    def get_completerank(self):
        return self.__completerank