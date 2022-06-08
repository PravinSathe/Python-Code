#!/usr/bin/env python
# coding: utf-8

# In[1]:


text = input().split()
ans = []
for word in text:
    if word.isdigit():
       ans.append(word)
print(ans)


# In[ ]:




