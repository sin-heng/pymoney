#!/usr/bin/env python
# coding: utf-8

# In[1]:


from file import *
from operation import *
file = 'pymoney.txt';money=0;catli=[];itemli=[];costli=[];timeli=[]
categories = init_cat()
money = init(file,money,categories,catli,itemli,costli,timeli)
choice = input('\nWhat do you want to do ( add/ view/ delete/ view categories/ find/ change money/ exit)? ')
while(choice != 'exit'):
    if(choice == 'add'):
        money = add_data(money,categories,catli,itemli,costli,timeli)
    elif(choice == 'view'):
        show_data(money,categories,catli,itemli,costli,timeli)
    elif(choice == 'delete'):
        money = delete_data(money,catli,itemli,costli,timeli)
    elif(choice == 'view categories'):
        view_cat(categories)
    elif(choice == 'find'):
        find(categories,catli,itemli,costli,timeli)
    elif(choice == 'change money'):
        money = change_money(costli)
    else:
        print('Wrong command')
    choice = input('\nWhat do you want to do ( add/ view/ delete/ view categories/ find/ change money/ exit)? ')
save_data(file,money,catli,itemli,costli,timeli)


# In[ ]:





# In[ ]:




