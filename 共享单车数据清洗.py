#!/usr/bin/env python
# coding: utf-8

# # 总结
# - 1. head(),info() describe() 导入数据后，先观察一下数据。看看都是什么类型的
# - 2. data.columns=[]  修改字段名称
# - 3. data.sort_values([]) 根据字段名排序。
# - 4. pd.to_datetime([]) 将字符串改编成时间格式 
# - 5. 修改原数据格式，直接 data[] = pd.to_datatime([])  使用的是Series 的特性，
# - 6. 筛选出符合条件的数据，显示进行逻辑判断，然后进行布尔型的筛选即可。
# - 7. 时间转换为时间戳，(dtime.values - np.datetime64('1970-01-01 08:00:00'))/np.timedelta(1,'s')
# - 8. 时间戳转换为时间 pd.to_datetime(data[要转换的时间],unit='s',origin=pd.Timestamp("1970-01-01 08:00:00"))
# - 9. 重复值查询，data.duplicated(subset=['ziduan1','ziduan2'])  得到的结果是存在重复值的行。
# - 10.  删除重复值 dara.drop_duplicated([字段名])  如果不填写字段名，则检查全部字段，
# - 11.  空值，data.fillna(a) a= 空值除填充默认值，  a='ffill' 填充列方向上的上一个值, a='bfill'  填充列方向上的下一个值。 a = {字典}  字典名字需要和字段名一一对应，填充字典中的数值， limit 限制填充行数， inplace= True or Flase  是否改变原数据
#   data.dropna() 将含有空值的行，全部删除。

# In[27]:


#导入共享单车的数据
import pandas as pd 

data = pd.read_csv('data1.csv')


# In[28]:


#检查，查看数据
data.head()


# In[29]:


#列索引修改为中文
data.columns=["订单编号","车辆编号","用户编号","订单开始时间","起始位置经度","起始位置纬度","订单结束时间","结束位置精度","结束位置纬度","轨迹"]
data.head(2)


# In[30]:


data.sort_values('订单编号')


# In[31]:


data.info()
#观察数据，没有空值，时间是字符串的数据


# In[32]:


pd.datetime.today().year


# In[33]:


#查看时间，
type(pd.to_datetime(data['订单开始时间']))


# In[34]:


import numpy as np 


# In[35]:


#骑行时间最长的时间是多少？
max(pd.to_datetime(data['订单结束时间'])-pd.to_datetime(data['订单开始时间']))


# In[36]:


#骑行 的平均时长是多少？
np.mean(pd.to_datetime(data['订单结束时间'])-pd.to_datetime(data['订单开始时间']))


# In[37]:


#修改原数据中的数据类型
data['订单开始时间']=pd.to_datetime(data['订单开始时间'])
data['订单结束时间']=pd.to_datetime(data['订单结束时间'])


# In[38]:


data.info() # 查看数据类型，可以看到时间是改成了datetime格式


# In[39]:


#我认为大于1天的全部都是异常数据，筛选出来小于1天的数据，
np.max(data['订单结束时间']-data['订单开始时间'])

data[data['订单结束时间']-data['订单开始时间']<'1 days 00:00:00']


# In[40]:


#转换时间戳

#把时间转换成时间戳
dtime = pd.to_datetime(data['订单开始时间'])
v = (dtime.values-np.datetime64("1970-01-01 08:00:00"))/np.timedelta64(1,'s')
data["订单开始时间"]= v
data


# In[43]:


ttime=data['订单开始时间']
ttime


# In[45]:


#时间戳转换成时间

data['订单开始时间']=pd.to_datetime(data['订单开始时间'],unit='s',origin=pd.Timestamp("1970-01-01 08:00:00"))


# In[46]:


data.head()


# In[51]:


#重复数据的处理  duplicated   里面有两个参数，subset和 keep   subset 是选择列，keep是选择保留第一个重复值还是最后一个，还是全部都不保留。
data[data.duplicated(subset=['车辆编号','用户编号'])]
#data.duplicated(subset=['车辆编号','用户编号']).sum()


# In[53]:



data.isnull().sum()


# In[74]:


data.drop_duplicates(subset=['用户编号'],keep= 'first')
#删除重复值


# In[65]:


# 空数据
df = pd.DataFrame([[np.nan,2,np.nan,0],
                  [3,4,np.nan,1],
                  [np.nan,np.nan,np.nan,5],
                  [np.nan,3,np.nan,4]],
                 columns = list("ABCD"))

df


# In[75]:


data[data.duplicated(subset=['用户编号'])]


# In[57]:


df.fillna(0)#填充为默认值


# In[58]:


df


# In[59]:


df.fillna(method='ffill')#填充为上一个值


# In[67]:


#按列名指定填充
values={"A":0,"B":1,"C":2,"D":3}
df.fillna(value=values)
df


# In[68]:


df.fillna(value=values,limit=2,inplace=True)
df


# In[70]:


df.dropna(inplace=True)


# In[ ]:





# In[ ]:




