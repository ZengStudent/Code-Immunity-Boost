from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils import timezone
import copy
from django.db import IntegrityError

from app_contract.models import ContractInstance,Contract_AddedTable,Contract_CompletedTable
from app_dashboard_normaluser.models import normalusercomplete_list
from app_guard import views as guardview
from app_aggression import views as aggressionview

import sys
import traceback

# Contract(Normal User)
@login_required(login_url='/login/')
def contractpage_normaluser(request):
    # SideBar
    context = {}
    context['segment'] = 'contract'
    context['guardtag'] = 'normaluser/guard/'
    context['aggressiontag'] = 'normaluser/aggression/'
    context['contracttag'] = 'normaluser/contract/'
    context['dashboardtag'] = 'normaluser/dashboard/'
    context['historytag'] = 'normaluser/history/'
    context['howtag'] = 'normaluser/how/'
    context['abouttag'] = 'normaluser/about/'
    context['settag'] = 'normaluser/set/'


    # CompletedTable
    complete_table = __completetablefilter(request.user)
    context['complete_table'] = complete_table

    # Completelist
    #completelist = normalusercomplete_list.objects.filter(author=request.user)

    # ctt = __showcontract(complete_table,request.user)
    ctt = __praticecontract(complete_table, request.user)
    context['dataset'] = ctt




    # 提交Form
    if request.POST:
        # 按下Dowork按鈕
        if 'dowork' in request.POST:
            # 取得合約ID
            contractid = int(request.POST['dowork'])
            # 選擇的合約
            selected_contact = ContractInstance.objects.get(id=contractid)

            # Contract Added Table
            __addtable(selected_contact,request.user,timezone.now())


            # Category : Guard
            if(selected_contact.get_category() == 'G'):
                # Mode : One To Many
                if(selected_contact.get_mode() == 'otm'):
                    return redirect(guardview.guard_otm,contractid=contractid)
                # Mode : Many To Many
                elif(selected_contact.get_mode() == 'mtm'):
                    return redirect(guardview.guard_mtm,contractid=contractid)
                # Mode : Many To One
                elif (selected_contact.get_mode() == 'mto'):
                    return redirect(guardview.guard_mto, contractid=contractid)
            # Category : Aggression
            elif(selected_contact.get_category() == 'A'):
                # Mode : One To Many
                if (selected_contact.get_mode() == 'otm'):
                    return redirect(aggressionview.aggression_otm, contractid=contractid)
                # Mode : Many To Many
                elif (selected_contact.get_mode() == 'mtm'):
                    return redirect(aggressionview.aggression_mtm, contractid=contractid)
                # Mode : Many To One
                elif (selected_contact.get_mode() == 'mto'):
                    return redirect(aggressionview.aggression_mto, contractid=contractid)

    return render(request,"contracts/contractpages-normaluser.html",context=context)


# 加入Contract(DataBase)
def __addtable(contractinstance,username,addtime):
    try:
        contract_add_table = Contract_AddedTable.objects.create(id=Contract_AddedTable.objects.count()+1,contract_id=contractinstance, author=username,addedtime=addtime)
        contract_add_table.save()
    except IntegrityError as e:
        if 'UNIQUE constraint' in str(e.args):
            print('unique constraint')

    except :
        print('__addtable ERROR')

    return None

# 整理使用者過關紀錄
def __completetablefilter(user_id):

    # 取得該user的已通關紀錄
    temp = normalusercomplete_list.objects.filter(author=user_id)
    #
    temp_value = temp.values('contract_id','editorcode_isbasic','editorcode_isadvance')
    #
    complete_dict = {}

    # 全部關卡資料
    contract_temp = ContractInstance.objects.all()
    # 取得關卡的資料(Guard)
    contract_complete_temp = {}


    for contractinstance in contract_temp:
        contract_complete_temp[contractinstance.get_id()] = 'nothing'

    for c_id in temp_value:
        if(c_id['editorcode_isbasic'] == True and c_id['editorcode_isadvance'] == True):
            complete_dict[c_id['contract_id']] = 'advance'
            contract_complete_temp[c_id['contract_id']] = 'advance'
        elif(c_id['editorcode_isbasic'] == True):
            complete_dict[c_id['contract_id']] = 'basic'
            contract_complete_temp[c_id['contract_id']] = 'basic'
        else:
            complete_dict[c_id['contract_id']] = 'nothing'
            contract_complete_temp[c_id['contract_id']] = 'nothing'

    return contract_complete_temp

# 檢查通過哪些關卡
def __checkusercompletecontract(username):
    # 全部關卡
    all_contract = ContractInstance.objects.all()

    # 關卡ID(Guard)，用於關卡是否解鎖
    all_contractid_guard = {}
    # 關卡ID(Aggression)，用於關卡是否解鎖
    all_contractid_aggression = {}


    # 關卡ID(Guard)，用於找出下一關
    all_contractid_guard_list = []
    # 關卡ID(Aggression)，用於找出下一關
    all_contractid_aggression_list = []

    # 關卡ID(Guard)，用於關卡的Rank
    all_rank_guard = {}
    # 關卡ID(Aggression)，用於關卡的Rank
    all_rank_aggression = {}


    # 該使用者以前通過的關卡
    user_completelist = normalusercomplete_list.objects.filter(author=username)




    # 設定關卡是否解鎖
    for allcontract in all_contract:
        # print(str(allcontract.get_id()))
        # 取得關卡ID(Guard)
        if(allcontract.get_category() == 'G'):
            if(allcontract.get_id() == 1):
                all_contractid_guard[str(allcontract.get_id())] = False
            else:
                all_contractid_guard[str(allcontract.get_id())] = True
            all_contractid_guard_list.append(allcontract.get_id())
            all_rank_guard[str(allcontract.get_id())] = ''
        # 取得關卡ID(Aggression)
        elif(allcontract.get_category() == 'A'):
            if (allcontract.get_id() == 2):
                all_contractid_aggression[str(allcontract.get_id())] = False
            else:
                all_contractid_aggression[str(allcontract.get_id())] = True
            all_contractid_aggression_list.append(allcontract.get_id())
            all_rank_aggression[str(allcontract.get_id())] = ''


    # 依照使用者通關紀錄，解鎖後一關
    for completelist in user_completelist:
        try:
            if(completelist.get_contract_id().get_category() == 'G'):
                # 找出已通關的關卡ID，在list的位置
                temp_index = all_contractid_guard_list.index(completelist.get_contract_id().get_id())

                # 取得該位置下一個
                temp_index = all_contractid_guard_list[temp_index]

                # 不是最後一關(代表解鎖)
                if(temp_index!=all_contractid_guard_list[-1]):
                    all_contractid_guard[str(temp_index)] = False

                all_rank_guard[str(completelist.get_contract_id().get_id())] = completelist.get_complete_rank()

            elif(completelist.get_contract_id().get_category() == 'A'):
                # 找出已通關的關卡ID，在list的位置
                temp_index = all_contractid_aggression_list.index(completelist.get_contract_id().get_id())
                # 取得該位置下一個
                temp_index = all_contractid_aggression_list[temp_index]
                # 不是最後一關(代表解鎖)
                if (temp_index != all_contractid_aggression_list[-1]):
                    all_contractid_aggression[str(temp_index)] = False

                all_rank_aggression[str(completelist.get_contract_id().get_id())] = completelist.get_complete_rank()
        except Exception as e:
            # print(e)
            error_class = e.__class__.__name__  # 取得錯誤類型
            detail = e.args[0]  # 取得詳細內容
            cl, exc, tb = sys.exc_info()  # 取得Call Stack
            lastCallStack = traceback.extract_tb(tb)[-1]  # 取得Call Stack的最後一筆資料
            fileName = lastCallStack[0]  # 取得發生的檔案名稱
            lineNum = lastCallStack[1]  # 取得發生的行號
            funcName = lastCallStack[2]  # 取得發生的函數名稱
            errMsg = "File \"{}\", line {}, in {}: [{}] {}".format(fileName, lineNum, funcName, error_class, detail)
            print(errMsg)
    return all_contractid_guard,all_contractid_aggression,all_rank_guard,all_rank_aggression


# 取得關卡Rank
def __checkcompletelistrank(username):
    # 全部關卡
    all_contract = ContractInstance.objects.all()

    # 該使用者以前通過的關卡
    user_completelist = normalusercomplete_list.objects.filter(author=username)


    return None


# 要顯示的關卡
def __showcontract(completetable,username):

    # 全部關卡
    all_contract = ContractInstance.objects.all()


    # 關卡ID(Guard)
    all_contractid_guard = {}
    # 關卡ID(Aggression)
    all_contractid_aggression = {}

    # 關卡ID(Guard)，用於關卡的Rank
    all_rank_guard = {}
    # 關卡ID(Aggression)，用於關卡的Rank
    all_rank_aggression = {}

    # 使用者看到的關卡
    # 關卡顯示編號,關卡實際ID,關卡名稱,關卡難度,關卡基本條件,關卡進階條件,關卡狀態
    user_contract = {'Guard':[],'Aggression':[]}

    temp_contrat = {'shownumber':0,'contractid':0,'contracttitle':'','contractlevel':'','basicdescription':'','advancedescription':'','contractstate':'','islock':'','completerank':''}
    temp_count = 1

    all_contractid_guard,all_contractid_aggression,all_rank_guard,all_rank_aggression = __checkusercompletecontract(username)



    # Guard
    for allcontract in all_contract:
        if(allcontract.get_category() == 'G'):
            temp_contrat['shownumber'] = temp_count
            temp_contrat['contractid'] = allcontract.get_id()
            temp_contrat['contracttitle'] = allcontract.get_title()
            temp_contrat['contractlevel'] = allcontract.get_level()
            temp_contrat['basicdescription'] = allcontract.get_content().get_description()
            temp_contrat['advancedescription'] = allcontract.get_perfect().get_description()
            temp_contrat['contractstate'] = completetable[allcontract.get_id()]
            temp_contrat['islock'] = all_contractid_guard[str(allcontract.get_id())]
            temp_contrat['completerank'] = all_rank_guard[str(allcontract.get_id())]
            user_contract['Guard'].append(copy.deepcopy(temp_contrat))
            temp_count = temp_count + 1
            temp_contrat = {'shownumber': 0, 'contractid': 0, 'contracttitle': '', 'contractlevel': '','basicdescription': '', 'advancedescription': '', 'contractstate': '', 'islock': '','completerank': ''}

    # 恢復初始值
    temp_count = 1
    temp_contrat = {'shownumber':0,'contractid':0,'contracttitle':'','contractlevel':'','basicdescription':'','advancedescription':'','contractstate':'','islock':''}

    # Aggression
    for allcontract in all_contract:
        if(allcontract.get_category() == 'A'):
            temp_contrat['shownumber'] = temp_count
            temp_contrat['contractid'] = allcontract.get_id()
            temp_contrat['contracttitle'] = allcontract.get_title()
            temp_contrat['contractlevel'] = allcontract.get_level()
            temp_contrat['basicdescription'] = allcontract.get_content().get_description()
            temp_contrat['advancedescription'] = allcontract.get_perfect().get_description()
            temp_contrat['contractstate'] = completetable[allcontract.get_id()]
            temp_contrat['islock'] = all_contractid_aggression[str(allcontract.get_id())]
            temp_contrat['completerank'] = all_rank_aggression[str(allcontract.get_id())]
            user_contract['Aggression'].append(copy.deepcopy(temp_contrat))
            temp_count = temp_count + 1
            temp_contrat = {'shownumber': 0, 'contractid': 0, 'contracttitle': '', 'contractlevel': '','basicdescription': '', 'advancedescription': '', 'contractstate': '', 'islock': '','completerank': ''}

    return user_contract

# 要顯示的關卡(練習)
def __praticecontract(completetable,username):
    # 全部關卡
    all_contract = ContractInstance.objects.all()

    # 關卡ID(Guard)
    all_contractid_guard = {}

    # 關卡ID(Guard)，用於關卡的Rank
    all_rank_guard = {}

    # 使用者看到的關卡
    # 關卡顯示編號,關卡實際ID,關卡名稱,關卡難度,關卡基本條件,關卡進階條件,關卡狀態
    user_contract = {'Guard': []}

    temp_contrat = {'shownumber': 0, 'contractid': 0, 'contracttitle': '', 'contractlevel': '', 'basicdescription': '',
                    'advancedescription': '', 'contractstate': '', 'islock': '', 'completerank': ''}
    temp_count = 1

    completelist= []

    all_contractid_guard, all_contractid_aggression, all_rank_guard, all_rank_aggression = __checkusercompletecontract(username)

    # 該使用者以前通過的關卡
    user_completelist = normalusercomplete_list.objects.filter(author=username)



    for e in user_completelist:
        completelist.append(e.get_contract_id().get_id())



    # Guard
    for allcontract in all_contract:
        if (allcontract.get_category() == 'G'):
            if(allcontract.get_id()==25 or allcontract.get_id()==26 or allcontract.get_id()==27 or allcontract.get_id()==28):
                temp_contrat['shownumber'] = temp_count
                temp_contrat['contractid'] = allcontract.get_id()
                temp_contrat['contracttitle'] = allcontract.get_title()
                temp_contrat['contractlevel'] = allcontract.get_level()
                temp_contrat['basicdescription'] = allcontract.get_content().get_description()
                temp_contrat['advancedescription'] = allcontract.get_perfect().get_description()
                temp_contrat['contractstate'] = completetable[allcontract.get_id()]
                # 25為練習關，預設開放
                if(allcontract.get_id()==25):
                    temp_contrat['islock'] = False
                # 26、27、28
                else:
                    # 前一關通關，則解鎖
                    if(allcontract.get_id()!=25 and allcontract.get_id() - 1 in completelist):
                        temp_contrat['islock'] = False
                    # 鎖住
                    else:
                        temp_contrat['islock'] = True
                temp_contrat['completerank'] = all_rank_guard[str(allcontract.get_id())]
                user_contract['Guard'].append(copy.deepcopy(temp_contrat))
                temp_count = temp_count + 1
                temp_contrat = {'shownumber': 0, 'contractid': 0, 'contracttitle': '', 'contractlevel': '',
                                'basicdescription': '', 'advancedescription': '', 'contractstate': '', 'islock': '',
                                'completerank': ''}

    return user_contract