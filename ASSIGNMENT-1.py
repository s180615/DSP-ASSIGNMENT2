#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
sal = pd.read_csv('Salaries.csv')
sal


# In[2]:


sal.head()


# In[3]:


sal.info()


# In[9]:


sal['BasePay'].mean()


# In[8]:


sal['OvertimePay'].max()


# In[10]:


sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['JobTitle']


# In[11]:


sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['TotalPayBenefits']


# In[12]:


sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].max()]


# In[13]:


sal[sal['TotalPayBenefits']  == sal['TotalPayBenefits'].min()]


# In[14]:


sal.groupby('Year').mean()['BasePay']


# In[15]:


sal['JobTitle'].nunique()


# In[16]:


grouped = sal.groupby('JobTitle').count()
top5 = grouped.sort_values(by='Id',  ascending=False)[:5]
top5['Id']


# In[17]:


copied_sal = sal[sal['Year'] == 2013]
group = copied_sal.groupby('JobTitle').count()
count = group[group['Id'] == 1]
count.count()['Id']


# In[18]:


def find_chief(job_title):    
    if 'chief' in job_title.lower().split():
        return True
    else:
        return False

sal = pd.read_csv('Salaries.csv')

sum(sal['JobTitle'].apply(lambda x: find_chief(x)))


# In[19]:


sal['title_len'] = sal['JobTitle'].apply(len)

sal[['title_len', 'TotalPayBenefits']].corr()


# In[ ]:




