#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().set_next_input("1. What does an empty dictionary's code look like");get_ipython().run_line_magic('pinfo', 'like')
Ans: d = {}


# In[ ]:


2. What is the value of a dictionary value with the key 'foo' and the value 42?
Ans: dictionary = {"foo": 42}
    values is 42


# In[ ]:


get_ipython().set_next_input('3. What is the most significant distinction between a dictionary and a list');get_ipython().run_line_magic('pinfo', 'list')
Ans: A list is an ordered sequence of objects, whereas dictionaries are unordered sets. 


# In[ ]:


4. What happens if you try to access spam['foo'] if spam is {'bar': 100}?
Ans: It will show key error


# In[ ]:


5. If a dictionary is stored in spam, 
what is the difference between the expressions 'cat' in spam and 'cat' in spam.keys()?
Ans: There is no difference.'cat' in spam checks whether there is a 'cat' key in the dictionary,
    while 'cat' in spam.key() checks whether there is a 'cat' key in the dictionary'


# In[ ]:


6. If a dictionary is stored in spam,
what is the difference between the expressions 'cat' in spam and 'cat' in spam.values()?
Ans: 'cat' in spam checks whether there is a 'cat' key in the dictionary,
    while 'cat' in spam. values() checks whether there is a value 'cat' for one of the keys in spam .


# In[ ]:


get_ipython().set_next_input('7. What is a shortcut for the following code');get_ipython().run_line_magic('pinfo', 'code')
if 'color' not in spam:
spam['color'] = 'black'
Ans: spam['color'] = 'black'


# In[ ]:


get_ipython().set_next_input('8. How do you "pretty print" dictionary values using which module and function');get_ipython().run_line_magic('pinfo', 'function')
Ans: pprint is a Python module that provides the capability to pretty print Python data types to be 
    more readable. This module also supports pretty-printing dictionary
    The pprint module there is a function with the same name pprint(), which is the function 
    used to pretty-print the given string or object. It is  to break each dictionary 
    element in the array right after the commas while also sorting 
    the dictionary’s values by key.


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




