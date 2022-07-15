from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.core.paginator import Paginator
from django.db import IntegrityError
import os, shutil
import json
from app_contract.models import ContractInstance,Contract_CompletedTable
from app_dashboard_normaluser.models import normaluser,normalusercode,normalusercompletecode,normalusercomplete_list


from logic_package.logic_Class_package.testmachine_otm import *
from logic_package.logic_Class_package.testmachine_mtm import *
from logic_package.logic_Class_package.testmachine_mto import *
from logic_package.logic_Basic_package import logic_basic  as lb
from datetime import datetime


CORE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Create your views here.
# ===========================================
# Aggression，one to many
# ===========================================
@login_required(login_url='/login/')
def aggression_otm(request, contractid):
    print(request.user)
    # 從資料庫讀取題目相關資料
    questioncode = lb.read_questioncode(
        CORE_DIR + '/database_folder/database_contract_folder/contract_' + str(contractid) + '/questioncode/')
    originalcode = lb.read_originalcode(
        CORE_DIR + '/database_folder/database_contract_folder/contract_' + str(contractid) + '/originalcode/')
    samplecode = lb.read_samplecode(
        CORE_DIR + '/database_folder/database_contract_folder/contract_' + str(contractid) + '/samplecode/')

    s = {}
    c = ContractInstance.objects.get(id=contractid)
    s = update_initial(request.user,c, questioncode, originalcode, samplecode)
    print('contractid: ', contractid)

    print('contract_title', c.get_title())
    print('contract_content_description', c.get_content().get_description())
    print('contract_perfect_description', c.get_perfect().get_description())
    print('award_basic', c.get_award().get_basic())
    print('award_test', c.get_award().get_test())
    print('award_mutant', c.get_award().get_mutant())

    # 提交Form
    if request.POST:
        # 使用者提交Code
        if 'codesubmit' in request.POST:
            print('codesubmit')
            print(request.POST['code'])

            tm = Testmachine_otm(str(request.user), request.POST['code'], c)

            tm.do_main()


            l = {}
            l = update_submit(request.user,c, questioncode, tm, originalcode, samplecode)

            # 儲存EditorCode(DataBase)
            __addnormalusercode(c, request.user, request.POST['code'], tm.get_errormessage(), tm.get_outputmessage())

            # 儲存EditorCode(Backend)
            __saveusercode(c, request.user, request.POST['code'], 'submit')


            # 如果通過基本條件
            if (tm.get_checkbasic() == True):
                # 儲存CompleteCode(DataBase)
                __addnormalusercompletecode(c, request.user, request.POST['code'], tm.get_checkbasic(),tm.get_checkadvance())
                # 儲存CompleteCode(Backend)
                __saveusercode(c, request.user, request.POST['code'], 'complete')
                # 儲存Contract Complete(DataBase)
                __completetable(c, request.user, tm.get_checkbasic(), tm.get_checkadvance())
                # 儲存User Data(DataBase)
                __completeuserdata(c, request.user, tm)
                # 儲存user Complete List(DataBase)
                __addnormalusercompletelist(c, request.user, tm.get_checkbasic(), tm.get_checkadvance(),tm.get_completescore(),tm.get_completerank())
            else:
                print('Save do not work')

            return render(request, 'aggression/aggression_page_otm.html', context=l)
        # 使用者回復預設Code
        elif 'codedefault' in request.POST:
            print('codedefault')
        elif 'opposites_pre' in request.POST:
            print('opposites_pre')
        elif 'opposites_next' in request.POST:
            print('opposites_pre')
        # 完成Contract
        elif 'codecomplete' in request.POST:
            print('codecomplete')
            user = normaluser.objects.get(author=request.user)
            user.add_correct_counts()
            print('Code Complete User:', user)
            # context
            temp_context = {}
            temp_context['segment'] = 'aggression'
            temp_context['guardtag'] = 'normaluser/guard/'
            temp_context['aggressiontag'] = 'normaluser/aggression/'
            temp_context['contracttag'] = 'normaluser/contract/'
            temp_context['dashboardtag'] = 'normaluser/dashboard/'
            temp_context['historytag'] = 'normaluser/history/'
            temp_context['howtag'] = 'normaluser/how/'
            temp_context['abouttag'] = 'normaluser/about/'
            temp_context['settag'] = 'normaluser/set/'
            temp_context['username'] = user
            temp_context['oldcorrectcount'] = user.get_correct_counts()
            temp_context['oldmistakecount'] = user.get_mistake_counts()
            temp_context['newcorrectcount'] = user.get_correct_counts() + 1
            temp_context['newmistakecount'] = user.get_mistake_counts() + 1

            # Contract
            ctt = ContractInstance.objects.all()
            temp_context['dataset'] = ctt
            return render(request, 'complete/completepages_normaluser.html', context=temp_context)


    if request.GET:
        print('GETTTTTTTT')

    return render(request, 'aggression/aggression_page_otm.html', context=s)

