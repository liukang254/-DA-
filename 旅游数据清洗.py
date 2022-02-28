#!/usr/bin/env python
# coding: utf-8

# ## 总结
# - 1. 检查字段名称是否存在空格，如果存在使用data.columns=[x.strip() for x in data.columns.values]
# - 2. 查看删除重复值   data[data.duplicated()]   data.drop_duplicate(inplace=True)
# - 3. count 和sum  的区别， 计数和求和 对于False 值的处理有区别。
# - 4. 给索引重新赋值   data.index = range(data.shape[0])
# - 5. 异常值处理
#     5.1  不符合业务逻辑的数值
#     5.2 不符合常识的数值
#     data.describe()
#     5.3  标准分数，标准差 标准化处理 
#         (y-y.mean())/y.std() 
#         可以查看标准分数大于某些值的值，一般为异常值。比如3
# - 6. 数据的合并
#     pd.concat([[a],[b]])
# - 7. 根据索引删除异常值
#     data.drop(del_index,inplace=True)
# - 8. 缺失值处理
#     1. 看是否能根据其他字段推出来缺失值
#     2. 可以使用本字段的其他值的平均值、众数来填充缺失值
#     data.loc[data['缺失字段'].isnull(),'缺失字段'] = [str(x)[:2] for x in data.loc[data['缺失字段'].isnull(),'其他字段']]
#     data['缺失字段'].fillna(round(data[''].mean()),inplace=True)
# - 9. 提取字符串中的值
#     data['new_name']= data['old_name'].str.extract("(\d\.\d)分/5分")  \d 代表数字 \.表示小数点  表示提取出格式为 双引号里的东西。
#     data[]=data[].str.extract(" (.+) ")  提取出空格之间的值。
#   

# In[3]:


# 请导入NumPy 和Pandas 并且把data2.csv的数据读取出来，并设置第0列为索引
import numpy as np
import pandas as pd 
data= pd.read_csv("data2.csv",index_col=0)
data.head()


# In[4]:


# 查看数据的形状，你能看出来这个数据有多少行    5100
data.shape


# In[ ]:





# In[6]:


# 请查看数据详情，然后判断是否有空数据 出发，目的，价格，节省，存在空数据
data.info()


# In[8]:


# 查看数据描述，并说明为什么不是所有的列都进行计算
data.describe()


# In[10]:


# 查看列的值，并发现其中是不是有一些数据上的问题
col = data.columns.values
col


# In[12]:


# 请写代码取出掉所有列名称中的空格    Python 列表推导式
data.columns = [x.strip() for x in col]


# In[13]:


# 查看列值，是否空格去除成功
data.columns.values


# In[18]:


# 查看重复数据，请思考重复数据查看的函数中的重复判断原则
# 哪个参数可以修改重复数据的判断条件  subset 
# 哪个参数可以控制保留哪条数据  keep
data.duplicated()


# In[17]:


# 查看所有重复数据
data[data.duplicated()]


# In[19]:


# 写代码统计一共有多少条数据是重复的
np.sum(data.duplicated())


# In[20]:


# 请删除掉所有重复数据 ，并替换原来数据(需要把这个动作作用在原数据上)
data.drop_duplicates(inplace=True)


# In[21]:


# 请查看重复数据的数量，如果等于0，那么就是删除成功了，如果不等于0，那么就删除失败了
data.duplicated().sum()


# In[20]:


np.sum(df.duplicated())


# In[25]:


# 请使用count统计现在的数据还剩多少条，并说明count方法和sum方法有什么区别  # count  是统计个数，统计的时候，可以包含False 或者任意数值，
# sum只统计了True 
data.duplicated().count()


# In[23]:


data.duplicated().sum()


# In[26]:


data.head()


# In[27]:


# 请写代码，把索引重新赋值，从0开始一直到最大值
data.index=range(data.shape[0])


# In[27]:


range(10)


# In[28]:


data.index


# ###  异常值处理
# - 不符合业务逻辑的值  比如出去玩，节省的钱比花的钱还多
# - 不符合常识的值： 比如有人把年龄写成了200岁

# In[30]:


data.describe()


# In[31]:


data.describe().T


# In[34]:


# 查看价格的标准差
data['价格'].std()


# In[35]:


#  标准差标准化处理，也叫标准分数
sta = (data['价格']-data['价格'].mean())/data['价格'].std()


# In[36]:


# 请筛选出标准分数大于3的数据
data[(data['价格']-data['价格'].mean())/data['价格'].std()>3]


# In[37]:


# 请筛选出节省的钱大于价格的数据
data[data['节省']>data['价格']]


# In[39]:


# 请把以上两种异常数据合并在一起
pd.concat([data[data['节省']>data['价格']],data[(data['价格']-data['价格'].mean())/data['价格'].std()>3]])


# In[42]:


### 下面就要对这些异常数据进行删除

##### 首先你需要把异常数据的索引值找出来，然后根据索引值再删除这些数据、
del_index = pd.concat([data[data['节省']>data['价格']],data[(data['价格']-data['价格'].mean())/data['价格'].std()>3]]).index
del_index


# In[44]:


# 找到索引值后删除这些数据,并作用在原数据上
data.drop(del_index,inplace=True)


# In[45]:


# 查看数据剩余条数，确认删除成功
data.shape


# ### 缺失值的处理
# 

# In[48]:


#### 请查看数据中有多少的缺失值
np.sum(data.isnull())


# In[49]:


# 首先要处理一下“出发地”为空的数据
### 第一步你需要查看出发地为空的数据
data[data['出发地'].isnull()]


# In[55]:


# 访问出发地为空的数据的出发地这个字段
data[data['出发地'].isnull()]['出发地']


# In[53]:


# 访问出发地为空的数据的路线名这个字段
data.loc[data['出发地'].isnull(),'路线名']


# In[71]:


# 把出发地为空的数据的出发地这个字段，重新赋值为 “路线名”这个字段中的前2个字符的值
data.loc[data['出发地'].isnull(),'出发地']= [str(x)[:2] for x in data.loc[data['出发地'].isnull(),'路线名']]


# In[72]:


data[data['出发地'].isnull()]


# In[73]:


# 查看价格为空的数据
data[data['价格'].isnull()]


# In[61]:


# 取到价格的平均值
data['价格'].mean()


# In[64]:


# 四舍五入平均值
round(data['价格'].mean(),0)


# In[65]:


# 把价格为空的数据用平均值填充
data[data['价格'].isnull()] = data['价格'].mean()
# 或者是  data['价格'].fillna(round(data['价格'].mean(),0),inpalce=True)


# In[69]:


# 请用sum方法查看空值情况
data['价格'].isnull().sum()


# In[60]:


# 对于目的地和节省两个字段中的空值，请按照以上方法进行处理





# In[77]:


#目的地
data.loc[data['目的地'].isnull(),'目的地']


# In[74]:


data.loc[data['目的地'].isnull(),'路线名']


# In[76]:


data.loc[data['目的地'].isnull(),'目的地'] = [str(x)[3:5] for x in data.loc[data['目的地'].isnull(),'路线名']]


# In[78]:


data[data['节省'].isnull()]


# In[82]:


data['节省'].mean()


# In[84]:


data['节省'].fillna(data['节省'].mean(),inplace=True)


# In[85]:


data.head()


# In[86]:


# 提取出酒店评分
data['评分']=data['酒店'].str.extract("(\d\.\d)分/5分")


# In[88]:


data.head()


# In[93]:


# 提取酒店等级
data['酒店等级'] = data['酒店'].str.extract(" (.+) ")


# In[94]:


data.head()


# In[96]:


data.drop(['酒店登记'],axis=1,inplace=True)


# In[98]:


data.head()

