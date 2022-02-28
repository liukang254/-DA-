#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt


# In[3]:


data = pd.read_csv("用户基本信息.csv")

data.head()


# #  数据说明
# - userid 用户编号
# - cms_segid 微信ID
# - cms_group_id 微信群ID
# - final_gender_code 性别 1是男2是女
# - age_level 年龄层次
# - pvalue_level 消费档次
# - shopping_level 购物档次
# - occupation 是不是大学生
# - new_user_class_level 城市层级

# In[6]:


data.shape


# In[7]:


chunksize=10000


user_info_chunk = pd.read_csv("用户基本信息.csv",chunksize=chunksize)

user_info = pd.DataFrame()


# In[9]:


type(user_info)


# In[10]:


start_index = 0

for u in user_info_chunk:
    print("正在处理第"+str(start_index)+"行数据")
    user_info = user_info.append(u.loc[start_index],ignore_index=True )
    start_index +=chunksize
print("处理完成。")


# In[12]:


user_info


# In[14]:


user_info["shopping_level"].unique()


# In[15]:


### 我要看一下这3个购物等级各自占比情况

user_info.groupby("shopping_level").count()["age_level"]


# In[16]:


font = {
    'family':"SimHei",
    "size":"15"
}
plt.rc("font",**font)
plt.pie(user_info.groupby("shopping_level").count()["age_level"]
       ,labels=[1,2,3]
       ,autopct="%.2f%%")
plt.title("购买等级占比")
plt.show()


# # 热力图
# 

# In[18]:


x = [[1,2]
     ,[3,4]
     ,[5,6]]
plt.imshow(x)


# In[19]:


# 先单个计算 age_level的基本情况
age_level_group_data = user_info.groupby("age_level").count()
age_level_group_data


# In[20]:


age_level_group_data.index.values


# In[21]:


for i in age_level_group_data.index.values:
    user_info["age_level"]==i
    print(user_info)


# In[22]:


for i in age_level_group_data.index.values:
    print("age_level为{}的shopping_level的情况是".format(i))
    print(user_info[user_info["age_level"]==i].groupby("shopping_level").count()["age_level"])


# In[23]:


# 创建一个空的列表
x = np.empty((3,0))
x


# In[24]:


for i in age_level_group_data.index.values:
    print("age_level为{}的shopping_level的情况是".format(i))
    result = user_info[user_info["age_level"]==i].groupby("shopping_level").count()["age_level"]
    print(result)
    
    # 要解决的是把空的行补成0
    if len(result) != 3:
        print("长度不是3，判断具体哪个值是缺失的，然后补0")
        # 先声明一个含有3个索引的数组，思路是，下边迭代出来的元素依次删除，剩下的就是没有的
        arr = [1,2,3]
        for i in result.index.values.astype(int):
            arr.remove(i)
        
        # 遍历arr中剩余的元素，并且把result中没有的位置赋值为0
        for a in arr:
            result[float(a)]=0
        
        result = result.sort_index()
        print(result)
    x = np.column_stack((x,result))
    
    
print(x)


# In[25]:


plt.imshow(x,
          cmap="YlGn")


plt.xlabel("年龄层次")
plt.ylabel("购物等级")

#

plt.xticks(np.arange(6), np.arange(1,user_info["age_level"].unique().astype(int).max() + 1))
plt.yticks(np.arange(3), np.arange(1,user_info["shopping_level"].unique().astype(int).max() + 1))
plt.colorbar()
plt.show()


# In[ ]:




