import os
import shutil
import difflib

CORE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class Comparetestmachine_otm():
    def __init__(self,username,usercode):
        self.username = username
        self.usercode = usercode
        self.comparecodeexist = {}



    def __do_diff(self):
        # 使用者的資料夾路徑
        root_path = CORE_DIR + '/overarea_folder/overarea_User_Folder/' + str(self.username)
        # 測試案例資料夾路徑
        codecompare_path = root_path + '/codecompare_folder'
        #
        text1 = ''
        #
        text2 = ''
        #
        temp_comparecodeexist = {}


        # 生成txt
        for i in range(0, len(self.usercode)):
            text1 = self.usercode[i].get_editorcode_completed()
            with open(codecompare_path + '/diff_' + str(i) + '.txt', 'w') as f:
                f.write(text1)

        # 生成Html
        for index in range(0, len(self.usercode)):
            print('--------------------------------------------')
            print(self.usercode[index].get_contract_id().get_category())
            print(self.usercode[index].get_contract_id().get_mode())
            print(self.usercode[index].get_id())
            print('--------------------------------------------')
            if(index == 0):
                temp_comparecodeexist[str(self.usercode[index].get_id())] = {'name':self.usercode[index].get_id(),'value':False}
                continue
            if(self.usercode[index].get_contract_id().get_category() == 'G' and self.usercode[index].get_contract_id().get_mode()=='otm'):
                if(self.usercode[index-1].get_contract_id().get_category() != 'G' or self.usercode[index-1].get_contract_id().get_mode()!='otm'):
                    temp_comparecodeexist[str(self.usercode[index].get_id())] = {'name':self.usercode[index].get_id(),'value':False}
                    continue
                else:
                    temp_comparecodeexist[str(self.usercode[index].get_id())] = {'name':self.usercode[index].get_id(),'value':True}
                    with open(codecompare_path + '/diff_' + str(index) + '.txt', 'r', encoding='utf-8') as f:
                        text1 = f.readlines()

                    with open(codecompare_path + '/diff_' + str(index-1) + '.txt', 'r', encoding='utf-8') as f:
                        text2 = f.readlines()
                    # Txt
                    d = difflib.Differ()  # 創建Differ()對象
                    diff = d.compare(text1, text2)
                    with open(codecompare_path + '/difftxt_' + str(self.usercode[index].get_id()) + '.txt', 'w') as f:
                        f.write(''.join(list(diff)))

                    # Html
                    d = difflib.HtmlDiff()
                    htmlContent = d.make_file(text1, text2)

                    with open(codecompare_path + '/diff_' + str(self.usercode[index].get_id()) + '.html', 'w') as f:
                        f.write(htmlContent)
            else:
                temp_comparecodeexist[str(self.usercode[index].get_id())] = {'name':self.usercode[index].get_id(),'value':False}

        return temp_comparecodeexist

    # 比較程式碼
    def do_compare(self):
        self.comparecodeexist = self.__do_diff()
        print(self.comparecodeexist)
        return self.comparecodeexist





























