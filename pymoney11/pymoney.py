#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
from Records import *
from Categories import *

categories = Categories()
records = Records(categories)

while True:
    command = input('\nWhat do you want to do ( add / view / delete / view categories / find / change money / exit )? ')
    if command == 'add':
        record = input('Add an expense or income record with format: category, description, amount\n')
        records.add(record, categories)
    elif command == 'view':
        records.view()
    elif command == 'delete':
        delete_record = input("Which record do you want to delete? ")
        records.delete(delete_record)
    elif command == 'view categories':
        categories.view()
    elif command == 'find':
        category = input('Which category do you want to find? ')
        target_categories = categories.find_subcategories(category)
        print(f'Here\'s your expense or income records under category \"{category}\":')
        records.find(target_categories)
    elif command == 'change money':
        records.change_money()
    elif command == 'exit':
        records.save()
        break
    else:
        sys.stderr.write('Invalid command. Try again.\n')

