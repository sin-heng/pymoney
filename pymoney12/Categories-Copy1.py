#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Categories:
    """
    1)parameter: none
    2)operation: Create a nested list
    3)return: none
    4)use function: none"""
    def __init__(self):
        self._categories = ['expense', ['food', ['meal', 'snack', 'drink'], 'transportation', ['bus', 'railway']],                 'income', ['salary', 'bonus']]
        
    """
    1)parameter: indent(used for recursion)
    2)operation: Print the categories with indentation
    3)return: none
    4)use function: none"""
    def view(self):
        def view_inner(categories,indent=0):
            for i in categories:
                if type(i) == list:
                    view_inner(i,indent+1)
                else:
                    for j in range(indent):
                        print('  ',end='')
                    print(f'- {i}')
        view_inner(self._categories)
    
    """
    1)parameter: category(category which want to be checked)
    2)operation: Check whether the category is valid 
    3)return: True if is valid, otherwise False
    4)use function: is_categories_valid_inner"""
    def is_category_valid(self,category):
        def is_category_valid_inner(category,categories):
            if type(categories) !=list:
                if categories == category:
                    return True
                else:
                    return False
            else:
                had_found=False
                for i in categories:
                    if is_category_valid_inner(category,i):
                        had_found=True
                return had_found
        return is_category_valid_inner(category,self._categories)
    
    """
    1)parameter: category(category which want to be checked)
    2)operation: Find all subcategories and flatten them
    3)return: A list of flatten categories of empty list
    4)use function: find_subcategories_inner,_flatten"""
    def find_subcategories(self,category):
        def find_subcategories_inner(category, categories):
            if type(categories) == list:
                for v in categories:
                    p = find_subcategories_inner(category, v)
                    if p == True:
                        index = categories.index(v)
                        if index + 1 < len(categories) and                             type(categories[index + 1]) == list:
                            return self._flatten(categories[index:index + 2])
                        else:
                        # return only itself if no subcategories
                            return [v]
                    if p != []:
                        return p
            return True if categories == category else []
        if not self.is_category_valid(category):
            Wrong('category not exist err')
        else:
            return find_subcategories_inner(category,self._categories)
    # return [] instead of False if not found
    
    """
    1)parameter: L(list)
    2)operation: Flatten a element in list
    3)return: A list with flatten elements
    4)use function: """
    def _flatten(self,L):
    # return a flat list that contains all element in the nested list L
    # for example, flatten([1, 2, [3, [4], 5]]) returns [1, 2, 3, 4, 5]
        if type(L) == list:
            result = []
            for child in L:
                result.extend(self._flatten(child))
            return result
        else:
            return [L]

