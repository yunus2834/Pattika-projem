#!/usr/bin/env python
# coding: utf-8

# # Flattening

# In[16]:


sample_list=[[1,2,3],["cat"],[4,5],[6,7,8]]


# In[17]:


flatten_list =[i for a in sample_list for i in a]
print(flatten_list)


# # Reversing

# In[24]:


sample_list3=[[1,2,3],[4,5],[6,7,8]]


# In[25]:


sample_list3.reverse()


# In[26]:


new_list=[ a[:: -1] for a in sample_list3]


# In[27]:


new_list


# In[ ]:





# In[ ]:




