import os,shutil


# 計算檔案數量(path:檔案資料夾路徑, allowtype(op):允許的資料類型)
def cal_filenumber(path,allowtype=[]):
    temp_number = 0

    for name in os.listdir(path):
        # 有限制檔案類型
        if(len(allowtype) > 0 ):
            for allow in allowtype:
                if(allow in name):
                    temp_number = temp_number + 1
        # 沒有限制檔案類型
        else:
            temp_number = temp_number + 1

    return temp_number


# ===========================================
# 從database_contract_folder讀取Original Code
# ===========================================
def read_originalcode(src):
    # originalcode
    context = ''

    # 檔案來源
    file_source = src + 'OriginalCode.txt'
    # 檔案目的地
    #file_des = des + 'OriginalCode.txt'
    # 讀檔
    with open(file_source, 'r', encoding='utf-8') as f:
        # 放入Original Code
        context = f.read()
        # 複製一份Original Code
        #shutil.copyfile(file_source, file_des)

    return context

# ===========================================
# 從database_contract_folder讀取Sample Code
# ===========================================
def read_samplecode(src):
    # samplecode
    context = ''

    # 檔案來源
    file_source = src + 'SampleCode.txt'
    # 檔案目的地
    #file_des = des + 'SampleCode.txt'
    # 讀檔
    with open(file_source, 'r', encoding='utf-8') as f:
        # 放入Sample Code
        context = f.read()
        # 複製一份Sample Code
        #shutil.copyfile(file_source, file_des)

    return context


# ===========================================
# 從database_contract_folder讀取Question
# ===========================================
def read_questioncode(src):
    # 讀取的內容
    context = []
    # file type
    allowtype = ['.py']
    # file count
    filecount = cal_filenumber(src,allowtype)
    print('filecount',filecount)

    # 挑選變異體
    # for i in range(1,filecount+1):
    #     # 檔案來源
    #     file_source = src + 'Mutant_' + str(i) + '.py'
    #     # 檔案目的地
    #     #file_des = des + 'Mutant_' + str(i) + '.py'
    #     # 讀檔
    #     with open(file_source, 'r',encoding='utf-8') as f:
    #         # 放入變異體
    #         context.append(f.read())
    #         # 複製一份變異體
    #         #shutil.copyfile(file_source,file_des)

    for name in os.listdir(src):
        # 讀檔
        with open(src + name, 'r',encoding='utf-8') as f:
            # 放入變異體
            context.append(f.read())

    return context


