#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import pandas as pd
from sklearn.cluster  import KMeans
import matplotlib.pyplot as plt
data=pd.read_csv('iris.csv')


# In[8]:


Iris_Kemans=KMeans(n_clusters=3,max_iter=5).fit_predict(data[['Petal.Length','Petal.Width']])
print(Iris_Kemans)
plt.figure()
plt.scatter(data['Petal.Length'],data['Petal.Width'],c=Iris_Kemans)
plt.title('k-means test')
plt.show()


# In[11]:


data['kmeans_result']=KMeans(n_clusters=3,max_iter=5).fit_predict(data[['Petal.Length','Petal.Width']])
data.head()


# In[15]:


get_ipython().run_line_magic('pinfo', 'KMeans')
# KMeans(
#     n_clusters=8,     打算分为几部分
#     init='k-means++',  
#     n_init=10,
#     max_iter=300,
#     tol=0.0001,
#     precompute_distances='auto',
#     verbose=0,
#     random_state=None,
#     copy_x=True,
#     n_jobs=None,
#     algorithm='auto',
#)









