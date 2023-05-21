#!/usr/bin/env python
# coding: utf-8

# In[1]:


money = int(input('How much money do you have? '))
print('Add an expense or income record with description and amount:\ndesc1 amt1, desc2 amt2, desc3 amt3, ...')

str = input()
list = str.split(',') #split by comma
index =0
for i in list: #list = ['desc1 amt1','desc2 amt2'...]
    li = i.split() #split by space
    list[index] = tuple(li) #list = [('desc1' amt1),('desc2' amt2)...]
    money += int(li[1])
    index+=1
print('Here\'s your expense and income records:')
for tup in list:
    print(' '.join(tup))
print(f'Now you have {money} dollars.')


# In[ ]:




