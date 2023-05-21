#!/usr/bin/env python
# coding: utf-8

# In[3]:


#pymoney checkpoint 6
# functions
"""
add_data:
1) need: itemli,costli,money
2) operation: add data in itemli and costli and count remaining money
"""
def add_data():
    global money
    print('Add an expense or income record with description and amount:')
    list = input().split()
    itemli.append(list[0])
    costli.append(list[1])
    money += int(list[1])
"""
show_data:
1) need: itemli,costli,money
2) operation: show index,item,cost and remaining money
"""
def show_data():
    global money
    print('Here\'s your expense or income record with description and amount:')
    print('Number Description          Amount') 
    print('====== ==================== ======')
    for i in range(len(itemli)):
        print("%-7d%-21s%s"% ((int)(i)+1,itemli[int(i)],costli[int(i)]))
    print(f'Now you have {money} dollars.')
"""
delete_data:
1) need: itemli,costli,money
2) operation: find assigned item; if not found: not found; if have one, then delete and notice; 
if have many, then show them all and let user to choice, delete assigned one(s) from back so that index will not confused.
"""
def delete_data():
    global money
    data = input('Which data would you like to delete:')
    count = 0
    index = [] #紀錄符合資料座標
    for i in range(len(itemli)):
        if itemli[i] == data:
            index.append(i)
            count+=1
    if(count == 0):
        print('No data found')
    elif(count==1):
        money -= int(costli[index[0]-1])
        itemli.pop(index[0]-1)
        costli.pop(index[0]-1)
        print(f'{data} is deleted')
    elif(count>1):
        print('Number Description          Amount') 
        print('====== ==================== ======')
        for i in index:
            print("%-7d%-21s%s"% (i+1,itemli[i],costli[i]))
        number = input('Which one(s) would you like to delete(input number:1,2,3):').split(',')
        number.reverse()#從最後開始刪除
        for num in number:
            target_index = int(num)
            money -= int(costli[target_index-1])
            itemli.pop(target_index-1)
            costli.pop(target_index-1)
# main function
money = int(input('How much money do you have? '))
itemli = [];costli = []
choice = input('\nWhat do you want to do (add/ view / delete / exit)? ')
while(choice != 'exit'):
    if(choice == 'add'):
        add_data()
    elif(choice == 'view'):
        show_data()
    elif(choice == 'delete'):
        delete_data()
    else:
        print('Wrong input')
    choice = input('\nWhat do you want to do (add/ view / delete / exit)? ')


# In[ ]:




