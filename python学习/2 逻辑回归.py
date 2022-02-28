#!/usr/bin/env python
# coding: utf-8

# In[2]:


#通过seaborn 库直接下载数据
# import seaborn as sns
# iris = sns.load_dataset('iris')


#比较稳定的方式是先下载到本地导入

import pandas as pd

TargetData = pd.read_csv('D:\\深度之眼\\02-数据集&代码\\工具课数据集及代码\\工具课数据集及代码\\11\\iris.csv')
TargetData.head()


# In[5]:





# 查看数据
# 

# In[6]:


type(TargetData)


# In[7]:


TargetData.info()
#通过观察每列的数据量可以发现没有缺失值


# In[8]:


TargetData.describe()
#看各列数据的 统计数据， 数量，平均值，标准差，最小值，最大值


# In[9]:


TargetData.Species.value_counts()
# .species.vlaues_counts   对【字符串】变量进行统计


# 利用seaborn库中的pair   plot观察变量之间的两两关系。

# In[10]:


import seaborn as sns 
sns.pairplot(data=TargetData,hue='Species')


# In[11]:


#通过观察可视化呈现可以发现花萼的长度并没有太好的区分度，为了运行效率， 我们可以考虑去掉

TargetData=TargetData.drop(['Sepal.Length','Sepal.Width'],axis=1)
TargetData.head()

# 1.2  事先为有监督学习算法准备标签，并将文本格式的标签变为整数型。
训练时候的标签需要从字符串变换为数字型，利用sklearn编码器功能实现
# In[16]:


from sklearn.preprocessing import LabelEncoder  #调用sklean函数中的LableEncoder 函数
encoder  = LabelEncoder()  #初始化  将LableEncoder 函数 赋给 encoder 
TargetData['Species']=encoder.fit_transform(TargetData['Species']) #先fit转换为set, 然后在transform。
#TargetData   # 相当于sql中的   group 然后  rename 成整数，好处是可以重溯 数字对应的字符串是什么。  如果单纯的人工强制变为数字，则不能重溯


# #1.3 将数值差异天然过大的数据进行归一化处理，也就是标准化处理
# 

# In[15]:


from sklearn.preprocessing import StandardScaler
import pandas as pd


# In[18]:


trans=StandardScaler()
TD_std= trans.fit_transform(TargetData[['Petal.Length','Petal.Width']])
TD_std=pd.DataFrame(TD_std,columns=['Petal.Length','Petal.Width'])
TD_std.head()


# # 1.4 将数据拆分为训练集和测试集，  此处不涉及验证集
# 

# In[19]:


from sklearn.model_selection import train_test_split
train_set,test_set=train_test_split(TargetData,test_size=0.2)

print(test_set.head())
print(train_set.head())


# # 1.5 最终分组，将特征x和标签y分开
# 

# In[20]:


test_set=test_set[['Petal.Length','Petal.Width','Species']]

train_x_set=train_set[['Petal.Length','Petal.Width']]
train_y_set=train_set['Species'].copy()

test_x_set =test_set[['Petal.Length','Petal.Width']]
test_y_set=test_set['Species'].copy()

train_x_set.head()


# In[21]:


train_y_set.head()


# In[22]:


test_x_set.head()


# In[23]:


test_y_set.head()


# # 1.2  算法实现

#  1   逻辑回归处理分类问题

# In[24]:


from sklearn.linear_model import LogisticRegression
#导入逻辑回归，并了解其中重要参数

LogisticRegression?
solver = 'warm'       此处是可选择不同的求解器，如果特征本身范围相近，用Sag  或者saga  求解可以更快收敛
max_iter=100         此处设置最大迭代次数
multi_class = 'warn'   此处设置解决多分类问题时采取的方式，默认一对多 ovr
# In[72]:


clf = LogisticRegression(solver='saga', max_iter=2000,multi_class='auto')  #函数赋值
clf


# *  训练

# In[73]:


clf.fit(train_x_set,train_y_set)


# * 预测

# In[74]:


res=clf.predict(test_x_set)
print(res)
print(test_y_set.values)


# * 评估

# In[75]:


accuracy =clf.score(test_x_set,test_y_set)
print('预测正确率：{:.0%}'.format(accuracy))


# * 结果可视化

# In[76]:


#定义绘图函数 draw（）

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

def draw(clf):

    # 网格化
    M, N = 500, 500
    x1_min, x2_min = TargetData[["Petal.Length", "Petal.Width"]].min(axis=0) # 取两根轴的最值，axis=0表示沿竖轴运作，
    x1_max, x2_max = TargetData[["Petal.Length", "Petal.Width"]].max(axis=0) # 因此取的就是花瓣长度和宽度的最值。
    t1 = np.linspace(x1_min, x1_max, M) # 将两根轴等差均分成500段并赋值给向量t1 t2
    t2 = np.linspace(x2_min, x2_max, N)
    x1, x2 = np.meshgrid(t1, t2) 
    # 用meshgrid生成两个数组，第一个是t1，t2交叉后所有点的横坐标；第二个数组是纵坐标；并分别把所有横，纵坐标赋值给x1和x2两个向量
    
    # 预测
    x_show = np.stack((x1.flat, x2.flat), axis=1) #flat功能先将x1和x2拉平成长度为【500】的数组，stack函数在第二维度（axis=1）上增加，
                                                  #组成【500，2】的矩阵，每一行其实就是某一个点的坐标。
    y_predict = clf.predict(x_show)               #为每个点预测分类结果，为绘制预测区域做准备。形状为【500，1】
    
    # 配色
    cm_light = mpl.colors.ListedColormap(["#A0FFA0", "#FFA0A0", "#A0A0FF"])
    cm_dark = mpl.colors.ListedColormap(["g", "r", "b"])
    
    # 绘制预测区域图
    plt.figure(figsize=(10, 6))#生成图像区域，并指定比例
    plt.pcolormesh(t1, t2, y_predict.reshape(x1.shape), cmap=cm_light) 
    #pcolormesh用来画背景预测区域，t1横坐标，t2纵坐标，第三项分类标签，第四项颜色
    
    # 绘制原始数据点
    plt.scatter(TargetData["Petal.Length"], TargetData["Petal.Width"], label=None,
                c=TargetData["Species"], cmap=cm_dark, marker='o', edgecolors='k')
    plt.xlabel("Petal.Length")
    plt.ylabel("Petal.Width")
    
    # 绘制图例
    color = ["g", "r", "b"]
    species = ["setosa", "virginica", "versicolor"]
    for i in range(3):
        plt.scatter([], [], c=color[i], s=40, label=species[i])    # 利用空点绘制图例
    plt.legend(loc="best")
    plt.title('iris_classfier')


# In[77]:


#绘图
draw(clf)


# In[42]:


#结果输出
out= test_x_set.copy()
out["y"]=test_y_set
out["pre"]=res
out


# In[33]:


out.to_csv("iris_predict.csv")


# In[43]:


get_ipython().run_line_magic('pinfo', 'LogisticRegression')
   


# In[ ]:




