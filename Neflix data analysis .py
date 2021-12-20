#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as  np
import seaborn as sns
df=pd.read_csv('Netflix.csv')
df.head(3)                                  #####importing data


# In[2]:


df.shape


# In[3]:


df.isnull().sum() ##find the null values


# In[9]:


df.dtypes ## checkiing data type


# In[13]:


df.info


# In[14]:


df.head()


# In[16]:


df.shape


# In[20]:


df[df.duplicated()]


# In[21]:


sns.heatmap(df.isnull()) ### plotting the heating map to see the highest null values


# In[26]:


#to find the houseof card what is  show id and who is the director of the show
df['title'].isin(['House od Cards'])


# In[31]:


df.dtypes


# In[34]:


df['date_added']=pd.to_datetime(df['date_added']) ##converting the data type of date added column into datetime


# In[35]:


df.columns


# In[36]:


df.head()


# In[37]:


df.dtypes


# In[41]:


df['date_added'].dt.year.value_counts() ###to se the maximum rating


# In[42]:


df['date_added'].dt.year.value_counts().plot(kind='bar')


# In[43]:


df.head(2
       )


# In[44]:


df.groupby('type').type.count()


# In[45]:


df['type'].value_counts()


# In[47]:


sns.countplot(df['type'])


# In[48]:


df.head()


# In[49]:


df['yearr']=df['date_added'].dt.year


# df.columns

# In[50]:


df.columns


# In[56]:


df[(df['type']=='Movie') & (df['yearr']==2020)] ##check the movies i  2020 year


# In[60]:


df[(df['type']=='TV Show') &(df['country']=='India')]['title'] ## to see the tv show in india espically title


# In[62]:


df['director'].value_counts().head() ## top most contrubuting director


# In[64]:


df.head(2)


# In[71]:


df[(df['type']=='Movie')&(df['listed_in']=='Comedies')]['rating'].sort_values(ascending=False)


# In[72]:


df[(df['type']=='Movie')&(df['listed_in']=='Comedies')|(df['country']=='United Kingdom')]  ####using OR operator to find the comedy movies in uK


# In[73]:


df.head(2)


# In[76]:


df1=df.dropna() ## drop null values


# In[79]:


df1.head(2)


# In[82]:


df1[df1['cast'].str.contains('Tom Cruise')] ##to check the content in the column use str.contain


# In[87]:


df['rating'].nunique()


# In[90]:


df[(df['type']=='Movie')&(df['rating']=='TV-14')].shape


# In[99]:


df[(df['type']=='Movie')&(df['rating']=='TV-14')&(df['country']=='Canada')].shape


# In[ ]:





# In[100]:


df.head()


# In[103]:


df['duration'].unique()## check duration


# In[105]:


df['duration'].dtypes


# In[106]:


df[['min','unit']]=df['duration'].str.split(' ',expand=True) #to see the duration properly we use str.split to split the string  


# In[108]:


df.head(2)


# In[109]:


df['min'].max()## as per given data max()  duration is 99


# In[110]:


df['min'].min()


# In[111]:


df['min'].mean()


# In[112]:


df['min'].dtypes


# In[113]:


df.head()


# In[114]:


df_TV=df[df['type']=='TV Show']


# In[117]:


df_TV.head(2)


# In[121]:


df_TV['country'].value_counts().sort_values(ascending=False).head() ## top 5 country having the most TV Shows


# In[127]:


df.sort_values('yearr',ascending=False).head(5)


# In[132]:


df[(df['type']=='Movie')&(df['listed_in']=='Kids TV')|(df['type']=='Movie')&(df['listed_in']=='Dramas')].head()###we have use and and OR operation 

