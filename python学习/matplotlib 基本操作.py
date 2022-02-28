#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 


# ### 折线图

# In[5]:


data= pd.read_excel("D:/数据分析/10周学会数据分析/材料/7数据可视化/第三周代码及数据/折线图.xlsx")
data.head()


# In[6]:


# Excel中的日期，是从1900年1月1日开始存储的，那么这一天将会以数字的形式存储成1
# origin 这个参数的意思是从哪一天开始计算
# Excel有一个时间计数上的bug，1900年的2月份给记成了29天



data['日期']=pd.to_datetime(data['日期']-2,unit='d',origin=pd.Timestamp("1900-01-01"))


# In[7]:


data.head()


# In[11]:




from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

plt.xticks(rotation=45)
#绘制折线图，第一参数是x轴，第二参数是y轴
plt.plot(data['日期'],data['总销售额'])
plt.show()


# In[12]:


#设置画布的大小 figsize 设置长宽
plt.figure(figsize=(20,5))
#设置x轴的倾斜角度
plt.xticks(rotation=45)
#设置color颜色
plt.plot(data['日期'],data['总销售额'],color='red')
plt.show()


# In[16]:


#一个图上画多个折线图
# linewidth  这个参数是设置线宽的。
#linstyle 这个参数是设置线的格式的
#marker 这个是设置线的拐点的样式的

plt.figure(figsize=(20,5))
plt.plot(data['日期'],data['总销售额'],color='red',linewidth=2,linestyle='-')
plt.plot(data['日期'],data['FBA销售额'],color='blue',linewidth=1,linestyle='-.')
plt.plot(data['日期'],data['自配送销售额'],color='green',linewidth=1,linestyle=':')
plt.xticks(rotation=45)
font = {
    "family":"SimHei",  #  这个是设置字体的
    "size":"20"  #  这个是设置字体大小的
}

plt.rc("font",**font)
#设置x轴的标签
plt.xlabel("时间")
plt.ylabel("销售额")
plt.show()


# In[17]:


#柱状图
data = pd.read_excel("D:/数据分析/10周学会数据分析/材料/7数据可视化/第三周代码及数据/长尾分布.xlsx")
data.head()


# In[20]:


#柱状图
plt.figure(figsize=(20,5))
plt.bar(data['排序'],data['销量'])

plt.show()


# In[24]:


plt.figure(figsize=(20,5))

plt.xticks(rotation=45)


plt.bar(data['排序'],height=data['销量'])
#plt.show()

#现在设置四周线
ax = plt.gca()
ax.spines["right"].set_color("white")
ax.spines["left"].set_color("orange")
ax.spines["top"].set_color("yellow")
ax.spines["bottom"].set_color("purple")


plt.xlim(data.index.values[0],data.index.values[-1])

plt.ylim(np.min(data["销量"]),np.max(data["销量"]))

plt.show()


# In[30]:


#条形图
plt.figure(figsize=(20,5))


plt.xticks(rotation=30)
plt.barh(data['排序'],data['销量'])

ax=plt.gca()

# 设置右侧颜色
ax.spines["right"].set_color("white")
# 修改左侧颜色
ax.spines["left"].set_color("orange")
# 修改上边颜色
ax.spines["top"].set_color("yellow")
# 修改下边颜色
ax.spines["bottom"].set_color("purple")


plt.show()


# In[31]:


# 饼图

data = pd.read_excel("D:/数据分析/10周学会数据分析/材料/7数据可视化/第三周代码及数据/折线图.xlsx")

data.head()


# In[32]:


plt.pie([1,2,3])
plt.show()


# In[37]:


# 需要先对数据进行运算后再进行绘制

plt.figure(figsize=(20,5))

font={
    "family":"SimHei",
    "size":"15"
}

plt.rc("font",**font)

#把三个渠道的销售总额算出来
sum_sales =np.sum(data['总销售额'])
FBA_sales = np.sum(data["FBA销售额"])
self_sales=np.sum(data["自配送销售额"])


plt.pie([sum_sales,FBA_sales,self_sales]
       ,labels=['总销售额',"FBA销售额","自配送销售额"]
       ,colors=["red","blue","green"]
       ,shadow=True
       ,labeldistance=1.1
       ,autopct="%.2f%%"
       ,startangle=150
       ,explode=[0.1,0.1,0.1])


plt.title("各渠道销售占比",fontdict={"family":"SimHei","size":30},loc="right")

plt.show()


# In[38]:


# 散点图
data = pd.read_excel("D:/数据分析/10周学会数据分析/材料/7数据可视化/第三周代码及数据/气泡图.xlsx")
data.head()


# In[40]:


plt.scatter(data["平均单个订单成本"],data["订单额"]
           ,color="#6A5ACD")
plt.show()


# In[42]:


## 随机生成RGB颜色  RGB颜色组成就是 一个# 加上任意的6个十六进制的字符组成的
import random 
def random_colors(numbers):
    colors=[]
    number=0
    while number <numbers:
        color_arr=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
        color=""
        for i in range(6):
            color+=color_arr[random.randint(0,len(color_arr)-1)]
        
        color = "#"+color
        colors.append(color)
        number+=1
    return colors
colors =random_colors(10)
colors


# In[44]:


plt.scatter(data["平均单个订单成本"],data["广告ROI"]
           ,s=data["订单额"]  #这个是设置球的大小
           ,color=colors   #设置球的颜色
           ,marker="h"    #设置biankuang 
           ,linewidths=3   #设置边框的宽度
           ,edgecolors="b"  #设置边框的颜色，如果没有设置边框的颜色，那么边框就跟球的颜色一样
           ,alpha=1   #设置透明度
           )

plt.show()


# In[46]:


#  气泡图颜色渐变

import random
data1 = data.sort_values("订单额")
x = []

for i in data1.index.values:
    x.append(random.randint(100,1000))
data1["人力投入"]= x
data1 


# In[47]:


plt.figure(figsize=(20,5))
plt.scatter(data1["平均单个订单成本"],data1['订单额']
           ,s=data1["人力投入"]
           ,marker="h"
           ,c=data1["广告ROI"]
           ,cmap="winter"
           )
plt.colorbar()
plt.xlabel("订单成本")
plt.ylabel("订单额")

plt.text(0,-4000,s="颜色深浅代表ROI ，球的大小代表人力投入",fontdict={"size":20})

plt.show()


# In[48]:


#直方图
data = pd.read_excel("D:/数据分析/10周学会数据分析/材料/7数据可视化/第三周代码及数据/直方图.xlsx")
data.head()


# In[49]:


plt.figure(figsize=(20,5))
plt.hist(data["数量"])
plt.show()


# In[50]:


#频数的直方图，
plt.figure(figsize=(20,5))
data1 = data[data["数量"]>20]
plt.hist(data1["数量"]
        ,bins=data1.index.values[-1]
        ,align="mid")

plt.xlim(20)
plt.show()


# In[51]:


#频率直方图

plt.figure(figsize=(20,5))
data1 = data[data["数量"]>20]

plt.hist(data1["数量"]
        ,bins=data1.index.values[-1]
        ,align="mid"
        ,density=True)

plt.xlim(20)
plt.show()


# In[52]:


# 箱型图
data = pd.read_excel("D:/数据分析/10周学会数据分析/材料/7数据可视化/第三周代码及数据/长尾分布.xlsx")
data.head()


# In[53]:


plt.boxplot(data[data["销量"]<2000]["销量"])
plt.show()


# In[54]:


# 横线上边的可以看做是异常值，也叫离群点。  
# 横线是上限值
# 依次往下是上4分位、中位数、下4分位数、下限
# 上4分位数的意思是全部数据中有4分之一的数据比它大
# 下4分位数的意思是全部数据中有4分之一的数据比它小
# 中位数的意思就是位于中间的数据
# 上4分位减去下4分位数代表着4分位的间距，那么异常值（离群点）就是大于  (上四分位 + 1.5 * 四分位间距) 或小于(下4分位 - 1.5*四分位间距)的数字
# 上限值就是等于（上4分位 + 1.5 * 四分位间距）的值


# In[58]:


## 箱型图也可以同时绘制多个

data1 = [data[data["销量"]<2000]["销量"],data[data["销量"]<3000]["销量"]]


plt.boxplot(data1
           ,notch=True
           ,sym='b'
            ,vert=True
            ,whis=2
            ,labels=["箱型图1","箱型图2"]
            ,showmeans=True
            ,meanline=True
            ,showfliers=True
            ,meanprops=dict(markerfacecolor="r",marker="s")
            ,widths=0.3
           )
plt.show()


# In[60]:


# 子图绘制

x = np.arange(1,100)

plt.subplot(221)
plt.plot(x,x*x)


plt.subplot(222)
plt.scatter(np.arange(0,10),np.random.rand(10))

plt.subplot(223)
plt.pie(x= [1,2,3,4],labels=['a','b','c','d'])

plt.subplot(224)
plt.bar(x=[1,2,3,4,5],height=[2,3,4,5,6])

plt.show()



# In[63]:


x = np.arange(1,100)
# 第一个图就是两行，两列中的左上的那个图，也就是第一个  221的意思
plt.subplot(221)
plt.plot(x,x*x)

# 这个图是绘制右上的那一个，是把整个画布看做是2行2列的图形 绘制第二个
plt.subplot(223)
plt.scatter(np.arange(0,10), np.random.rand(10))


plt.subplot(122)
plt.bar(x=[1,2,3,4],height=[4,3,6,5])

plt.show()


# In[64]:


x = np.arange(1,100)

# 第一个图就是两行，两列中的左上的那个图，也就是第一个  221的意思
plt.subplot(221)
plt.plot(x,x*x)

# 这个图是绘制右上的那一个，是把整个画布看做是2行2列的图形 绘制第二个
plt.subplot(222)
plt.scatter(np.arange(0,10), np.random.rand(10))

plt.subplot(212)
plt.bar(x=[1,2,3,4],height=[4,3,6,5])

plt.show()


# In[65]:


data = pd.read_csv("D:/数据分析/10周学会数据分析/材料/7数据可视化/第三周代码及数据/特斯拉股票.csv")
data.head()


# In[70]:


data1 = data.head(100)
plt.figure(figsize=(14,7))

plt.suptitle("特斯拉股票")

fig1 = plt.subplot(3,1,(1,2))
fig1.plot(data1["Date"],data1["Open"])

fig2 = plt.subplot(3,1,3)
fig2.bar(data1["Date"],data1["Volume"])


plt.show()


# In[ ]:




