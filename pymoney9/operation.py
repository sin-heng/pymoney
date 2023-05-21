#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from tool import *
def add_data(money,categories,catli,itemli,costli,timeli):
    print('Add an expense or income record with category, description, and amount(seperate by spaces):')
    list1 = input().split(',')
    for i in list1:
        list2 = i.split()
        if(len(list2)!=3):
            Wrong('format err')
            continue
        if(is_category_valid(list2[0],categories)==True):
            catli.append(list2[0])
            itemli.append(list2[1])
            if(is_number(list2[2])):
                costli.append((int)(list2[2]))
                money += int(list2[2])
            else: # cost 非數字時，設為0
                Wrong('costli not number err')
                costli.append(0) 
            timeli.append(Time())
        else:
            Wrong('add category not exist err')
    return money

def show_data(money,categories,catli,itemli,costli,timeli):
    print('Here\'s your expense or income record with description and amount:')
    print('Number Category        Description          Amount Time') 
    print('====== =============== ==================== ====== ================')
    for i in range(len(itemli)):
        print("%-7d%-16s%-21s%6d%17s"% ((int)(i)+1,catli[int(i)],itemli[int(i)],costli[int(i)],timeli[int(i)]))
    print('===================================================================')
    print(f'Now you have {money} dollars.') 

def delete_data(money,catli,itemli,costli,timeli):
    data = input('Which data would you like to delete(enter item name):')
    count = 0 # 紀錄找到資料
    index = [] # 紀錄符合資料座標
    # 尋找符合資料
    for i in range(len(itemli)):
        if itemli[i] == data:
            index.append(i)
            count+=1
    # 沒找到，返回operation select
    if(count == 0):
        print(f"There's no record. Fail to delete.\n")
    # 找到一個，直接刪除，返回operation select
    elif(count==1):
        money -= int(costli[index[0]])
        catli.pop(index[0])
        itemli.pop(index[0])
        costli.pop(index[0])
        timeli.pop(index[0])
        print(f'{data} is deleted')
    # 找到多個
    elif(count>1):
        number =[] # 儲存使用者指定座標
        print('Number Category        Description          Amount Time') 
        print('====== =============== ==================== ====== ================')
        for i in index:
            print("%-7d%-16s%-21s%6d%17s"% ((int)(i)+1,catli[int(i)],itemli[int(i)],costli[int(i)],timeli[int(i)]))
        number = input('Which one(s) would you like to delete(input number:1,2,3):').split(',')
        number.reverse()#從最後開始刪除
        # 確認格式
        is_format_ok = True
        for num in number:
            if(not is_number(num)):
                is_format_ok=False
                break
        # 刪除
        had_delete = False
        if(is_format_ok):
            for num in number:
                if((int)(num)-1 in index):
                    money -= int(costli[(int)(num)-1])
                    catli.pop((int)(num)-1)
                    itemli.pop((int)(num)-1)
                    costli.pop((int)(num)-1)
                    timeli.pop((int)(num)-1)
                    had_delete=True
                else: # input isn't in data
                    Wrong('delete not exist err')
                    break
            if(had_delete):
                print(f'{data} is deleted')
        else:
             Wrong('delete format err') # 沒按照format: 1 2 3
    return money
def init_cat():
    list = ['expense', ['food', ['meal', 'snack', 'drink'], 'transportation', ['bus', 'railway']],             'income', ['salary', 'bonus']]
    return list
def view_cat(categories,indent=0):
    for i in categories:
        if type(i) == list:
            view_cat(i,indent+1)
        else:
            for j in range(indent):
                print('  ',end='')
            print(f'- {i}')
def find(categories,catli,itemli,costli,timeli):
    category = input("Which category do you want to find?")
    if not is_category_valid(category,categories):
        Wrong('category not exist err')
    else:
        list1 = find_subcategories(category, categories)
        print(f'Here\'s your expense or income records under category \"{category}\":')
        print('Number Category        Description          Amount Time') 
        print('====== =============== ==================== ====== ================')
        index = list(filter(lambda i:catli[i] in list1,range(len(itemli))))
        money =0
        for i in index:
            print("%-7d%-16s%-21s%6d%17s"% (i+1,catli[i],itemli[i],costli[i],timeli[i]))
            money += costli[i]
        print(f'The total amount above is {money}.')
def find_subcategories(category, categories):
    if type(categories) == list:
        for v in categories:
            p = find_subcategories(category, v)
            if p == True:
                index = categories.index(v)
                if index + 1 < len(categories) and                     type(categories[index + 1]) == list:
                    return flatten(categories[index:index + 2])
                else:
                # return only itself if no subcategories
                    return [v]
            if p != []:
                return p
    return True if categories == category else []
# return [] instead of False if not found
def flatten(L):
# return a flat list that contains all element in the nested list L
# for example, flatten([1, 2, [3, [4], 5]]) returns [1, 2, 3, 4, 5]
    if type(L) == list:
        result = []
        for child in L:
            result.extend(flatten(child))
        return result
    else:
        return [L]
def change_money(costli):
    money = input('How much money do you have? ')
    if(not is_number(money)):
        Wrong('money not number err')
        money = 0
    else:
        money = (int)(money)
    for cost in costli:
        money +=cost
    return money

