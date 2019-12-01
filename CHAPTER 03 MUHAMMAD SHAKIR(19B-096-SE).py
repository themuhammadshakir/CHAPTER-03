#!/usr/bin/env python
# coding: utf-8

# # MUHAMMAD SHAKIR(19B-096-SE)

# # CHAPTER 03

# # 3.24

# In[75]:


x = []
x = eval(input("ENTER LIST :"))
x.remove("secret")
print(x)


# # 3.26

# In[16]:


x = eval(input("ENTER LIST :"))
print(x[0])
print(x[-1])


# # 3.27

# In[25]:


x = eval(input("ENTER POSITIVE INTEGER :"))
for i in range(0,x):
    if x%x==0:
        print(x)
        x= x+5


# # 3.28

# In[26]:


x = eval(input("ENTER NUMBER :"))
for i in range(0,x):
    print(i**2)


# # 3.29

# In[57]:


x = eval(input("ENTER POSITIVE INTEGER :"))
for i in range(1,x):
    if x%i==0:
        print(i)
if x%x==0:
    print(x)


# # 3.30

# In[60]:


x = eval(input("ENTER FIRST NUMBER :"))
y = eval(input("ENTER SECOND NUMBER :"))
z = eval(input("ENTER THIRD NUMBER :"))
res = eval(input("ENTER FOURTH NUMBER :"))
a = (x+y+z)/3
if res==a:
    print("EQUAL")


# # 3.31

# In[86]:


def reverse_string(x):
    x = 'dna'
    return x[::-1]
reverse_string(x)


# # 3.32

# In[101]:


x = eval(input("ENTER FOUR DIGIT INTEGER :"))
y = x%10
z = y-3
for i in range(z,y+1):
    print(i)


# # 3.34

# In[100]:


def pay(x,y):
    if y<40:
        return x*y
    else:
        return (x*y*1.5)-x**2

pay(10,45)


# # 3.35

# In[119]:


def prob(x):
    return x**-2
prob(2)


# # 3.36

# In[122]:


def reverse_int(x):
    return x//x
reverse_int(234)


# # 3.40

# In[128]:


def average(x):
    x = [1,2,3,4,5]
    return 1+2+3+4+5/len(x)
average(x)    

