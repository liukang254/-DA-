#!/usr/bin/env python
# coding: utf-8

# # 快捷键
# # 运行  shift + 回车 执行此代码块
# # alt + 回车 执行此代码块并插入一个空行
# # 标记是什么？
# - 标记是一个叫做markdown的格式来编辑文件

# ###  知识点
# - Pandas的安装  
# 
# 1.命令行中安装 pip install pandas 用这种方法安装需要重新启动jupyter来加载新的包
# 
# 2.jupyter中安装   !pip install pandas 用这种方法安装就可以直接使用安装的包了

# In[7]:


# 导包
import pandas as pd
# 这里的import是关键字，以后你想导入什么包就import什么
# as 的意思是起一个别名，我下边再用到pandas的时候，就可以直接使用pd了


# In[13]:


# 使用Pandas读取Excel中的文件
sheet1_data = pd.read_excel("../aaa/a/数据分析测试题1.xlsx")
sheet1_data


# ###  read_excel的参数怎么写
# - 第一个参数支持的就是一个路径（绝对路径和相对路径）
# - 绝对路径是从根目录开始的 mac的根目录 : /aaa/bb/cc  windows的根目录 D:/aaa/bb/cc
# - 相对路径的意思是：首先你要相对谁(我启动jupyter的那么文件夹) ，然后 ..表示上一级目录  .代表当下目录，可以写也可以不写

# ### jupyter 中查看函数的参数 怎么办
# - 快捷键是 shift + tab
# 

# In[14]:


sheet2_data = pd.read_excel("数据分析测试题.xlsx",sheet_name="第一阶段第二套")
sheet2_data


# In[19]:


sheet3_data = pd.read_excel("数据分析测试题.xlsx",sheet_name="第一阶段第三套")
sheet3_data


# In[16]:


# 常用字符编码  utf-8 
# gbk


# In[21]:


type(sheet1_data)


# ###  Pandas中的数据类型有哪些
# - Series
# - DataFrame

# In[22]:


# 我们自己要声明一个DataFrame应该怎么写
df1 = pd.DataFrame({
    "a":[1,2,3],
    "b":[4,5,6]
})

df1


# In[23]:


df1 = pd.DataFrame({
    "a":[1,2,3],
    "b":[4,5,6]
},index=[100,101,102])
df1


# In[25]:


# head函数的功能是默认读取前5行
sheet1_data.head(3)


# In[26]:


# tail函数的功能是读取末尾的数据
sheet1_data.tail()


# In[28]:


# 查看索引
sheet1_data.index


# In[30]:


for i in range(1,10,2):
    print(i)


# In[31]:


# 查看数据形状
sheet1_data.shape


# In[33]:


sheet1_data.info()
# object 其实他就是字符串
# int32 or int64  这都是整数，只是精度不同


# In[34]:


sheet1_data.describe()


# In[35]:


sheet1_data.values


# In[36]:


type(sheet1_data.values)


# In[37]:


sheet1_data.size


# In[42]:


sheet1_data.ndim


# In[44]:


sheet1_data.head(1)


# ### DataFrame的访问操作

# In[46]:


# 访问某一列数据怎么办
sheet1_data["题干"].head()


# In[41]:


type(sheet1_data["题型"])


# In[51]:


sheet1_data[["题型","难度","题干"]].head()
# [1,2,3,4]


# In[52]:


sheet1_data.columns


# In[53]:


df1 = pd.DataFrame({
    "a":[1,2,3],
    "b":[4,5,6]
},index=[100,101,102])
df1


# In[54]:


df1[[True,False,True]]


# In[55]:


# 在咱们这份题库数据中，请筛选出难度2的所有题目
sheet1_data.head(1)


# In[74]:


# and   or 
# pandas 多条件判断   &  | 表示and或者是or
sheet1_data[(sheet1_data["难度"]==2) | (sheet1_data["难度"]==3)].head(1)


# In[77]:


# loc访问数据， 访问行和列同时筛选
sheet1_data.loc[[1,3,5],"题型"]


# In[79]:


# 问：访问行完了之后，想筛选多列数据怎么办
sheet1_data.loc[[1,3,5],["题型","题干"]]


# In[85]:


# 访问从某一列开始的后边所有列
sheet1_data.loc[45:,"题型":]


# In[86]:


# 行筛选后，访问哪列到哪列
sheet1_data.loc[45:,"题型":"题干"]


# In[87]:


# 总结loc可以提供给我们一个自由访问DataFrame的功能
# 支持两个参数，但参数必须首先要使用一个中括号包裹   sheet1_data.loc[]
# 第一个参数表示行，第二个参数表示列
# 当第一个参数使用[]包裹，也就是列表的时候，表示你明确的要哪一行的数据
# 当第一个参数不用[]包裹，使用冒号，那么就表示从哪行开始一直到最后或到具体哪一行
# 第二参数表示列的筛选，具体方式跟行相同


# ####loc 和 iloc 区别
# - loc是使用字段的名称进行访问
# - iloc使用的是索引数字
# 

# In[88]:


sheet1_data.head(1)


# In[89]:


sheet1_data.iloc[1:3,2:4]


# In[91]:


# 这种方式也是可以访问行和列的
sheet1_data["题干"][3]


# In[95]:


sheet1_data[["题干","选项（如果有）"]][3:6]


# In[96]:


# at ,应用在选择单个值
sheet1_data.at[1,"题干"]


# In[97]:


sheet1_data.loc[1,"题干"]


# In[99]:


sheet1_data.iloc[1,4]


# In[100]:


sheet1_data.iat[1,4]


# In[ ]:





# In[107]:


# 数据合并,多个sheet页中的或多个Excel表格中的数据合并到一起
#concat
pd.concat([sheet1_data,sheet2_data,sheet3_data])


# In[108]:


df1


# In[109]:


pd.concat([sheet1_data,sheet2_data,sheet3_data,df1])


# In[110]:


final_data = pd.concat([sheet1_data,sheet2_data,sheet3_data])
final_data.head(1)


# In[111]:


# 把处理后的数据重新写入一个新的Excel文件中
final_data.to_excel("final_data.xlsx",sheet_name="第一阶段三套题汇总")


# In[116]:


# 先声明一个字典
d = {
    "姓名":["建国","爱国","卫国","建军"],
    "年龄":[17,18,19,20]
}
df3 = pd.DataFrame(d)
df3


# In[123]:


# 增删改查   CRUD  create  read  update  delete
# 新增一行
df3.loc[4] = ["爱党",21]


# In[124]:


df3


# In[125]:


# 新增一列
df3["是否入党"] = ["是","否","是","否","是"]


# In[126]:


df3


# In[127]:


ddf3 = df3.drop(0)


# In[128]:


ddf3


# In[129]:


df3


# In[130]:


# inplace参数的意义是是否要作用在原数据上
df3.drop(0,inplace=True)
df3


# In[132]:


# 如何删除一列的数据
ddf4 = df3.drop(["年龄"],axis=1)


# In[133]:


ddf4


# In[134]:


df3.drop(["年龄"],axis=1,inplace=True)


# In[135]:


df3


# In[ ]:




