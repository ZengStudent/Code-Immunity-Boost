# Testmachine (多對一)
# Testmachine (一對多)
# Testmachine (多對多)


class Testmachine():
    def __init__(self, username):
        # 使用者
        self.username = username

    # 新建使用者在overarea_User_Folder的所有資料夾
    def __create_user_overarea(self):
        return None

    # 讀取Contract的TestCase
    def read_testcase(self):
        return None

    # 讀取Contract的TestCase
    def __read_testcase(self):
        return None

    # 讀取Contract的變異體
    def __read_mutant(self):
        return None

    # 建立單元測試py檔案
    def __create_testcase(self):
        return None

    # 執行單元測試
    def __do_unittest(self):
        return None

    # 整體報告
    def __do_report(self):
        return None

    # 檢查是否編譯成功
    def __do_checkcompiler(self):
        return None

    # 檢查是否達到通關條件
    def __do_checkcontract(self):
        return None

    # 檢查是否達到通關條件(基本)
    def __do_checkcontract_basic(self):
        return None

    # 檢查是否達到通關條件(基本，Unittest)
    # def __do_checkcontract_basic_ut(self):
    #     return None

    # 檢查是否達到通關條件(完美)
    def __do_checkcontract_advance(self):
        return None

    # 檢查是否達到通關條件(完美，Unittest)
    # def __do_checkcontract_advance_ut(self):
    #     return None

    # 統整
    def do_main(self):
        return None