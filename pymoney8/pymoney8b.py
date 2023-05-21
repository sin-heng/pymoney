#!/usr/bin/env python
# coding: utf-8

# In[5]:


def add_data(money,itemli,costli):
    print('Add an expense or income record with description and amount(breakfast -40, dinner -50):')
    list = input().split(',')
    for i in list:
        li = i.split()
        if(len(li)<2):
            solve_wrong(2)
        else:
            itemli.append(li[0])
            if(is_number(li[1])):
                costli.append((int)(li[1]))
                money += int(li[1])
            else: # cost 非數字時，設為0
                solve_wrong(8)
                costli.append(0) 
    return money
def show_data(money,itemli,costli):
    print('Here\'s your expense or income record with description and amount:')
    print('Number Description          Amount') 
    print('====== ==================== ======')
    for i in range(len(itemli)):
        print("%-7d%-21s%s"% ((int)(i)+1,itemli[int(i)],costli[int(i)]))
    print(f'Now you have {money} dollars.') 
def delete_data(money,itemli,costli):
    data = input('Which data would you like to delete:')
    count = 0
    index = [] #紀錄符合資料座標
    for i in range(len(itemli)):
        if itemli[i] == data:
            index.append(i)
            count+=1
    # 沒找到，返回operation select
    if(count == 0):
        solve_wrong(4)
    # 找到一個，直接刪除，返回operation select
    elif(count==1):
        money -= int(costli[index[0]])
        itemli.pop(index[0])
        costli.pop(index[0])
        print(f'{data} is deleted')
    # 找到多個
    elif(count>1):
        number =[] # 儲存使用者指定座標
        print('Number Description          Amount') 
        print('====== ==================== ======')
        for i in index:
            print("%-7d%-21s%s"% (i+1,itemli[i],costli[i]))
        number = input('Which one(s) would you like to delete(input number:1,2,3):').split(',')
        number.reverse()#從最後開始刪除
        is_format_ok = True
        for num in number:
            if(not is_number(num)):
                is_format_ok=False
                break;
        if(is_format_ok):
            for num in number:
                if((int)(num)-1 in index):
                    money -= int(costli[(int)(num)-1])
                    itemli.pop((int)(num)-1)
                    costli.pop((int)(num)-1)
                else: # input isn't in data
                    solve_wrong(6)
                    break
        else:
             solve_wrong(5) # 沒按照format: 1 2 3
        print(f'{data} is deleted')
    return money
def solve_wrong(wrong):
    import sys
    if(wrong==0): # invalid number for money
        sys.stderr.write("Invalid value for money. Set to 0 by default.\n")
        return 0;
    elif(wrong==1): # invalid choice of operation
        sys.stderr.write("Invalid command. Try again.\n")
    elif(wrong==2): # add string cannot split to two element
        sys.stderr.write("The format of a record should be like this: breakfast -50,... Fail to add a record.\n")
    elif(wrong==3): # the cost isn't number
        sys.stderr.write("Invalid value for money.\nFail to add a record.\n")
    elif(wrong==4): # when delete, there is no match data
        sys.stderr.write(f"There's no record. Fail to delete.\n")
    elif(wrong==5): # when multiple data to delete, choice which one(s)
        sys.stderr.write("Please input the format like: 1,2,3. Fail to delete.\n")
    elif(wrong==6): # when multiple data to delete, choice the one(s) out of given range
        sys.stderr.write("There are some choice don't exist on above list.\n")
    elif(wrong==7):
        sys.stderr.write("Invalid money in file. Set to 0 by default.\n")
    elif(wrong==8):
        sys.stderr.write("Invalid cost in file. Set to 0 by default.\n")
    elif(wrong==9):
        sys.stderr.write("Invalid data in file. Will be deleted.\n")
def init(file,money,itemli,costli):
    try:
        fh = open(file,'r')
        # if file already exist
        print('Welcome back')
        money = process_exist_data(fh,money,itemli,costli)
    except:
        # if file don't exist
        fh = open(file,'x')
        money = input('How much money do you have? ')
        if(not is_number(money)):
            money = solve_wrong(0)
        else:
            money = (int)(money)
    fh.close()
    return money
def save_data(file,money,itemli,costli):
    fh = open(file,'w')
    fh.write(f'{money}\n')
    for i in range(len(itemli)):
        fh.write(f'{itemli[i]}  {costli[i]}\n')
    fh.close()
def is_number(n):
    try:
        int(n)
    except:
        return False
    return True
def process_exist_data(fh,money,itemli,costli):
    line = fh.readline()
    if(not is_number(line)):
        solve_wrong(7)
        money=0
    else:
        money = (int)(line)
        
    for line in fh.readlines():
        li = line.split()
        if(len(li)<2): # 缺資料
            solve_wrong(9)
            continue
        itemli.append(li[0])
        if(not is_number(li[1])):
            solve_wrong(8)
            costli.append(0)
        else:
            costli.append((int)(li[1]))
    return money
def change_money(costli):
    money = input('How much money do you have? ')
    if(not is_number(money)):
        solve_wrong(0)
        money = 0
    else:
        money = (int)(money)
    for cost in costli:
        money +=cost
    return money
# main function        
file = 'pymoney.txt';money=0;itemli=[];costli=[]
money = init(file,money,itemli,costli)
choice = input('\nWhat do you want to do (add/ view/ delete/ exit/ change_money)? ')
while(choice != 'exit'):
    if(choice == 'add'):
        money = add_data(money,itemli,costli)
    elif(choice == 'view'):
        show_data(money,itemli,costli)
    elif(choice == 'delete'):
        money = delete_data(money,itemli,costli)
    elif(choice == 'change_money'):
        money = change_money(costli)
    else:
        print('Wrong input')
    choice = input('\nWhat do you want to do (add/ view/ delete/ exit/ change_money)? ')
save_data(file,money,itemli,costli)


# In[ ]:





# In[ ]:




