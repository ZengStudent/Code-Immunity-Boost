from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
from django.conf import settings
# Create your models here.

#---------------------------------------
# 合約(類別)
#---------------------------------------
class Contract(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    CONTACT_CATEGORY = (('G','Guard'),
                        ('A','Aggression')
                )
    CONTRACT_MODE = (('otm','OneToMany'),
                     ('mto','ManyToOne'),
                     ('mtm','ManyToMany')
    )
    CONTRACT_LEVEL = (('easy', 'EASY'),
                     ('medium', 'MEDIUM'),
                     ('hard', 'HARD'),
                     ('strong', 'STRONG')
                     )

    tilte = models.TextField(max_length=1000,null=False,blank=False)
    contract_category = models.CharField(max_length=50,null=False,blank=False,choices=CONTACT_CATEGORY)
    contract_mode = models.CharField(max_length=50,null=False,blank=False,choices=CONTRACT_MODE)
    contract_level = models.CharField(max_length=50, null=False, blank=False, choices=CONTRACT_LEVEL)
    contract_oppositescount = models.PositiveSmallIntegerField(null=False,blank=False,default=2,validators=[MinValueValidator(1)])

    contract_customer = models.CharField(default='不具名提供',max_length=50,null=False,blank=False)
    contract_story = models.TextField(null=True,blank=True)

    contract_input_description = models.TextField(null=True, blank=True)
    contract_output_description = models.TextField(null=True, blank=True)
    contract_input_example_one = models.TextField(null=True, blank=True)
    contract_output_example_one = models.TextField(null=True, blank=True)
    contract_input_example_two = models.TextField(null=True, blank=True)
    contract_output_example_two = models.TextField(null=True, blank=True)


    contract_createtime = models.DateTimeField(default=timezone.now,null=False,blank=False)

    content = models.ForeignKey('Contract_Content',null=False,blank=False,on_delete=models.CASCADE)
    perfect = models.ForeignKey('Contract_Perfect',null=False,blank=False,on_delete=models.CASCADE)
    award = models.ForeignKey('Contract_Award', null=False, blank=False, on_delete=models.CASCADE)

    # (官方建議至少保留這方法)直接使用
    def __str__(self):
        return f'{self.tilte}'

    def get_id(self):
        return self.id

    def get_title(self):
        return self.tilte

    def get_category(self):
        return self.contract_category

    def get_mode(self):
        return self.contract_mode

    def get_level(self):
        return self.contract_level

    def get_oppositescount(self):
        return self.contract_oppositescount

    def get_content(self):
        return self.content

    def get_customert(self):
        return self.contract_customer

    def get_story(self):
        return self.contract_story

    def get_input_description(self):
        return self.contract_input_description

    def get_output_description(self):
        return self.contract_output_description

    def get_input_example_one(self):
        return self.contract_input_example_one

    def get_output_example_one(self):
        return self.contract_output_example_one

    def get_input_example_two(self):
        return self.contract_input_example_two

    def get_output_example_two(self):
        return self.contract_output_example_two
    '''
    contract_input_description = models.TextField(null=True, blank=True)
    contract_output_description = models.TextField(null=True, blank=True)
    contract_input_example_one = models.TextField(null=True, blank=True)
    contract_output_example_one = models.TextField(null=True, blank=True)
    contract_input_example_two = models.TextField(null=True, blank=True)
    contract_output_example_two = models.TextField(null=True, blank=True)
    '''



    def get_perfect(self):
        return self.perfect

    def get_award(self):
        return self.award

#---------------------------------------
# 合約(實例)
#---------------------------------------
class ContractInstance(models.Model):
    id = models.PositiveIntegerField(primary_key=True)

    contract = models.ForeignKey('Contract', null=False, blank=False, on_delete=models.CASCADE)

    # (建議至少)直接使用
    def __str__(self):
        return f'ContractInstance #{self.id}'

    def get_id(self):
        return self.id

    def get_contract(self):
        return self.contract

    def get_title(self):
        return self.contract.get_title()

    def get_category(self):
        return self.contract.get_category()

    def get_oppositescount(self):
        return self.contract.get_oppositescount()

    def get_mode(self):
        return self.contract.get_mode()

    def get_level(self):
        return self.contract.contract_level

    def get_customert(self):
        return self.contract.contract_customer

    def get_story(self):
        return self.contract.contract_story

    def get_input_description(self):
        return self.contract.contract_input_description

    def get_output_description(self):
        return self.contract.contract_output_description

    def get_input_example_one(self):
        return self.contract.contract_input_example_one

    def get_output_example_one(self):
        return self.contract.contract_output_example_one

    def get_input_example_two(self):
        return self.contract.contract_input_example_two

    def get_output_example_two(self):
        return self.contract.contract_output_example_two

    def get_content(self):
        return self.contract.get_content()

    def get_perfect(self):
        return self.contract.get_perfect()

    def get_award(self):
        return self.contract.get_award()



#---------------------------------------
# 合約(內容)
#---------------------------------------
class Contract_Content(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    CONTENT_CATEGORY = (('ut', 'Unittest'),
                        ('cov','Coverage'),
                        ('ms','MutationScore')
                        )

    content_description = models.TextField(max_length=10000,null=True,blank=True,help_text='Enter Content Description.')
    content_category = models.CharField(max_length=50,null=False,blank=False,choices=CONTENT_CATEGORY)
    content_precent = models.PositiveSmallIntegerField(null=False,blank=False,default=50,validators=[MinValueValidator(0),MaxValueValidator(100)])

    # (建議至少)直接使用
    def __str__(self):
        return f'Content #{self.id}'

    def get_description(self):
        return self.content_description

    def get_category(self):
        return self.content_category

    def get_precent(self):
        return self.content_precent
#---------------------------------------
# 合約(完美條件)
#---------------------------------------
class Contract_Perfect(models.Model):
    id = models.PositiveIntegerField(primary_key=True)

    PERFECT_CATEGORY = (('em', 'Empty'),
                        ('ut','Unittest'),
                        ('cov','Coverage'),
                         ('ms', 'MutantScore')
    )

    perfect_description = models.TextField(max_length=10000, null=True, blank=True,
                                           help_text='Enter Content Description.')
    perfect_category = models.CharField(max_length=50, null=False, blank=False, choices=PERFECT_CATEGORY)
    perfect_precent = models.PositiveSmallIntegerField(null=False, blank=False, default=50,validators=[MinValueValidator(0),MaxValueValidator(100)])

    # (建議至少)直接使用
    def __str__(self):
        return f'Perfect #{self.id}'

    def get_description(self):
        return self.perfect_description

    def get_category(self):
        return self.perfect_category

    def get_precent(self):
        return self.perfect_precent

#---------------------------------------
# 合約(獎勵)
#---------------------------------------
class Contract_Award(models.Model):
    id = models.PositiveIntegerField(primary_key=True)

    award_basic = models.PositiveBigIntegerField(null=False,blank=False,default=0)
    award_test = models.PositiveIntegerField(null=False, blank=False, default=0)
    award_mutant = models.PositiveIntegerField(null=False, blank=False, default=0)

    # (建議至少)直接使用
    def __str__(self):
        return f'Award #{self.id}'

    def get_basic(self):
        return self.award_basic

    def get_test(self):
        return self.award_test

    def get_mutant(self):
        return self.award_mutant

#
#---------------------------------------
# 合約(被加入)
#---------------------------------------
class Contract_AddedTable(models.Model):
    # 資料表ID
    id = models.PositiveIntegerField(default=1,primary_key=True)

    # 合約實體ID
    contract_id = models.ForeignKey(ContractInstance, null=False, blank=False, on_delete=models.CASCADE)
    # 使用者帳戶
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=1,
    )

    # 合約加入時間
    addedtime = models.DateTimeField(default=timezone.now,null=False,blank=False)

    # (官方建議至少保留這方法)直接使用
    def __str__(self):
        return f'{self.id}'

    def get_id(self):
        return self.id

    def get_contract_id(self):
        return self.contract_id

    def get_author(self):
        return self.author

    def get_addedtime(self):
        return self.addedtime
#---------------------------------------
# 合約(被完成)
#---------------------------------------
class Contract_CompletedTable(models.Model):
    # 資料表ID
    id = models.PositiveIntegerField(default=1,primary_key=True)

    # 合約實體ID
    contract_id = models.ForeignKey(ContractInstance, null=False, blank=False, on_delete=models.CASCADE)

    # 使用者帳戶
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=1,
    )

    # 合約完成時間
    completedtime = models.DateTimeField(default=timezone.now,null=False,blank=False)

    # 是否以Basic完成
    complete_isbasic = models.BooleanField(default=False, null=False, blank=False)
    # 是否以Advance完成
    complete_isadvance = models.BooleanField(default=False, null=False, blank=False)

    # (官方建議至少保留這方法)直接使用
    def __str__(self):
        return f'{self.id}'

    def get_id(self):
        return self.id

    def get_contract_id(self):
        return self.contract_id

    def get_author(self):
        return self.author

    def get_completedtime(self):
        return self.completedtime

    def get_complete_isbasic(self):
        return self.complete_isbasic

    def get_complete_isadvance(self):
        return self.complete_isadvance
