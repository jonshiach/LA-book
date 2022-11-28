#!/usr/bin/env python
# coding: utf-8

# # SymPy commands
# 
# The SymPy library can perform symbolic calculations.

# In[1]:


import sympy as sym


# ## Matrices
# 
# ### Define matrices

# In[2]:


A = sym.Matrix([[1, 2], [3, 4]])
display(A)


# In[3]:


B = sym.Matrix([[5, 6], [7, 8]])
display(B)


# ### Matrix addition

# In[4]:


AplusB = A + B
display(AplusB)


# ### Multiplication by a scalar

# In[5]:


Atimes3 = 3 * A
display(Atimes3)


# ### Matrix multiplication

# In[6]:


AB = A * B
display(AB)


# ### Matrix exponent

# In[7]:


Asquared = A ** 2
display(Asquared)


# ### Matrix transpoose

# In[8]:


Atranspose = A.T
display(Atranspose)


# ### Zero matrix

# In[10]:


zero = sym.zeros(2, 3)
display(zero)


# ### Identity matrix

# In[11]:


I = sym.eye(3)
display(I)


# ### Determinant of a matrix

# In[12]:


detA = A.det()
print(detA)


# ### Adjoint matrix

# In[13]:


adjA = A.adjugate()
display(adjA)


# ### Inverse matrix

# In[14]:


invA = A.inv()
display(invA)


# ---
# 
# ## Systems of linear equations

# In[15]:


A = sym.Matrix([[1, 2], [3, 4]])
display(A)


# In[16]:


b = sym.Matrix([5, 11])
display(b)


# ### Solution using matrix inverse

# In[17]:


x = A.inv() * b
display(x)


# ### Forming an augmented matrix

# In[18]:


Ab = A.row_join(b)
display(Ab)


# ### Row reduction

# In[19]:


Abrref = Ab.rref()[0]
display(Abrref)


# ### Rank of a matrix

# In[20]:


rankA = A.rank()
print(rankA)


# ---
# 
# ## Vectors

# In[21]:


a = sym.Matrix([1, 2, 3])
display(a)


# In[22]:


b = sym.Matrix([4, 5, 6])
display(b)


# ### Vector magnitude

# In[23]:


anorm = a.norm()
display(anorm)


# ### Unit vector

# In[24]:


ahat = a / a.norm()
display(ahat)


# ### Dot product

# In[25]:


adotb = a.dot(b)
print(adotb)


# ### Cross product

# In[26]:


acrossb = a.cross(b)
display(acrossb)

