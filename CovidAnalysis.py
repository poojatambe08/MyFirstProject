#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[34]:


data = pd.read_csv(r"D:\Pooja Personal\DataScience\covid_19_india.csv")


# In[7]:


data.columns


# In[25]:


data.tail()


# In[26]:


data.describe()


# In[27]:


data.isnull().sum()


# In[12]:


data.columns


# # Relating the variables with scatterplots

# In[35]:


sns.relplot(x="State/UnionTerritory" ,y="Deaths" , hue = "Cured" ,data=data)


# In[ ]:





# In[36]:


sns.pairplot(data)


# In[37]:


data.columns


# In[47]:


sns.relplot(x="State/UnionTerritory" , y ="Deaths" ,kind = "line" , data=data)


# In[49]:


data.columns


# In[52]:


sns.catplot(x ="State/UnionTerritory" , y = "Cured" ,data=data)


# In[ ]:




