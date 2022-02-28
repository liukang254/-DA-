#!/usr/bin/env python
# coding: utf-8

# In[181]:


import numpy as np  
import pandas as pd
data = pd.read_excel('data_excel.xlsx')
#


# # 总结
# - 本次总共学会了如下的操作。
# - 1. 【广播运算】，考虑线，面，体就行。
# - 2. 【数据的堆叠】，四个方法，行维度和列维度各两个
# - 3. 【numpy的降维】，有三种方法，ravel,flatten,reshape(-1)共同点是直接操作都不会改变原来的numpy的数据，并且三种方法都可以添加：order = 'F' 来实现降维后排序的功能，从小到大。区别点：flatten 改变数值，不会影响原来的数据，另外两个回影响原来的数据。
# - 4. 【花式索引】，主要是可以隔行提取数值，间隔取数，arr[[1,2,4],[4,5,7]
# - 5. 【转置】 .T
# - 6. 【切片操作】，使用冒号，跟列表一样。
# - 7. 【矢量化】，也就是不使用循环程序，实现批量处理数据的目的，列表和python中的array是不一样的。
# - 8. 【zero(),ones(),empty(),arange()】, 类型转换:astype(np.int64)
# - 9. ndim 维度， shape 形状，
# - 10. 【读取大文件】，采用chunksize=**  可以每次只读取**行。然后使用for 循环，遍历数据，
#     或者使用nrows  只读取前几行。注意与head的区别。
# - 11.【查找缺失值】，pd.isnull()或者 **.isnul() , isnull = isna   结果是布尔型的Series 
# - 12. 【声明一个series】 ， pd.Series(列表名)  或者pd.Series([liebiao],index="") 或者是 pd.Series(字典)

# data.info()

# In[6]:


data.head()


# In[8]:


data.describe()


# In[9]:


type(data)


# In[10]:


type(data['id'])


# ### Series 是Dataframe的列  Dataframe 是表，

# In[11]:


data['id']


# In[12]:


my_list=[1,2,3,4]
my_list[0]


# ### 自己声明一个Series

# In[13]:


obj = pd.Series(my_list)
obj


# In[16]:


obj.index


# In[17]:


obj.values


# In[18]:


obj.value_counts


# In[19]:


obj = pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])
obj


# In[20]:


obj= {
    'a':1,
    'b':2,
    'c':3
}
obj_1=pd.Series(obj)
obj_1


# In[21]:


obj_1['b']


# ###  数据处理

# ## 缺失值处理
# 

# In[36]:


data={
    'a':1,
    'b':None,
    'c':""
}
obj = pd.Series(data)
obj
#如果这一列内容是数值型的，那缺失值则显示Nan, 如果是字符串，则显示None


# In[ ]:


#isnull  等于  isna 


# In[37]:


pd.isnull(obj)


# In[38]:


pd.isna(obj)


# In[39]:


obj.isnull()


# In[40]:


obj.notnull()


# ## 算数运算和数据对齐

# In[42]:


d1 = pd.Series([1.3,1.5,2.6,-3.2], index=['a','b','c','d'])
d2 = pd.Series([-1.5,-1.2,-2.0,3.2,4.5], index=['a','b','c','d','e'])
d1


# In[43]:


d2


# In[44]:


d1+d2
#是位置对应相加


# In[47]:


#补充知识：pandas 如何读取大数据量文件
data1=pd.read_csv("executive.csv",nrows=5)
#与head的区别是使用head()是只显示前几行，使用nrows 是只读取前几行。d
data1


# In[49]:


data2 = pd.read_csv("executive.csv",chunksize=100)
data2


# In[50]:


for d in data2:
    print(d)


# ### Numpy
# - Numpy 其实就是一个多维的数组，（列表、list）对象【1，2，3，4，5】

# In[53]:


import numpy as np
data=[1,2,3,4]
n = np.array(data* 10)
n


# In[54]:


data=[1,2,3,4]
data


# In[55]:


n.shape


# In[56]:


arr= [[1,2,3,4],[5,6,7,8]]
arr


# In[57]:


arr2=np.array(arr)
arr2


# In[58]:


arr2.shape


# In[59]:


arr2.ndim


# In[61]:


arr = [
    [
        [1,2],
        [3,4]],
       
       [
        [5,6],
        [7,8]]
]
arr3=np.array(arr)
arr3


# In[62]:


arr3.ndim


# In[63]:


arr3.shape


# ### Numpy对数据类型进行合理推断

# In[64]:


arr = [["a","2",3,4],[5,6,7,8]]
arr2 = np.array(arr)
arr2


# In[65]:


arr = [[1.2,3,4,5],[5,6,7,8]]
arr2 = np.array(arr)
arr2


# ### numpy创建指定长度的数组

# In[66]:


np.zeros(10)


# In[68]:


np.ones((2,3))


# In[69]:


np.empty((2,3,4))


# In[72]:


np.arange(1,10)


# In[76]:


##数据类型转换

arr = np.array([1.7,1.234,-1,23,22,34])
arr


# In[74]:


arr.astype(np.int64)


# ## 矢量化
# ### 在不用编写循环的情况下就可以进行批量运行，这就叫矢量化

# In[77]:


arr1 = [1,2,3,4]
arr2 = [5,6,7,8]
arr1 + arr2


# In[78]:


arr1 = np.array([1,2,3,4])
arr2 = np.array([5,6,7,8])
arr1 + arr2


# In[79]:


arr1 - arr2


# In[80]:


arr1 * arr2


# In[81]:


arr1 * 5


# In[82]:


arr1 / arr2


# ## 切片操作

# In[83]:


arr = np.arange(10)
arr


# In[84]:


arr[4]


# In[85]:


arr[:3]


# In[87]:


arr[1:4]=11


# In[88]:


arr


# In[89]:


arr1 = np.array([[1,2,3,4],[5,6,7,8]])
arr1


# In[91]:


arr1[1][1]


# In[93]:


names = np.array(["HanMeiMei","LiLei","Tony","Jack"])
names=='HanMeiMei'


# In[94]:


names[2]


# In[95]:


(names=='HanMeiMei') &(names=="Tony")


# In[96]:


(names=='HanMeiMei') | (names=="Tony")


# ## 花式索引 Fancy Indexing
# - 这是numpy 的术语，指的是利用整数数组进行索引。

# In[111]:



import numpy as np
arr = np.empty((8,4))
for i in range(8):
    arr[i]=i
arr


# In[112]:


arr[[2,3,4,8,]]


# In[126]:


arr = np.arange(32).reshape((8,4))
arr 


# In[127]:


arr[[2,3]]


# In[119]:


arr[[2,3,1],[1,1,1]]


# In[120]:


arr = np.arange(15).reshape(5,3)
arr


# In[121]:


arr.T


# In[122]:


arr.transpose()


# ## numpy 的降维操作

# In[128]:


arr=np.array([[1,10,100],[2,20,200],[3,30,300]])
arr


# In[130]:


# ravel  降维操作，是二维降为一维，不改变顺序，且不改变原来的np数组
data = arr.ravel()
data


# In[131]:


arr.reshape(-1)
#reshape  也是可以降维的。并且也不改变原来的 


# In[132]:


arr


# In[133]:


arr.flatten()
#flatten 跟前面的一样


# In[135]:


##改变排序的降维操作
arr.ravel(order='F')
# order=F   可以按着从小到大的改变顺序


# In[136]:


arr


# In[138]:


arr.flatten()[0]=1000


# In[139]:


arr


# In[140]:


arr.ravel()[1]=1000
arr


# In[144]:


arr.reshape(-1)[4]=2222
arr


# In[146]:


arr.ravel()


# In[147]:


arr


# ##  numpy 堆叠操作

# In[148]:


arr1 = np.array([[1,10,100],[2,20,200],[3,30,300]])
arr2 = np.array([1,2,3])
arr1


# In[149]:


arr2


# In[150]:


np.vstack([arr1,arr2])


# In[152]:


np.row_stack([arr1,arr2])


# In[153]:


arr3 = np.array([4,5,6])


# In[154]:


np.hstack([arr2,arr3])


# In[155]:


arr4 = ([7],[8],[9])
np.hstack([arr1,arr4])


# In[156]:


np.column_stack([arr1,arr4])


# ### 总结一下，数据堆叠有两种，
# - 一种行方向上的堆叠，有两种方法， vstack 或者是row_stack   要求是 两个数组的列是一样的。
# - 一种列方向上的堆叠，有两种方法， hstack 或者是 column_stack  要求是两个数组行是一样的。
# 

# ### 广播运算

# In[163]:


arr1 = np.arange(12).reshape(3,4)
arr2 = np.arange(101,113).reshape(3,4)
print(arr1)
print(arr2)


# In[ ]:


# 对位相加不是广播运算


# In[ ]:





# In[161]:


arr1 +arr2


# In[164]:


arr1 = np.arange(60).reshape(5,4,3)
arr2 = np.arange(12).reshape(4,3)#
#从后面开始维度都是一样的，是可以广播运算的。


# In[165]:


arr1+arr2


# In[177]:


arr1 = np.arange(60).reshape(5,4,3)
arr2 = np.array([1,2,3])


# In[178]:


arr1


# In[179]:


arr2


# In[180]:


arr1+arr2


# In[174]:


arr1 = np.arange(12).reshape(4,3)
arr2=np.array([1,2,3])
arr1


# In[175]:


arr2


# In[176]:


arr1+arr2


# In[ ]:


# 总结  广播运算有三种情况
#  总的来讲就是 线 ，面，体传播的三种情况
#1. 线滑动成面，一维的逐行或者是逐列滑动到二维上
#2 .线滑动成面，二维的逐维度滑动成体
#2. 线 滑动成体，一维的逐行或者是逐列滑动成三维的。


# 

# In[ ]:




