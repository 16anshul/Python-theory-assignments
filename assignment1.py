#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().set_next_input('1. In the below elements which of them are values or an expression');get_ipython().run_line_magic('pinfo', 'expression')
eg:- values can be integer or string and expressions will be mathematical operators.
*              expression
'hello'        values
-87.8          values
-              expression
()
+	           expression
6               values


# In[ ]:


get_ipython().set_next_input('2. What is the difference between string and variable');get_ipython().run_line_magic('pinfo', 'variable')
Ans: A string is the values inside the quotes assignes as a string
     A variable is a container for a particular set of bita or type of data.


# In[ ]:


3. Describe three different data types.
Ans: Numeric : The integer , float and complex values belong to numeric datatype
     Dictionary:
     Boolean
     Set
     Sequence : It includes string , list and tuple


# In[ ]:


get_ipython().set_next_input('4. What is an expression made up of? What do all expressions do');get_ipython().run_line_magic('pinfo', 'do')
Ans: Expressions are representation of value. Expressions are made with help of operands.
    Do's of expressions are:
    An arithmetic expression evaluates to a single arithmetic value.
    A character expression evaluates to a single value of type character.
    A logical or relational expression evaluates to a single logical value.


# In[ ]:


get_ipython().set_next_input('5. This assignment statements, like spam = 10. What is the difference between an expression and a statement');get_ipython().run_line_magic('pinfo', 'statement')
Ans: Here, relational operator is used as an expression
    A statement is a programming instruction that does something i.e. some action takes place. 


# In[ ]:


get_ipython().set_next_input('6. After running the following code, what does the variable bacon contain');get_ipython().run_line_magic('pinfo', 'contain')
bacon = 22
bacon + 1
Ans : 23


# In[ ]:


get_ipython().set_next_input('7. What should the values of the following two terms be');get_ipython().run_line_magic('pinfo', 'be')
'spam' + 'spamspam'
'spam' * 3
Ans: spamspamspam
    spamspamspam


# In[ ]:



get_ipython().set_next_input('8. Why is eggs a valid variable name while 100 is invalid');get_ipython().run_line_magic('pinfo', 'invalid')
Ans:
The name of the variable must always start with either a letter or an underscore (_).


# In[ ]:


get_ipython().set_next_input('9. What three functions can be used to get the integer, floating-point number, or string version of a value');get_ipython().run_line_magic('pinfo', 'value')
Ans:
    The int() , float() , and str( ) functions will evaluate to the integer, 
    floating-point number, and string versions of the value passed to them.


# In[ ]:


get_ipython().set_next_input('10. Why does this expression cause an error? How can you fix it');get_ipython().run_line_magic('pinfo', 'it')
'I have eaten ' + 99 + ' burritos.'
Ans: It will show type error. It can only concatenate str (not "int") to str
    we can fix by amke it all as a string('I have eaten 99 burritos.')
    

