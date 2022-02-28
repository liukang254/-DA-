#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 以数据分析的思路来想象一下，假设我们获取到了某一个公司的员工相关数据，会发生哪些事情
# 姓名、性别、联系方式、入职时间、入职等级、基本薪资、福利情况
# 晋升时间点、晋升职级、薪资调整情况、员工职位、离职时间


# In[1]:


# 导入数据并把数据读取出来
import pandas as pd

data = pd.read_csv("salaries.csv")
data


# In[3]:


# 删除Id这一列
data.drop('Id',axis=1,inplace=True)
data


# In[4]:


data.head()


# In[5]:


# 把所有列的名字改成中文，方便后续使用
data.columns
data.columns=['员工姓名','员工职位','基本工资','加班工资','其他支付','福利','总共支付','总共支付加福利','入职年份','附加说明','代理','状态']
data.columns


# In[6]:


data.head()


# In[8]:





# In[9]:


data.head()


# In[13]:


# 查看"员工姓名"这一列数据
data['员工姓名'].head()


# In[15]:


# 查看数据详情
data.info()


# In[17]:


#1、查看入职年份都有几个(值有多少种)
data['入职年份'].nunique()


# In[18]:


# 计算平均工资
data['基本工资'].mean()


# In[19]:


# 加班工资最高的金额是多少
data['加班工资'].max()


# In[22]:


# 人名是GARY JIMENEZ的基本工资有多少
data[data['员工姓名']=='GARY JIMENEZ']['基本工资']


# In[24]:


# 收入最高的人是谁（总共支付加福利）
data[data['总共支付加福利']==data['总共支付加福利'].max()]['员工姓名']


# In[26]:


# 收入最低的人是谁（总共支付加福利）
data[data['总共支付加福利']==data['总共支付加福利'].min()]


# In[27]:


data.describe()


# In[28]:


data.info()


# In[32]:


# 每年所有员工的平均的基本工资是多少
data.groupby('入职年份').mean()['基本工资']


# In[41]:


# 任职人数最多的5个岗位    (排序) 正序和倒序
data.groupby('员工职位').count()['员工姓名'].sort_values(ascending=False).head(8)


# In[43]:


# value_counts()是值计数统计
data['员工职位'].value_counts().head()


# In[44]:


# 这个机构有多少个工作岗位
data['员工'].nunique()


# In[56]:


# 2014年有多少个职位只由一个人担任
sum(data[data['入职年份']==2014]['员工职位'].value_counts()==1)


# In[60]:


data[data['入职年份']==2014].head()


# In[61]:


data[data['入职年份']==2014]


# In[62]:


data[data['入职年份']==2014]['员工职位'].value_counts()


# In[64]:





# In[63]:


data[data['入职年份']==2014]['员工职位'].value_counts()==1


# In[66]:


sum(data[data['入职年份']==2014]['员工职位'].value_counts()==1)


# In[ ]:




