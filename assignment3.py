#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().set_next_input('1. Why are functions advantageous to have in your programs');get_ipython().run_line_magic('pinfo', 'programs')
Ans:Functions reduce the need for duplicate code and they make programs shorter, easier to read, 
    and easier to update.


# In[ ]:


get_ipython().set_next_input("2. When does the code in a function run: when it's specified or when it's called");get_ipython().run_line_magic('pinfo', 'called')
    Ans: A function call is what moves the program execution into the function, 
    and the function call evaluates to the function's return value.


# In[ ]:


get_ipython().set_next_input('3. What statement creates a function');get_ipython().run_line_magic('pinfo', 'function')
Ans: “def” keyword is a statement for defining a function in Python


# In[ ]:


get_ipython().set_next_input('4. What is the difference between a function and a function call');get_ipython().run_line_magic('pinfo', 'call')
Ans:A function is procedure to achieve a particular result
    while function call is using this function to achive that task.
    


# In[ ]:


get_ipython().set_next_input('5. How many global scopes are there in a Python program? How many local scopes');get_ipython().run_line_magic('pinfo', 'scopes')
Ans:The scope of global variables is the entire program 
    whereas the scope of local variable is limited to the function where it is defined
    There's only one global Python scope per program execution
    Local scopes can as many as per functions.


# In[ ]:


get_ipython().set_next_input('6. What happens to variables in a local scope when the function call returns');get_ipython().run_line_magic('pinfo', 'returns')
Ans: The local variables disappear after the function returns.


# In[ ]:


get_ipython().set_next_input('7. What is the concept of a return value? Is it possible to have a return value in an expression');get_ipython().run_line_magic('pinfo', 'expression')
Ans:A return value is used to end the execution of the function call and “returns” the result
We can use that value in a math expression or any other kind of expression in 
which the value has a logical meaning.


# In[ ]:


get_ipython().set_next_input('8. If a function does not have a return statement, what is the return value of a call to that function');get_ipython().run_line_magic('pinfo', 'function')
Ans:  If no return statement appears in a function definition, the return value of the function is undefined.


# In[ ]:


get_ipython().set_next_input('9. How do you make a function variable refer to the global variable');get_ipython().run_line_magic('pinfo', 'variable')
Ans: If we want to refer function variable to a global variable  
    We can use the global keyword to declare which variables are global.


# In[ ]:


get_ipython().set_next_input('10. What is the data type of None');get_ipython().run_line_magic('pinfo', 'None')
Ans: None is used to define a null value. It is not the same as an empty string, False, or a zero. 
    It is a data type of the class NoneType object


# In[ ]:


get_ipython().set_next_input('11. What does the sentence import areallyourpetsnamederic do');get_ipython().run_line_magic('pinfo', 'do')
Ans: That import statement imports a module named areallyourpetsnamederic.


# In[ ]:


get_ipython().set_next_input('12. If you had a bacon() feature in a spam module, what would you call it after importing spam');get_ipython().run_line_magic('pinfo', 'spam')
Ans:This function can be called with spam. bacon()


# In[ ]:


get_ipython().set_next_input('13. What can you do to save a programme from crashing if it encounters an error');get_ipython().run_line_magic('pinfo', 'error')
Ans: If an error occurs in a program, we don't want the program to crash we use
    error handling to notify the user of why the error occurred and 
    gracefully exit the process that caused the error.


# In[ ]:


get_ipython().set_next_input('14. What is the purpose of the try clause? What is the purpose of the except clause');get_ipython().run_line_magic('pinfo', 'clause')
Ans:The try block allows us to test a block of code for errors.
    The except block enables us to handle the error.

