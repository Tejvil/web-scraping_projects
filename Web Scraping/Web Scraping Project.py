#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Scraping Data from a real Website + Pandas


# In[5]:


from bs4 import BeautifulSoup
import requests


# In[6]:


url = "https://en.wikipedia.org/wiki/List_of_largest_companies_in_India"
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html')


# In[7]:


print(soup)


# In[8]:


soup.find('table')


# In[9]:


soup.find_all('table')[1]


# In[19]:


world_titles = table.find_all('th')


# In[20]:


table = soup.find_all('table')[1]


# In[21]:


world_table_titles = [title.text.strip() for title in world_titles]

print (world_table_titles)


# In[22]:


import pandas as pd


# In[25]:


df = pd.DataFrame(columns = world_table_titles )
df


# In[34]:


column_data = table.find_all('tr')


# In[35]:


for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    
    length = len(df)
    df.loc[length] = individual_row_data
    


# In[36]:


df


# In[43]:


df.to_csv(r'C:\Users\ASUS\Desktop\Data Analisis\PYTHON\Web Scraping\Companies.csv',index = False)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