@login_required(login_url='/login/')
def aggression_mtm(request, contractid):
    print(request.user)
    s = {}

    # 從資料庫讀取題目相關資料
    questioncode = lb.read_questioncode(
        CORE_DIR + '/database_folder/database_contract_folder/contract_' + str(contractid) + '/questioncode/')
    originalcode = lb.read_originalcode(
        CORE_DIR + '/database_folder/database_contract_folder/contract_' + str(contractid) + '/originalcode/')
    samplecode = lb.read_samplecode(
        CORE_DIR + '/database_folder/database_contract_folder/contract_' + str(contractid) + '/samplecode/')

    s = {}
    c = ContractInstance.objects.get(id=contractid)
    s = update_initial(request.user,c, questioncode, originalcode, samplecode)

    if request.POST:
        # 使用者提交Code
        if 'codesubmit' in request.POST:

            usercodes = {}
            Editor_Acount = int(request.POST['Editor_Acount'])
            for i in range(1, Editor_Acount + 1, 1):
                usercodes['usercodes_' + str(i)] = request.POST['breadhiddeninput_' + str(i)]


            tm = Testmachine_mtm(str(request.user), usercodes, c)
            tm.do_main()


            # 儲存EditorCode(DataBase)
            __addnormalusercode(c, request.user, usercodes, tm.get_errormessage(), tm.get_outputmessage())
            # 儲存EditorCode(Backend)
            __saveusercode(c, request.user, usercodes, 'submit')

            #
            l = {}
            l = update_submit(request.user, c, questioncode, tm, originalcode, samplecode)

            # 如果通過基本條件
            if (tm.get_checkbasic() == True):
                # 儲存CompleteCode(DataBase)
                __addnormalusercompletecode(c, request.user, request.POST['code'], tm.get_checkbasic(),tm.get_checkadvance())
                # 儲存CompleteCode(Backend)
                __saveusercode(c, request.user, usercodes, 'complete')
                # 儲存Contract Complete(DataBase)
                __completetable(c, request.user, tm.get_checkbasic(), tm.get_checkadvance())
                # 儲存User Data(DataBase)
                __completeuserdata(c, request.user, tm)
                # 儲存user Complete List(DataBase)
                __addnormalusercompletelist(c, request.user, tm.get_checkbasic(), tm.get_checkadvance(),tm.get_completescore(),tm.get_completerank())
            else:
                print('Save do not work')

            return render(request, 'aggression/aggression_page_mtm.html', context=l)
        # 完成Contract
        elif 'codecomplete' in request.POST:

            user = normaluser.objects.get(author=request.user)
            user.add_correct_counts()

            # context
            temp_context = {}
            temp_context['segment'] = 'aggression'
            temp_context['guardtag'] = 'normaluser/guard/'
            temp_context['aggressiontag'] = 'normaluser/aggression/'
            temp_context['contracttag'] = 'normaluser/contract/'
            temp_context['dashboardtag'] = 'normaluser/dashboard/'
            temp_context['historytag'] = 'normaluser/history/'
            temp_context['howtag'] = 'normaluser/how/'
            temp_context['abouttag'] = 'normaluser/about/'
            temp_context['settag'] = 'normaluser/set/'
            temp_context['username'] = user
            temp_context['oldcorrectcount'] = user.get_correct_counts()
            temp_context['oldmistakecount'] = user.get_mistake_counts()
            temp_context['newcorrectcount'] = user.get_correct_counts() + 1
            temp_context['newmistakecount'] = user.get_mistake_counts() + 1

            # Contract
            ctt = ContractInstance.objects.all()
            temp_context['dataset'] = ctt
            return render(request, 'complete/completepages_normaluser.html', context=temp_context)

    return render(request, 'aggression/aggression_page_mtm.html', context=s)

@login_required(login_url='/login/')
def aggression_mto(request, contractid):
    s = {}

    # 從資料庫讀取題目相關資料
    questioncode = lb.read_questioncode(
        CORE_DIR + '/database_folder/database_contract_folder/contract_' + str(contractid) + '/questioncode/')
    originalcode = lb.read_originalcode(
        CORE_DIR + '/database_folder/database_contract_folder/contract_' + str(contractid) + '/originalcode/')
    samplecode = lb.read_samplecode(
        CORE_DIR + '/database_folder/database_contract_folder/contract_' + str(contractid) + '/samplecode/')

    s = {}
    c = ContractInstance.objects.get(id=contractid)
    s = update_initial(request.user,c, questioncode, originalcode, samplecode)

    if request.POST:
        # 使用者提交Code
        if 'codesubmit' in request.POST:

            usercodes = {}
            Editor_Acount = int(request.POST['Editor_Acount'])
            for i in range(1, Editor_Acount + 1, 1):
                usercodes['usercodes_' + str(i)] = request.POST['breadhiddeninput_' + str(i)]

            tm = Testmachine_mto(str(request.user), usercodes, c)
            tm.do_main()


            # 儲存EditorCode(DataBase)
            __addnormalusercode(c, request.user, usercodes, tm.get_errormessage(), tm.get_outputmessage())
            # 儲存EditorCode(Backend)
            __saveusercode(c, request.user, usercodes, 'submit')

            #
            l = {}
            l = update_submit(request.user, c, questioncode, tm, originalcode, samplecode)

            # 如果通過基本條件
            if (tm.get_checkbasic() == True):
                # 儲存CompleteCode(DataBase)
                __addnormalusercompletecode(c, request.user, request.POST['code'], tm.get_checkbasic(),tm.get_checkadvance())
                # 儲存CompleteCode(Backend)
                __saveusercode(c, request.user, usercodes, 'complete')
                # 儲存Contract Complete(DataBase)
                __completetable(c, request.user, tm.get_checkbasic(), tm.get_checkadvance())
                # 儲存User Data(DataBase)
                __completeuserdata(c, request.user, tm)
                # 儲存user Complete List(DataBase)
                __addnormalusercompletelist(c, request.user, tm.get_checkbasic(), tm.get_checkadvance(),tm.get_completescore(),tm.get_completerank())
            else:
                print('Save do not work')

            return render(request, 'aggression/aggression_page_mto.html', context=l)
        # 完成Contract
        elif 'codecomplete' in request.POST:

            user = normaluser.objects.get(author=request.user)
            user.add_correct_counts()
            # context
            temp_context = {}
            temp_context['segment'] = 'aggression'
            temp_context['guardtag'] = 'normaluser/guard/'
            temp_context['aggressiontag'] = 'normaluser/aggression/'
            temp_context['contracttag'] = 'normaluser/contract/'
            temp_context['dashboardtag'] = 'normaluser/dashboard/'
            temp_context['historytag'] = 'normaluser/history/'
            temp_context['howtag'] = 'normaluser/how/'
            temp_context['abouttag'] = 'normaluser/about/'
            temp_context['settag'] = 'normaluser/set/'
            temp_context['username'] = user
            temp_context['oldcorrectcount'] = user.get_correct_counts()
            temp_context['oldmistakecount'] = user.get_mistake_counts()
            temp_context['newcorrectcount'] = user.get_correct_counts() + 1
            temp_context['newmistakecount'] = user.get_mistake_counts() + 1

            # Contract
            ctt = ContractInstance.objects.all()
            temp_context['dataset'] = ctt
            return render(request, 'complete/completepages_normaluser.html', context=temp_context)

    return render(request, 'aggression/aggression_page_mto.html', context=s)


# ===========================================
# 更新頁面(初始化)
# ===========================================
def update_initial(reuqestuser,input_contract, input_questioncode, input_originalcode, input_samplecode):
    temp_context = {}
    # SideBar
    temp_context['segment'] = 'aggression'
    temp_context['guardtag'] = 'normaluser/guard/'
    temp_context['aggressiontag'] = 'normaluser/aggression/'
    temp_context['contracttag'] = 'normaluser/contract/'
    temp_context['dashboardtag'] = 'normaluser/dashboard/'
    temp_context['historytag'] = 'normaluser/history/'
    temp_context['howtag'] = 'normaluser/how/'
    temp_context['abouttag'] = 'normaluser/about/'
    temp_context['settag'] = 'normaluser/set/'

    # html
    temp_context['mutant_context'] = json.dumps(input_questioncode)
    temp_context['defaultcode'] = json.dumps(input_samplecode)
    temp_context['originalcode'] = json.dumps(input_originalcode)
    temp_context['isdefault'] = json.dumps('true')
    temp_context['contract_title'] = input_contract.get_title()
    temp_context['contract_number'] = input_contract.get_id()
    temp_context['contract_description'] = input_contract.get_story()
    temp_context['contract_input_description'] = input_contract.get_input_description()
    temp_context['contract_output_description'] = input_contract.get_output_description()
    temp_context['contract_input_example_one'] = input_contract.get_input_example_one()
    temp_context['contract_output_example_one'] = input_contract.get_output_example_one()
    temp_context['contract_input_example_two'] = input_contract.get_input_example_two()
    temp_context['contract_output_example_two'] = input_contract.get_output_example_two()
    temp_context['contract_basic'] = input_contract.get_content().get_precent()
    temp_context['contract_advance'] = input_contract.get_perfect().get_precent()
    temp_context['contract_basic_category'] = input_contract.get_content().get_category()
    temp_context['contract_advance_category'] = input_contract.get_perfect().get_category()

    temp_context['contract_content_description'] = input_contract.get_content().get_description()
    temp_context['contract_perfect_description'] = input_contract.get_perfect().get_description()
    temp_context['award_basic'] = input_contract.get_award().get_basic()
    temp_context['award_test'] = input_contract.get_award().get_test()
    temp_context['award_mutant'] = input_contract.get_award().get_mutant()
    temp_context['basicprecent'] = 0
    temp_context['advanceprecent'] = 0
    temp_context['completeprecent'] = 0
    temp_context['codecomplete_state'] = '未達最低標準'
    temp_context['codecompletebutton_state'] = ''
    temp_context['table_square'] = False
    temp_context['submitsurvived'] = 'unknow'
    temp_context['submitkilled'] = 'unknow'

    # Contract Submit
    if (input_contract.get_mode() == 'otm'):
        # 得到該使用者的上傳的合約資料
        temp_normalusersubmitdata = normalusercode.objects.filter(author=reuqestuser,
                                                                  contract_id=input_contract.get_id())
        # 計算資料數量
        temp_normalusersubmitdata_count = temp_normalusersubmitdata.count()
        # 如果有該關卡的提交紀錄
        if (temp_normalusersubmitdata_count > 0):
            normalusersubmitdata = temp_normalusersubmitdata[temp_normalusersubmitdata_count - 1]
            temp_context['defaultcode'] = json.dumps(normalusersubmitdata.get_editorcode())
    elif (input_contract.get_mode() == 'mtm'):
        # 得到該使用者的上傳的合約資料
        temp_normalusersubmitdata = normalusercode.objects.filter(author=reuqestuser,contract_id=input_contract.get_id())
        # 計算資料數量
        temp_normalusersubmitdata_count = temp_normalusersubmitdata.count()

        # 如果有該關卡的提交紀錄
        if (temp_normalusersubmitdata_count > 0):
            normalusersubmitdata = temp_normalusersubmitdata[temp_normalusersubmitdata_count - 1]
            temp_context['deddd'] = json.dumps(__coverteditorcode(normalusersubmitdata.get_editorcode()))
        # 如果沒有該關卡的提交紀錄
        else:
            temp_context['deddd'] = json.dumps(input_samplecode)
    elif (input_contract.get_mode() == 'mto'):
        # 得到該使用者的上傳的合約資料
        temp_normalusersubmitdata = normalusercode.objects.filter(author=reuqestuser,contract_id=input_contract.get_id())
        # 計算資料數量
        temp_normalusersubmitdata_count = temp_normalusersubmitdata.count()

        # 如果有該關卡的提交紀錄
        if (temp_normalusersubmitdata_count > 0):
            normalusersubmitdata = temp_normalusersubmitdata[temp_normalusersubmitdata_count - 1]
            temp_context['deddd'] = json.dumps(__coverteditorcode(normalusersubmitdata.get_editorcode()))
        # 如果沒有該關卡的提交紀錄
        else:
            temp_context['deddd'] = json.dumps(input_samplecode)

    return temp_context


# ===========================================
# 更新頁面(submit)
# ===========================================
def update_submit(reuqestuser,input_contract, input_questioncode, input_testmachine, input_originalcode, input_samplecode):
    temp_context = {}

    # SideBar
    temp_context['segment'] = 'aggression'
    temp_context['guardtag'] = 'normaluser/guard/'
    temp_context['aggressiontag'] = 'normaluser/aggression/'
    temp_context['contracttag'] = 'normaluser/contract/'
    temp_context['dashboardtag'] = 'normaluser/dashboard/'
    temp_context['historytag'] = 'normaluser/history/'
    temp_context['howtag'] = 'normaluser/how/'
    temp_context['abouttag'] = 'normaluser/about/'
    temp_context['settag'] = 'normaluser/set/'

    # html
    temp_context['mutant_context'] = json.dumps(input_questioncode)
    temp_context['defaultcode'] = json.dumps(input_samplecode)
    temp_context['originalcode'] = json.dumps(input_originalcode)
    temp_context['isdefault'] = json.dumps('false')

    if (input_contract.get_mode() == 'otm'):
        temp_context['user_code'] = json.dumps(input_testmachine.get_usercode())
    elif (input_contract.get_mode() == 'mtm'):
        temp_context['user_code'] = json.dumps(input_testmachine.get_usercode())
        # 得到該使用者的上傳的合約資料
        temp_normalusersubmitdata = normalusercode.objects.filter(author=reuqestuser,contract_id=input_contract.get_id())
        # 計算資料數量
        temp_normalusersubmitdata_count = temp_normalusersubmitdata.count()
        # 如果有該關卡的提交紀錄
        if (temp_normalusersubmitdata_count > 0):
            normalusersubmitdata = temp_normalusersubmitdata[temp_normalusersubmitdata_count - 1]
            temp_context['deddd'] = json.dumps(__coverteditorcode(normalusersubmitdata.get_editorcode()))
        # 如果沒有該關卡的提交紀錄
        else:
            temp_context['deddd'] = json.dumps(input_samplecode)

    elif (input_contract.get_mode() == 'mto'):
        temp_context['user_code'] = json.dumps(input_testmachine.get_usercode())
        # 得到該使用者的上傳的合約資料
        temp_normalusersubmitdata = normalusercode.objects.filter(author=reuqestuser,
                                                                  contract_id=input_contract.get_id())
        # 計算資料數量
        temp_normalusersubmitdata_count = temp_normalusersubmitdata.count()
        # 如果有該關卡的提交紀錄
        if (temp_normalusersubmitdata_count > 0):
            normalusersubmitdata = temp_normalusersubmitdata[temp_normalusersubmitdata_count - 1]
            temp_context['deddd'] = json.dumps(__coverteditorcode(normalusersubmitdata.get_editorcode()))
        # 如果沒有該關卡的提交紀錄
        else:
            temp_context['deddd'] = json.dumps(input_samplecode)


    temp_context['console_output_message'] = input_testmachine.get_outputmessage()
    temp_context['console_error_message'] = input_testmachine.get_errormessage()
    temp_context['contract_title'] = input_contract.get_title()
    temp_context['contract_number'] = input_contract.get_id()
    temp_context['contract_description'] = input_contract.get_story()

    temp_context['contract_input_description'] = input_contract.get_input_description()
    temp_context['contract_output_description'] = input_contract.get_output_description()
    temp_context['contract_input_example_one'] = input_contract.get_input_example_one()
    temp_context['contract_output_example_one'] = input_contract.get_output_example_one()
    temp_context['contract_input_example_two'] = input_contract.get_input_example_two()
    temp_context['contract_output_example_two'] = input_contract.get_output_example_two()
    temp_context['contract_basic'] = input_contract.get_content().get_precent()
    temp_context['contract_advance'] = input_contract.get_perfect().get_precent()
    temp_context['contract_basic_category'] = input_contract.get_content().get_category()
    temp_context['contract_advance_category'] = input_contract.get_perfect().get_category()
    temp_context['contract_content_description'] = input_contract.get_content().get_description()
    temp_context['contract_perfect_description'] = input_contract.get_perfect().get_description()
    temp_context['award_basic'] = input_contract.get_award().get_basic()
    temp_context['award_test'] = input_contract.get_award().get_test()
    temp_context['award_mutant'] = input_contract.get_award().get_mutant()
    temp_context['basicprecent'] = round(input_testmachine.get_basicprecent(), 2)
    temp_context['advanceprecent'] = round(input_testmachine.get_advanceprecent(), 2)
    temp_context['completeprecent'] = round(input_testmachine.get_completeprecent(), 2)

    temp_context['basiccompletescore'] = input_testmachine.get_basiccompletescore()
    temp_context['advancecompletescore'] = input_testmachine.get_advancecompletescore()
    temp_context['speicalcompletescore'] = input_testmachine.get_speicalcompletescore()
    temp_context['completescore'] = input_testmachine.get_completescore()
    temp_context['completerank'] = input_testmachine.get_completerank()

    # 提交後，編譯成功
    if (input_testmachine.get_checkcompiler() == True):
        temp_context['table_square'] = True
        temp_context['table_square_dict'] = input_testmachine.get_squaredict()
        temp_context['smallreport'] = input_testmachine.get_smallreport()
        temp_context['submitsurvived'], temp_context['submitkilled'] = __coversquaredict(input_contract.get_mode(),input_testmachine.get_squaredict())

        # 達到基本條件和達到完美條件
        if (input_testmachine.get_checkbasic() == True and input_testmachine.get_checkadvance() == True):
            temp_context['codecomplete_state'] = '已達進階標準'
            temp_context['codecompletebutton_state'] = 'advance'
        # 只達到基本條件
        elif (input_testmachine.get_checkbasic() == True):
            temp_context['codecomplete_state'] = '已達最低標準'
            temp_context['codecompletebutton_state'] = 'basic'
        # 沒達到基本條件
        else:
            temp_context['codecomplete_state'] = '未達最低標準'
            temp_context['codecompletebutton_state'] = 'disabled'
    # 提交後，編譯失敗
    else:
        temp_context['codecomplete_state'] = 'Compile Error'
        temp_context['codecompletebutton_state'] = 'compiler'
        temp_context['table_square'] = False
        temp_context['submitsurvived'] = 'unknow'
        temp_context['submitkilled'] = 'unknow'

    return temp_context



def __coverteditorcode(usercode):
    temp_dict = {}
    temp_splitsequencelist = usercode.split('usercodes')

    for i in range(1, len(temp_splitsequencelist)):
        temp_splitsequence = '\'usercode' + temp_splitsequencelist[i]
        temp_splitsequence = temp_splitsequence[:temp_splitsequence.rfind('\'') + 1]

        temp_key = temp_splitsequence[:temp_splitsequence.find(':')].strip('\'')
        temp_value = temp_splitsequence[temp_splitsequence.find(':') + 1:]
        temp_value = temp_value[temp_value.find('\'') + 1:]
        temp_value = temp_value[:temp_value.rfind(',')]
        if (temp_value.rfind('\'') > 0):
            temp_value = temp_value[:temp_value.rfind('\'')]

        temp_value = temp_value.replace('\\n', '\n')
        temp_value = temp_value.replace('\\r', ' ')

        temp_dict[temp_key] = temp_value

    return temp_dict


def __coversquaredict(mode,squaredict):

    temp_survived = []
    temp_killed = []
    temp_count = 1

    temp_submitsurvived = ''
    temp_submitkilled = ''

    temp_dict = {}

    if(mode == 'otm'):
        for username,uservalue in squaredict.items():
            if (uservalue['scorecodename'] == "---"):
                temp_killed.append(str(temp_count))
            else:
                temp_survived.append(str(temp_count))
            temp_count = temp_count + 1
    else:
        # (建立空字典)
        for username, uservalue in squaredict.items():
            for name, value in uservalue.items():
                temp_dict[name] = 0
            break
        # (計算)
        for username, uservalue in squaredict.items():
            for name, value in uservalue.items():
                if (value['scorecodename'] == "---"):
                    temp_dict[name] = temp_dict[name] + 1
        # (歸納)
        for dict_name, dict_value in temp_dict.items():
            if (dict_value > 0):
                temp_survived.append(dict_name)
            else:
                temp_killed.append(dict_name)


    for i in range(0, len(temp_survived)):
        if (i != len(temp_survived) - 1):
            temp_submitsurvived = temp_submitsurvived + temp_survived[i] + '、'
        else:
            temp_submitsurvived = temp_submitsurvived + temp_survived[i]

    for j in range(0, len(temp_killed)):
        if (j != len(temp_killed) - 1):
            temp_submitkilled = temp_submitkilled + temp_killed[j] + '、'
        else:
            temp_submitkilled = temp_submitkilled + temp_killed[j]

    return temp_submitsurvived,temp_submitkilled

# 儲存EditorCode(DataBase)
def __addnormalusercode(contractinstance,username,usercode,compilerinfo,unittetstinfo):
    nucode = normalusercode.objects.create(id=normalusercode.objects.last().get_id() + 1,
                                           contract_id=contractinstance, author=username,
                                           editorcode=usercode,
                                           editorcode_submittime=timezone.now(),
                                           editorcode_compile_info=compilerinfo,
                                           editorcode_unittest_info=unittetstinfo)
    nucode.save()
    return None

# 儲存EditorCode、EditorCode Complete(Backend)
def __saveusercode(contractinstance,username,usercode,mode):
    if (mode == 'submit'):
        # 使用者儲存路徑
        save_folder_dir = CORE_DIR + '/database_folder/database_usercode_folder/'
    elif (mode == 'complete'):
        #
        save_folder_dir = CORE_DIR + '/database_folder/database_usercompletecode_folder/'
    else:
        print('__saveusercode Error')
        return None

    # 新建資料夾
    if (os.path.isdir(save_folder_dir + str(username)) == False):
        os.mkdir(save_folder_dir + str(username))


    # 新建資料夾
    save_file_dir = save_folder_dir + str(username) + '/' + (
                str(username) + '-' + str(contractinstance.get_id()) + '-' + datetime.now().strftime(
            "%Y-%m-%d-%H-%M-%S"))
    if (os.path.isdir(save_file_dir) == False):
        os.mkdir(save_file_dir)

    # 寫入(One To Many)
    if (type(usercode) == str):
        file_name = save_file_dir + '/' + 'usercode_1.py'
        f = open(file_name, 'w+', encoding='utf-8')
        f.write(usercode)
        f.close()
    # 寫入(Many To Many、Many To One)
    elif (type(usercode) == dict):
        for name, value in usercode.items():
            file_name = save_file_dir + '/' + name + '.py'
            f = open(file_name, 'w+', encoding='utf-8')
            f.write(value)
            f.close()

    return None



# 儲存EditorCode Complete(DataBase)
def __addnormalusercompletecode(contractinstance,username,usercode,isbasic,isadvance):
    nucode = normalusercompletecode.objects.create(id=normalusercompletecode.objects.last().get_id() + 1,
                                           contract_id=contractinstance, author=username,
                                           editorcode_completed=usercode,
                                           editorcode_completedtime=timezone.now(),
                                           editorcode_isbasic=isbasic,
                                           editorcode_isadvance=isadvance)
    nucode.save()
    return None


# 儲存user Complete List(DataBase)
def __addnormalusercompletelist(contractinstance,username,isbasic,isadvance,completescore,completerank):


    # 該使用者以前通過的關卡
    user_completelist = normalusercomplete_list.objects.filter(author=username,contract_id=contractinstance.get_id())

    # 該關卡以前沒有通過
    if(user_completelist.exists() == False):
        # 如果沒有任何紀錄
        if(len(normalusercomplete_list.objects.all()) <= 0):
            nucode = normalusercomplete_list.objects.create(id=1,contract_id=contractinstance,author=username,editorcode_completedtime=timezone.now(),
                                               editorcode_isbasic=isbasic,
                                               editorcode_isadvance=isadvance,
                                               complete_score=completescore,complete_rank=completerank)
        # 至少有一筆紀錄
        else:
            nucode = normalusercomplete_list.objects.create(id=normalusercomplete_list.objects.last().get_id() + 1, contract_id=contractinstance, author=username,
                                                            editorcode_completedtime=timezone.now(),
                                                            editorcode_isbasic=isbasic,
                                                            editorcode_isadvance=isadvance,
                                                            complete_score=completescore,complete_rank=completerank)

        nucode.save()

    return None


# 儲存Contract Complete(DataBase)
def __completetable(contractinstance,username,isbasic,isadvance):
    try:
        contract_complete_table = Contract_CompletedTable.objects.create(id=Contract_CompletedTable.objects.last().get_id() + 1,
                                                                contract_id=contractinstance, author=username,
                                                                completedtime=timezone.now(),
                                                                complete_isbasic=isbasic,
                                                                complete_isadvance=isadvance)
        contract_complete_table.save()
    except IntegrityError as e:
        if 'UNIQUE constraint' in str(e.args):
            print('unique constraint')

    except:
        print('__addtable ERROR')

    return None



# 儲存User Data(DataBase)
def __completeuserdata(contractinstance,username,testmachine):
    userobject = normaluser.objects.get(author=username)

    # 經驗
    userobject.add_basic_experience(contractinstance.get_award().get_basic())
    userobject.add_testing_experience(contractinstance.get_award().get_test())
    if(testmachine.get_checkadvance() == True):
        userobject.add_advance_experience(contractinstance.get_award().get_mutant())

    # 等級

    # Category
    userobject.add_completed_contract_count()
    if(contractinstance.get_category() == 'G'):
        userobject.add_guard_contract_count()
    elif(contractinstance.get_category() == 'A'):
        userobject.add_aggression_contract_count()
    else:
        print('others')

    # Mode
    if(contractinstance.get_mode() == 'otm'):
        userobject.add_onetomany_contract_count()
    elif(contractinstance.get_mode() == 'mtm'):
        userobject.add_manytomany_contract_count()
    elif (contractinstance.get_mode() == 'mto'):
        userobject.add_manytoone_contract_count()
    else:
        print('others')

    # Pass Condition
    if (contractinstance.get_content().get_category() == 'ut'):
        userobject.add_unittest_contract_count()
    elif (contractinstance.get_content().get_category() == 'cov'):
        userobject.add_coverage_contract_count()
    elif (contractinstance.get_content().get_category() == 'ms'):
        userobject.add_mutationscore_contract_count()
    else:
        print('others')

    # Pass State
    if(testmachine.get_checkadvance() == True):
        userobject.add_basic_contract_count()
        userobject.add_advance_contract_count()
    else:
        userobject.add_basic_contract_count()


    # 儲存
    userobject.save()
    return None


