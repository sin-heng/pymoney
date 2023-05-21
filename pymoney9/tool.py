#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def Wrong(wrong):
    import sys
    if(wrong=='money not number err'): # invalid number for money
        sys.stderr.write("Invalid value for money. Set to 0 by default.\n")
        return 0
    elif(wrong=='format err'): # add string cannot split to three element
        sys.stderr.write("The format of a record should be like this: food breakfast -50,... Fail to add a record.\n")
    elif(wrong=='costli not number err'): # the cost isn't number
        sys.stderr.write("Invalid value for cost. Set to 0 by default.\n")
    elif(wrong=='delete format err'): # when multiple data to delete, choice which one(s)
        sys.stderr.write("Please input the format like: 1,2,3. Fail to delete.\n")
    elif(wrong=='delete not exist err'): # when multiple data to delete, choice the one(s) out of given range
        sys.stderr.write("There are some choice don't exist on above list. Fail to delete.\n")
    elif(wrong=='money in file not number err'):
        sys.stderr.write("Invalid money in file. Set to 0 by default.\n")
        return 0
    elif(wrong=='costli in file not number err'):
        sys.stderr.write("Invalid cost in file. Set to 0 by default.\n")
    elif(wrong=='data invalid err'):
        sys.stderr.write("Invalid data in file. Will be deleted.\n")
    elif(wrong=='add category not exist err'):
        sys.stderr.write("The specified category is not in the category list.\nYou can check the category list by command \"view category\".\nFailed to add a record.")
    elif(wrong=='category not exist err'):
        sys.stderr.write("The specified category is not in the category list.\n")
    elif(wrong=='category in file not exist err'):
        sys.stderr.write("Category in file is not in the category list. Will be deleted.\n")
def is_number(n):
    try:
        int(n)
    except:
        return False
    return True
def is_category_valid(category,categories):
    if type(categories) !=list:
        if categories == category:
            return True
        else:
            return False
    else:
        had_found=False
        for i in categories:
            if is_category_valid(category,i):
                had_found=True
        return had_found
def Time():
    import time
    time = time.localtime(time.time())
    s = f'{time.tm_year}/{time.tm_mon}/{time.tm_mday} {time.tm_hour}:{time.tm_min:02d}'
    return s

