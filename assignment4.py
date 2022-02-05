#!/usr/bin/env python
# coding: utf-8

# In[ ]:


1. What exactly is []?
Ans: In Python, a list is created by placing elements inside square brackets [] , separated by commas.


# In[ ]:


2. In a list of values stored in a variable called spam, 
how would you assign the value 'hello' as the third value? (Assume [2, 4, 6, 8, 10] are in spam.)
Let's pretend the spam includes the list ['a', 'b', 'c', 'd'] for the next three queries.
Ans: spam[2] = "hello"


# In[ ]:


3. What is the value of spam[int(int('3' * 2) / 11)]?
Ans: 8


# In[ ]:


4. What is the value of spam[-1]?
Ans: 10


# In[ ]:


5. What is the value of spam[:2]?
Ans: [2,4]


# In[ ]:


Lets pretend bacon has the list [3.14, 'cat' ,  11, 'cat', True] for the next three questions.
6. What is the value of bacon.index('cat')?
Ans:  1


# In[ ]:


get_ipython().set_next_input('7. How does bacon.append(99) change the look of the list value in bacon');get_ipython().run_line_magic('pinfo', 'bacon')
Ans: It will append 99 in the end of list[3.14, 'cat', 11, 'cat', True, 99]


# In[ ]:


get_ipython().set_next_input("8. How does bacon.remove('cat') change the look of the list in bacon");get_ipython().run_line_magic('pinfo', 'bacon')
Ans: It will remove the cat from the left and list become [3.14, 11, 'cat', True, 99]


# In[ ]:


get_ipython().set_next_input('9. What are the list concatenation and list replication operators');get_ipython().run_line_magic('pinfo', 'operators')
Ans:The operator for list concatenation is +, while the operator for replication is *.


# In[ ]:


10. What is difference between the list methods append() and insert()?
Ans: The difference is that with append, we just add a new entry at the end of the list. 
    With insert(position, new_entry) we can create a new entry exactly in the position you want


# In[ ]:


get_ipython().set_next_input('11. What are the two methods for removing items from a list');get_ipython().run_line_magic('pinfo', 'list')
Ans: methods are 
    remove():remove the very first given element matching from the list
    pop(): removes an element from the list based on the index given
    clear():remove all the elements present in the list


# In[ ]:


12. Describe how list values and string values are identical.
Ans: The similarity between Lists and Strings in Python is that both are sequences


# In[ ]:


get_ipython().set_next_input("13. What's the difference between tuples and lists");get_ipython().run_line_magic('pinfo', 'lists')
Ans:The tuples are immutable objects the lists are mutable. 
    This means that tuples cannot be changed while the lists can be modified.


# In[ ]:


14. How do you type a tuple value that only contains the integer 42?
Ans: (42,)


# In[ ]:


get_ipython().set_next_input("15. How do you get a list value's tuple form? How do you get a tuple value's list form");get_ipython().run_line_magic('pinfo', 'form')
Ans: list value can get in tuple form by using tuple() builtin function
    tuple value's in list form by call list() builtin function


# In[ ]:


get_ipython().set_next_input('16. Variables that "contain" list values are not necessarily lists themselves. Instead, what do they contain');get_ipython().run_line_magic('pinfo', 'contain')
Ans:Variables will contain references to list values rather than list values themselves


# In[ ]:


17. How do you distinguish between copy.copy() and copy.deepcopy()?
Ans: A shallow copy constructs a new compound object and then (to the extent possible) 
    inserts references into it to the objects found in the original.
    A deep copy constructs a new compound object and then, recursively,
    inserts copies into it of the objects found in the original.

