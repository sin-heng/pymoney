#!/usr/bin/env python
# coding: utf-8

# In[3]:


class Record:
    """
    1)parameter: category, description, amount, time(if have)
    2)operation: store above data into a instance
    3)return: none
    4)ues function: Time
    initialize attribute: category, item, amount"""
    def __init__(self,category,description,amount,time=''):
        self._cat = category
        self._des = description
        self._amount = amount
        if time=='':
            self._time = self.Time()
        else:
            self._time = time
        
    @property
    def category(self):
        return self._cat
    
    @property
    def description(self):
        return self._des
    
    @property
    def amount(self):
        return self._amount
    
    @property
    def time(self):
        return self._time
    
    """
    1)parameter: none
    2)operation: Produce a string of time
    3)return: string of time
    4)use function: none"""
    @staticmethod
    def Time():
        import time
        time = time.localtime(time.time())
        s = f'{time.tm_year:}/{time.tm_mon:02d}/{time.tm_mday:02d} {time.tm_hour:02d}:{time.tm_min:02d}'
        return s


# In[ ]:




