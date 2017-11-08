
# coding: utf-8

# In[1]:


import pandas


# In[2]:


http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQ&render=download


# In[3]:


url="http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQ&render=download"


# In[4]:


url


# In[5]:


import pandas as pd


# In[6]:


url="http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQ&render=download"
df= pd.read_csv(url)


# In[7]:


df


# In[8]:


import folium


# In[9]:


import geocoder


# In[10]:


location = geocoder.google("中山大學管理學院").latlng


# In[12]:


location


# In[13]:


folium.Map (location=location,zoom_start=16)

