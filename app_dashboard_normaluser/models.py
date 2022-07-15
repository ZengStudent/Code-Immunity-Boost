from django.db import models
from django.conf import settings
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from  app_contract.models import ContractInstance
from  app_contract.models import Contract_CompletedTable
# Create your models here.




class normaluser(models.Model):

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=1,
    )

    GENDER = (('M','男性'),('W','女性'),('IPNTS','不願意透露'))
    EDUCATION = (('illiterate','未受教育'),
                 ('kindergarten','幼稚園'),
                 ('elementary','小學'),
                 ('juniorhighschool','國中'),
                 ('seniorhighschool','高中'),
                 ('university','大學'),
                 ('master', '碩士'),
                 ('doctora', '博士'),
                 )

    # 帳戶建立時間
    user_createtime = models.DateTimeField(default=timezone.now,null=False,blank=False)
    # 姓
    lastname = models.CharField(default='lastname',max_length=100,null=False,blank=False)
    # 名
    firstname = models.CharField(default='firstname',max_length=100,null=False,blank=False)
    # 電子郵件
    email = models.EmailField(null=True,blank=True)
    # 性別
    gender = models.CharField(max_length=10,default='M',null=False,blank=False,choices=GENDER)
    # 年齡
    age = models.PositiveSmallIntegerField(default=0,null=True,blank=True)
    # 教育程度
    education = models.CharField(max_length=50,default='illiterate',null=False,blank=False,choices=EDUCATION)
    # 身分
    status = models.CharField(max_length=50,default='nonstatus',null=True,blank=True)
    # 出身日期
    borntime = models.DateTimeField(default=timezone.now,null=True,blank=True)
    # 已完成的合約數量
    completed_contract_count = models.PositiveIntegerField(default=0,null=False,blank=False)
    # Guard完成數量
    guard_contract_count = models.PositiveIntegerField(default=0,null=False,blank=False)
    # aggressio完成數量
    aggression_contract_count = models.PositiveIntegerField(default=0, null=False, blank=False)
    # one to many完成數量
    onetomany_contract_count = models.PositiveIntegerField(default=0, null=False, blank=False)
    # many to many完成數量
    manytomany_contract_count = models.PositiveIntegerField(default=0, null=False, blank=False)
    # many to one完成數量
    manytoone_contract_count = models.PositiveIntegerField(default=0, null=False, blank=False)
    # Unittest完成數量
    unittest_contract_count = models.PositiveIntegerField(default=0, null=False, blank=False)
    # Coverage完成數量
    coverage_contract_count = models.PositiveIntegerField(default=0, null=False, blank=False)
    # MutationScore完成數量
    mutationscore_contract_count = models.PositiveIntegerField(default=0, null=False, blank=False)
    # Basic完成數量
    basic_contract_count = models.PositiveIntegerField(default=0, null=False, blank=False)
    # Advance完成數量
    advance_contract_count = models.PositiveIntegerField(default=0, null=False, blank=False)
    # 使用者基本經驗值
    basic_experience = models.PositiveIntegerField(default=0, null=False, blank=False)
    # 使用者測試經驗值
    testing_experience = models.PositiveIntegerField(default=0, null=False, blank=False)
    # 使用者進階經驗值
    advance_experience = models.PositiveIntegerField(default=0, null=False, blank=False)
    # 使用者基本等級
    basic_level = models.PositiveIntegerField(default=0, null=False, blank=False)
    # 使用者測試等級
    testing_level = models.PositiveIntegerField(default=0, null=False, blank=False)
    # 使用者進階等級
    advance_level = models.PositiveIntegerField(default=0, null=False, blank=False)

    class Meta:
        permissions = (
            ('can_use_normal','Can Use Normal'),

        )


    def __str__(self):
        return f'{self.author}'

    def get_user_createtime(self):
        return self.user_createtime

    def get_lastname(self):
        return self.lastname

    def get_firstname(self):
        return self.firstname

    def get_email(self):
        return self.email

    def get_gender(self):
        return self.gender

    def get_age(self):
        return self.age

    def get_education(self):
        return self.education
    
    def get_status(self):
        return self.status

    def get_borntime(self):
        return self.borntime

    def get_completed_contract_count(self):
        return self.completed_contract_count

    def add_completed_contract_count(self):
        self.completed_contract_count = self.completed_contract_count + 1
        return None

    def get_guard_contract_count(self):
        return self.guard_contract_count

    def add_guard_contract_count(self):
        self.guard_contract_count = self.guard_contract_count + 1
        return None

    def get_aggression_contract_count(self):
        return self.aggression_contract_count

    def add_aggression_contract_count(self):
        self.aggression_contract_count = self.aggression_contract_count + 1
        return None

    def get_onetomany_contract_count(self):
        return self.onetomany_contract_count

    def add_onetomany_contract_count(self):
        self.onetomany_contract_count = self.onetomany_contract_count + 1
        return None

    def get_manytomany_contract_count(self):
        return self.manytomany_contract_count

    def add_manytomany_contract_count(self):
        self.manytomany_contract_count = self.manytomany_contract_count + 1
        return None

    def get_manytoone_contract_count(self):
        return self.manytoone_contract_count

    def add_manytoone_contract_count(self):
        self.manytoone_contract_count = self.manytoone_contract_count + 1
        return None

    def get_unittest_contract_count(self):
        return self.unittest_contract_count

    def add_unittest_contract_count(self):
        self.unittest_contract_count = self.unittest_contract_count + 1
        return None

    def get_coverage_contract_count(self):
        return self.coverage_contract_count

    def add_coverage_contract_count(self):
        self.coverage_contract_count = self.coverage_contract_count + 1
        return None

    def get_mutationscore_contract_count(self):
        return self.mutationscore_contract_count

    def add_mutationscore_contract_count(self):
        self.mutationscore_contract_count = self.mutationscore_contract_count + 1
        return None

    def get_basic_contract_count(self):
        return self.basic_contract_count

    def add_basic_contract_count(self):
        self.basic_contract_count = self.basic_contract_count + 1
        return None

    def get_advance_contract_count(self):
        return self.advance_contract_count

    def add_advance_contract_count(self):
        self.advance_contract_count = self.advance_contract_count + 1
        return None

    def get_basic_experience(self):
        return self.basic_experience

    def add_basic_experience(self,value):
        self.basic_experience = self.basic_experience + int(value)
        return None

    def get_testing_experience(self):
        return self.testing_experience

    def add_testing_experience(self,value):
        self.testing_experience = self.testing_experience + int(value)
        return None

    def get_advance_experience(self):
        return self.advance_experience

    def add_advance_experience(self,value):
        self.advance_experience = self.advance_experience + int(value)
        return None

    def get_basic_level(self):
        return self.basic_level

    def add_basic_level(self):
        self.basic_level = self.basic_level + 1
        return None

    def get_testing_level(self):
        return self.testing_level

    def add_testing_level(self):
        self.testing_level = self.testing_level + 1
        return None

    def get_advance_level(self):
        return self.advance_level

    def add_advance_level(self):
        self.advance_level = self.advance_level + 1
        return None

class normalusercode(models.Model):
    # 資料表ID
    id = models.PositiveIntegerField(default=1, primary_key=True)

    # 合約實體ID
    contract_id = models.ForeignKey(ContractInstance, null=False, blank=False, on_delete=models.CASCADE)
    # 使用者帳戶
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=1,
    )


    # Editor Code
    editorcode = models.TextField(default='',null=True,blank=True)
    # Editor Code 提交時間
    editorcode_submittime = models.DateTimeField(default=timezone.now,null=False,blank=False)
    # Editor Code 提交資訊(Compiler)
    editorcode_compile_info = models.TextField(default='',null=False,blank=False)
    # Editor Code 提交資訊(Unittest)
    editorcode_unittest_info = models.TextField(default='', null=False, blank=False)


    def __str__(self):
        return f'{self.author}'

    def get_id(self):
        return self.id

    def get_author(self):
        return self.author

    def get_contract_id(self):
        return self.contract_id

    def get_editorcode(self):
        return self.editorcode

    def get_editorcode_submittime(self):
        return self.editorcode_submittime

    def get_editorcode_compile_info(self):
        return self.editorcode_compile_info

    def get_editorcode_unittest_info(self):
        return self.editorcode_unittest_info

class normalusercompletecode(models.Model):
    # 資料表ID
    id = models.PositiveIntegerField(default=1, primary_key=True)

    # 合約實體ID
    contract_id = models.ForeignKey(ContractInstance, null=False, blank=False, on_delete=models.CASCADE)
    # 使用者帳戶
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=1,
    )


    # 合約完成的Editor Code
    editorcode_completed = models.TextField(default='', null=True, blank=True)
    # 合約的完成時間
    editorcode_completedtime = models.DateTimeField(default=timezone.now, null=False, blank=False)
    # 是否以Basic完成
    editorcode_isbasic = models.BooleanField(default=False, null=False, blank=False)
    # 是否以Advance完成
    editorcode_isadvance = models.BooleanField(default=False, null=False, blank=False)

    def __str__(self):
        return f'{self.author}'

    def get_id(self):
        return self.id

    def get_author(self):
        return self.author

    def get_contract_id(self):
        return self.contract_id

    def get_editorcode_completed(self):
        return self.editorcode_completed

    def get_editorcode_completedtime(self):
        return self.editorcode_completedtime

    def get_editorcode_isbasic(self):
        return self.editorcode_isbasic

    def get_editorcode_isadvance(self):
        return self.editorcode_isadvance




class normalusercomplete_list(models.Model):
    # 資料表ID
    id = models.PositiveIntegerField(default=1, primary_key=True)


    # 合約實體ID
    contract_id = models.ForeignKey(ContractInstance, null=False, blank=False, on_delete=models.CASCADE)
    # 使用者帳戶
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=1,
    )

    # 合約的完成時間
    editorcode_completedtime = models.DateTimeField(default=timezone.now, null=False, blank=False)
    # 是否以Basic完成
    editorcode_isbasic = models.BooleanField(default=False, null=False, blank=False)
    # 是否以Advance完成
    editorcode_isadvance = models.BooleanField(default=False, null=False, blank=False)

    # 完成分數
    complete_score = models.IntegerField(default=0,null=False,blank=False)

    COMPLETE_RANK = (('S', 'S'),
                        ('A', 'A'),('B', 'B'),('C', 'C'),('D', 'D'),)
    # 完成Rank
    complete_rank = models.CharField(max_length=50,null=True,blank=False,choices=COMPLETE_RANK)


    def __str__(self):
        return f'{self.author}'

    def get_id(self):
        return self.id

    def get_author(self):
        return self.author

    def get_contract_id(self):
        return self.contract_id

    def get_editorcode_completedtime(self):
        return self.editorcode_completedtime

    def get_editorcode_isbasic(self):
        return self.editorcode_isbasic

    def get_editorcode_isadvance(self):
        return self.editorcode_isadvance

    def get_complete_score(self):
        return self.complete_score

    def get_complete_rank(self):
        return self.complete_rank