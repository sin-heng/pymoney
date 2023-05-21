#!/usr/bin/env python
# coding: utf-8

# In[5]:


money = int(input('How much money do you have? '))
print('Add an expense or income record with description and amount:')
str = input()
list = str.split()
money += int(list[1])
print(f'Now you have {money} dollars.')


# In[ ]:




