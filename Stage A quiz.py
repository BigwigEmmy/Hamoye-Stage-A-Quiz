#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd

#load given data from url
url= 'https://raw.githubusercontent.com/WalePhenomenon/climate_change/master/fuel_ferc1.csv'
data_file =  pd.read_csv(url, error_bad_lines=False)
print(data_file.describe(include='all'))


# In[ ]:


#peep into my data
data_file.head()


# In[ ]:


#correlation
data_file.corr()


# In[ ]:


#group by year and sum fuel cost per unit burned
data_file.groupby('report_year')['fuel_cost_per_unit_burned'].sum()


# In[ ]:


#group by year and find average fuel cost delivered
data_file.groupby('report_year')['fuel_cost_per_unit_delivered'].mean()


# In[ ]:


#compute skewness
data_file.skew()


# In[ ]:


#compute kurtosis
data_file.kurtosis()


# In[ ]:


#group by fuel code and find average
data_file.groupby('fuel_type_code_pudl')['fuel_cost_per_unit_burned'].mean()


# In[ ]:


#missing values check
data_file.isnull().sum()


# In[ ]:




