#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""
open_file: 
1) get mode: 'a', 'w', 'r'
2) operation: find the file and if file not exist then create one; if file exist, then open and write or read it.
3) return file object
4) this function don't help close file
"""
def open_file(mode):
    from pathlib import Path
    pymoneyfile = Path('pymoney.txt')
    pymoneyfile.touch(exist_ok=True) # if file exists, then do nothing, else create one
    fh = open(pymoneyfile,mode) # append last
    return fh;
"""
solve_wrong: 
1) get number of wrong
2) solve problem and print warnings
3) return solve value if needed
"""
def solve_wrong(wrong):
    import sys
    if(wrong==0): # invalid number for money
        sys.stderr.write("Invalid value for money. Set to 0 by default.")
        return 0;
    elif(wrong==1): # invalid choice of operation
        sys.stderr.write("Invalid command. Try again.")
    elif(wrong==2): # add string cannot split to two element
        sys.stderr.write("The format of a record should be like this: breakfast -50.         Fail to add a record.")
    elif(wrong==3): # the cost isn't number
        sys.stderr.write("Invalid value for money.\nFail to add a record.")
    elif(wrong==4): # when delete, there is no match data
        sys.stderr.write(f"There's no record. Fail to delete.")
    elif(wrong==5): # when multiple data to delete, choice which one(s)
        sys.stderr.write("Please input the format like: 1,2,3. Fail to delete.")
    elif(wrong==6): # when multiple data to delete, choice the one(s) out of given range
        sys.stderr.write("There are some choice don't exist on above list.")
    elif(wrong==7):
        sys.stderr.write("Invalid money in file. Set to 0 by default")
    elif(wrong==8):
        sys.stderr.write("Invalid cost in file. Set to 0 by default")
def process_exist_data(fh):
    money =0;itemli=[];costli=[]
    line_index =0
    for line in fh.readlines():
        temp = line[:len(line)-2]
        if(line_index==0):
            if(check_number(temp)):
                money = (int)(temp)
            else:
                solve_wrong(7)
        else:
            l = temp.split()
            itemli.append(l[0])
            if(check_number(l[1])):
                costli.append((int)(l[1]))
            else:
                wrong(8)
        line_index+=1
"""
save_data: 
1) get file object
2) operation: write data: money, itemli, costli into pymoney.txt
    format:
    money
    item1  cost1
    item2  cost2
"""
def save_data(fh):
    global money
    fh.write(f'{money}\n')
    for i in range(len(itemli)):
        fh.write(f'{itemli[i]}  {costli[i]}\n')
"""
check_number: 
1) get num: num is string
2) operation: check whether num is legal number
4) check: True
"""
def check_number(num): # num為string
    is_number = True
    count_dot =0
    if(num.isdigit()): # 最一般的型態: 1000
        pass
    else:
        for i in range(len(num)):
            if(not num[i].isdigit()):
                if((num[i]=='-' or num[i]=='+') and i==0): # 是正或負號，且在第一位
                    pass
                elif(num[i]=='.' and count_dot<=1):
                    if(i==len(num)-1): # 最後一位
                        is_number = False
                    elif(num[i+1].isdigit()):
                        count_dot +=1
                else:
                    is_number = False
    return is_number


# In[ ]:




