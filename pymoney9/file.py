#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from tool import*
def init(file,money,categories,catli,itemli,costli,timeli):
    try:
        fh = open(file,'r')
        # if file already exist
        print('Welcome back')
        money = process_exist_data(fh,money,categories,catli,itemli,costli,timeli)
    except:
        # if file don't exist
        fh = open(file,'x')
        money = input('How much money do you have? ')
        if(not is_number(money)):
            money = Wrong('money not number err')
        else:
            money = (int)(money)
    fh.close()
    return money
def process_exist_data(fh,money,categories,catli,itemli,costli,timeli):
    line = fh.readline()
    if(not is_number(line)):
        money = Wrong('money in file not number')
    else:
        money = (int)(line)
        
    for line in fh.readlines():
        list1 = line.split()
        if(len(list1)!=5): # 缺資料
            Wrong('data invalid err')
            continue
        # check category
        if(is_category_valid(list1[0],categories)):
            catli.append(list1[0])
        else:
            Wrong('category in file not exist err')
            continue
        itemli.append(list1[1])
        # check costli
        if(not is_number(list1[2])):
            Wrong('costli in file not number err')
            costli.append(0)
        else:
            costli.append((int)(list1[2]))
        timeli.append(list1[3]+' '+list1[4])
    return money
def save_data(file,money,catli,itemli,costli,timeli):
    fh = open(file,'w')
    fh.write(f'{money}\n')
    for i in range(len(itemli)):
        fh.write(f'{catli[i]:{16}}  {itemli[i]:{21}}  {costli[i]:{6}} {timeli[i]:{17}}\n')
    fh.close()

