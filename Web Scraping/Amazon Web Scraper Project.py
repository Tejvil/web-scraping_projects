#!/usr/bin/env python
# coding: utf-8

# In[31]:


# importing libraries

from bs4 import BeautifulSoup
import requests
import time
import datetime


# In[32]:


# connect to website

url = 'https://www.amazon.co.uk/adidas-HC0449-ENT22-T-shirt-Mens/dp/B0BV38CQ96/ref=sr_1_5?content-id=amzn1.sym.7414f21e-2c95-4394-9a75-8c1b3641bcea&dib=eyJ2IjoiMSJ9.mCLlEdsDonh-qCdHH6LcYQv8tGH8zz8m4s_T3BA5ngIkhBW-5b4oG4kaODOeQr8TruwJTVqF_qE4UPy54m7P0C1nTA8osaAi5GENOrlIbNfoJAkofzq8qvrWhM6aAY_MFVa2kLep39SllVsT7gfpO7lS2qkKlYA-vOgJmhFLYyyyqrYJK_zwPH2bB88tRiFksCsvcGCGbj1YBsY5lO5MxNuALYs5omnTn6qv3WaOgKggpEGdTwcwQWHzXkf177cWJj8oQ06y8eXaoHo1MtCfbTNRJwVFegWq7nreul_l7HM.hKmw05N0HD8N4u92MMCUumXYu9mZmkDxMZqqYNbOqiM&dib_tag=se&pd_rd_r=6024e2ff-814d-44f9-9edd-b880d4ce98f7&pd_rd_w=IlJb2&pd_rd_wg=P5aTY&pf_rd_p=7414f21e-2c95-4394-9a75-8c1b3641bcea&pf_rd_r=3DRDMN87GW5EXE6FPQQM&qid=1720716780&s=apparel&sr=1-5&srs=1730929031'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"}

page = requests.get(url, headers=headers)

soup1 = BeautifulSoup(page.content,'html.parser')

soup2 = BeautifulSoup(soup1.prettify(),'html.parser')

title = soup2.find(id='productTitle').get_text()

price = soup2.find(class_='a-offscreen').get_text()


print(title)

print(price)


# In[33]:


price = price.strip()[1:]
title = title.strip()

print(title)

print(price)


# In[37]:


import datetime
today = datetime.date.today()
print(today)


# In[38]:


import csv

header = ['title','Price','Date']
data = [title, price,today]

with open ('AmazonwebScraperDataset.csv','w', newline = '', encoding = 'UTF8') as f :
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)


# In[39]:


import pandas as pd 

df = pd.read_csv(r'C:\Users\ASUS\Python For Data Analysis\AmazonwebScraperDataset.csv')

print(df)


# In[ ]:


# append data to csv

with open ('AmazonwebScraperDataset.csv','a+', newline = '', encoding = 'UTF8') as f :
    writer = csv.writer(f)
    writer.writerow(data)
    


# In[ ]:


def check_price():
    
    url = 'https://www.amazon.co.uk/adidas-HC0449-ENT22-T-shirt-Mens/dp/B0BV38CQ96/ref=sr_1_5?content-id=amzn1.sym.7414f21e-2c95-4394-9a75-8c1b3641bcea&dib=eyJ2IjoiMSJ9.mCLlEdsDonh-qCdHH6LcYQv8tGH8zz8m4s_T3BA5ngIkhBW-5b4oG4kaODOeQr8TruwJTVqF_qE4UPy54m7P0C1nTA8osaAi5GENOrlIbNfoJAkofzq8qvrWhM6aAY_MFVa2kLep39SllVsT7gfpO7lS2qkKlYA-vOgJmhFLYyyyqrYJK_zwPH2bB88tRiFksCsvcGCGbj1YBsY5lO5MxNuALYs5omnTn6qv3WaOgKggpEGdTwcwQWHzXkf177cWJj8oQ06y8eXaoHo1MtCfbTNRJwVFegWq7nreul_l7HM.hKmw05N0HD8N4u92MMCUumXYu9mZmkDxMZqqYNbOqiM&dib_tag=se&pd_rd_r=6024e2ff-814d-44f9-9edd-b880d4ce98f7&pd_rd_w=IlJb2&pd_rd_wg=P5aTY&pf_rd_p=7414f21e-2c95-4394-9a75-8c1b3641bcea&pf_rd_r=3DRDMN87GW5EXE6FPQQM&qid=1720716780&s=apparel&sr=1-5&srs=1730929031'

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"}

    page = requests.get(url, headers=headers)

    soup1 = BeautifulSoup(page.content,'html.parser')

    soup2 = BeautifulSoup(soup1.prettify(),'html.parser')

    title = soup2.find(id='productTitle').get_text()

    price = soup2.find(class_='a-offscreen').get_text()

    price = price.strip()[1:]

    title = title.strip()

    import datetime
    today = datetime.date.today()

    import csv

    header = ['title','Price','Date']
    
    data = [title, price,today]
    
    
    with open ('AmazonwebScraperDataset.csv','a+', newline = '', encoding = 'UTF8') as f :
        writer = csv.writer(f)
        writer.writerow(data)


# In[ ]:


while (True):
    check_price()
    time.sleep(86400)


# In[ ]:


import pandas as pd 

df = pd.read_csv(r'C:\Users\ASUS\Python For Data Analysis\AmazonwebScraperDataset.csv')

print(df)


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




