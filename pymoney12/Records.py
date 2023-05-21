#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
from Record import *
class Records:
    """
    1)parameter: categories(instance of Categories)
    2)operation: Create a file when file hasn't exist, otherwise read existing file
    3)return: none
    4)use function: is_number"""
    def __init__(self,categories):
        self._file='pymoney.txt'; self._money=0; self._records = []
        try:
            fh = open(self._file,'r')
            # if file already exist
            print('Welcome back')
            self.process_exist_data(fh,categories)
        except:
            # if file don't exist
            fh = open(self._file,'x')
            money = input('How much money do you have? ')
            if(not self.is_number(money)):
                sys.stderr.write("Invalid value for money. Set to 0 by default.\n")
                self._money=0
            else:
                self._money = int(money)
        fh.close()
        
    """
    1)parameter: record(line of input), categories(instance of Categories)
    2)operation: Seperate record and store data to catli, itemli, costli, timeli. Also check whether category and cost is valid.
    3)return: none
    4)use function: is_number, is_category_valid"""
    def add(self,record,categories):
        # Step1: seperate multiple item by comma
        list1 = record.split(',')
        for i in list1:
            #Step2: seperate category, description, amount by space
            list2 = i.split()
            #Step3: check number of data in a group
            if(len(list2)!=3):
                sys.stderr.write("The format of a record should be like this: food breakfast -50,... Fail to add a record.\n")
                continue
            #Step4: check whether category is valid
            if(categories.is_category_valid(list2[0])==True):
                category = list2[0]
                description = list2[1]
                #Step5: check whether cost is valid
                if(self.is_number(list2[2])):
                    amount = (int)(list2[2])
                    self._money += int(list2[2])
                else: # cost 非數字時，設為0
                    sys.stderr.write("Invalid value for cost. Set to 0 by default.\n")
                    amount = 0 
                r = Record(category,description,amount)
                self._records.append(r)
            else:
                sys.stderr.write("The specified category is not in the category list.\nYou can check the category list by command \"view category\".\nFailed to add a record.")
                
    """
    1)parameter: none
    2)operation: Show data by format: Number Category Description Amount Time 
    3)return: none"""
    def view(self):
        print('Here\'s your expense or income record with description and amount:')
        print('Number Category        Description          Amount Time') 
        print('====== =============== ==================== ====== ================')
        for r in self._records:
            print("%-7d%-16s%-21s%6d%17s"% (self._records.index(r)+1,r.category,r.description,r.amount,r.time))
        print('===================================================================')
        print(f'Now you have {self._money} dollars.') 
        
    """
    1)parameter: delete_record(item name)
    2)operation: Delete data, deal with three possible scenario: no data, one data, multiple data
    3)return: none
    4)use function: is_number"""
    def delete(self,delete_record):
        count = 0 # 紀錄找到資料
        index = [] # 紀錄符合資料座標
        # Step1:尋找符合資料
        for r in self._records:
            if r.description == delete_record:
                index.append(self._records.index(r))
                count+=1
        # Step2-1:沒找到，返回operation select
        if(count == 0):
            print(f"There's no record. Fail to delete.\n")
        # Step2-2:找到一個，直接刪除，返回operation select
        elif(count==1):
            self._money -= int(self._records[index[0]].amount)
            self._records.pop(index[0])
            print(f'{delete_record} is deleted')
        # Step2-3:找到多個
        elif(count>1):
            number =[] # 儲存使用者指定座標
            print('Number Category        Description          Amount Time') 
            print('====== =============== ==================== ====== ================')
            for i in index:
                print("%-7d%-16s%-21s%6d%17s"% ((int)(i)+1,self._records[int(i)].category,self._records[int(i)].description,\
                                                self._records[int(i)].amount,self._records[int(i)].time))
            print('===================================================================')
            number = input('Which one(s) would you like to delete(input number:1,2,3):').split(',')
            number.reverse()#從最後開始刪除
            # 確認格式
            is_format_ok = True
            for num in number:
                if(not self.is_number(num)):
                    is_format_ok=False
                    sys.stderr.write("Please input the format like: 1,2,3(use number). Fail to delete.\n") # 沒按照format: 1 2 3
                    return
            # 確認數字範圍
            is_index_ok = True
            for num in number:
                if(not ((int)(num)-1 in index)):
                    is_index_ok=False
                    sys.stderr.write("There are some choice don't exist on above list. Fail to delete.\n")
                    return
            # 刪除
            for num in number:
                self._money -= int(self._records[(int)(num)-1].amount)
                self._records.pop((int)(num)-1)
            print(f'{delete_record} is deleted')
                    
    """
    1)parameter: target_categories(list of flatten categories)
    2)operation: Print the item of target category
    3)return: none
    4)use function: none"""
    def find(self,target_categories):
        print('Number Category        Description          Amount Time') 
        print('====== =============== ==================== ====== ================')
        index = list(filter(lambda i:self._records[i].category in target_categories,range(len(self._records))))
        money =0
        for i in index:
            print("%-7d%-16s%-21s%6d%17s"% (i+1,self._records[i].category,self._records[i].description,\
                                            self._records[i].amount,self._records[i].time))
            money += self._records[i].amount
        print(f'The total amount above is {money}.')
    
    """
    1)parameter: none
    2)operation: Help user change their money data
    3)return: none
    4)use function: is_number"""
    def change_money(self):
        money = input('How much money do you have? ')
        if(not self.is_number(money)):
            sys.stderr.write("Invalid value for money. Not change money.\n")
        else:
            self._money = (int)(money)
            for r in self._records:
                self._money += r.amount

    """
    1)parameter: none
    2)operation: Save data with format: category, description, amount, time
    3)return: none
    4)use function: none"""
    def save(self):
        fh = open(self._file,'w')
        fh.write(f'{self._money}\n')
        for r in self._records:
            fh.write(f'{r.category:{16}}  {r.description:{21}}  {r.amount:{6}}  {r.time:{17}}\n')
        fh.close()
        
    """
    1)parameter: none
    2)operation: Save data with format: category, description, amount, time
    3)return: none
    4)use function: is_number, is_category_valid"""
    def process_exist_data(self,fh,categories):
        #Step1:check money
        line = fh.readline()
        flag =False #remember whether money has valid
        if(not self.is_number(line)):
            sys.stderr.write("-Invalid money in file. Set to 0 by default.\n")
            self._money=0
            flag = True
        else:
            self._money = int(line)
            
        #Step2:check other data
        for line in fh.readlines():
            list1 = line.split()
            if(len(list1)!=5): # 缺資料
                sys.stderr.write("-Invalid data in file. Will be deleted.\n")
                continue
            #Step2-1:check category
            if(categories.is_category_valid(list1[0])):
                category = list1[0]
            else:
                sys.stderr.write("-Category in file is not in the category list. Will be deleted.\n")
                continue
            #Step2-2:append item
            description = list1[1]
            #Step2-3:check costli
            if(not self.is_number(list1[2])):
                sys.stderr.write("-Invalid cost in file. Set to 0 by default.\n")
                amount = 0
            else:
                amount = (int)(list1[2])
            #Step2-4:check costli
            time = (list1[3]+' '+list1[4])
            r = Record(category,description,amount,time)
            self._records.append(r)
        if flag:
            for r in self._records:
                self._money += r.amount
            
    """
    1)parameter: one data object
    2)operation: Check whether the data is integer
    3)return: True if is integer, otherwise False
    4)use function: none"""
    @staticmethod
    def is_number(n):
        try:
            int(n)
        except:
            return False
        return True

