#!/usr/bin/env python
# coding: utf-8

# 第一部分 数据处理

# In[35]:


#导入数据并完成数据的处理

#引用pandas库     使用read_csv 文件路径 读取文件
import pandas as pd    
TargetData = pd.read_csv('D:\\深度之眼\\02-数据集&代码\\工具课数据集及代码\\工具课数据集及代码\\13\\iris.csv')

#读取文件后，根据之前的经验，我们删除不用的数据，或这是说特征不明显的数据。
# 用列表表示想要删除的列，【“字段名1”，“字段名2”】 axis  =1  表示删除的是列，  =0 表示删除的是行
TargetData=TargetData.drop(["Sepal.Length","Sepal.Width"],axis=1)

#删除后，我们将标签整数化，  使用的库是  sklearn  preprocessing   中的 LabelEncoder
#函数是  .fit_transform 
from sklearn.preprocessing import LabelEncoder

encoder= LabelEncoder()
# 将想要标签数字化使用对应的函数
TargetData["Species"] = encoder .fit_transform(TargetData["Species"])


#将数据标签化后，导入sklearn.model_selection.train_test_split  模块
from sklearn.model_selection import train_test_split

#使用该函数，对数据进行训练集和测试集的切割   测试集  20%    训练集80%

train_set,test_set= train_test_split(TargetData,test_size=0.2)

#设置测试集的各个字段
test_set=test_set[['Petal.Length','Petal.Width','Species']]  

train_x_set=train_set[['Petal.Length','Petal.Width']]
train_y_set=train_set[['Species']].copy()

test_x_set=test_set[['Petal.Length','Petal.Width']]
test_y_set= test_set[['Species']].copy()


# In[36]:


train_x_set.head()


# In[37]:


train_y_set.head()


# In[38]:


test_x_set.head()


# In[39]:


test_y_set.head()


# 定义可视化函数draw()

# In[50]:


#定义绘图函数 draw()

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt 

def draw(clf):
    #网格化
    M,N = 500,500
    x1_min,x2_min=TargetData[["Petal.Length","Petal.Width"]].min(axis=0) #取两根轴的最值，axis= 0 表示延竖轴运作
    x1_max,x2_max=TargetData[["Petal.Length","Petal.Width"]].max(axis=0) #因此取的值就是  花瓣长度和宽度的最值，
    t1=np.linspace(x1_min,x1_max,M)   
    t2=np.linspace(x2_min,x2_max,N)   #将两根轴等差的均分500段，并赋值给向量t1  和t2 
    
    x1,x2=np.meshgrid(t1,t2)
    
    #用meshgrid 生成两个数组， 第一个是t1 t2 交叉后所有点的横坐标，第二个数组是纵坐标，并分别把横纵坐标赋值给 X1 和x2 两个向量
    
    #预测
    x_show=np.stack((x1.flat,x2.flat),axis=1) #flat功能先将x1 x2 拉平成长度为500的数组，stack函数在第二个维度上（axis=1）上增加，
                                              #组成【500，2】的矩阵，每一行其实就是某一个点的坐标。
                                              #为每个点预测分类结果，为绘制预测区做好准备，形状为【500，1】
    y_predict=clf.predict(x_show)
    
    #配色
    
    cm_light=mpl.colors.ListedColormap(["#A0FFA0","#FFA0A0","#A0A0FF"])
    cm_dark=mpl.colors.ListedColormap(['g','r','b'])
    
    #绘制预测区域
    
    plt.figure(figsize=(10,6)) #生成图像区域，并指定比例
    plt.pcolormesh(t1,t2,y_predict.reshape(x1.shape),cmap=cm_light)
    #pcolormesh 用来画背景预测区域，t1横坐标，t2纵坐标，第三项分类标签，第四项颜色
    
    #绘制原始数据点
    
    plt.scatter(TargetData["Petal.Length"],TargetData["Petal.Width"],label=None,
               c=TargetData["Species"],cmap=cm_dark,marker='o',edgecolors='k')
    plt.xlabel=("Petal.Length")
    plt.ylabel=("Petal.Width")
    
    #绘制图例
    color=["g",'r','b']
    species=["setoa","virginica","versicolor"]
    for i in range(3):
        plt.scatter([],[],c=color[i],s=40,label=species[i])
    plt.legend(loc="best")
    plt.title('iris_classfier')
    
    
    
    


# 2 算法实现，决策树

# 采用CART  决策树算法

# In[41]:


from sklearn.tree import DecisionTreeClassifier
#导入决策树，并学习一下其中重要参数


# * DecisionTreeClassifier(
#     * criterion='gini', #此处决定特征划分的方法，默认使用CART算法的GINI系数
#     * max_depth=None,) #此处决定树的最大深度，默认为不设限

# In[123]:


clf=DecisionTreeClassifier(max_depth=5) #可尝试调整最大深度的参数来观察预测结果的变化。
clf


# * 训练

# In[124]:


clf.fit(train_x_set,train_y_set)


# * 预测

# In[125]:


res=clf.predict(test_x_set)
print(res)
print(test_y_set.values.T)


# * 评估

# In[126]:


accuracy= clf.score(test_x_set,test_y_set)
print("预测正确率：{:.0%}".format(accuracy))
print(accuracy)


# * 结果可视化

# In[127]:


#绘图
draw(clf)


# In[52]:


#结果输出
out =test_x_set.copy()
out["y"]=test_y_set
out["pre"]=res
out.head()


# 3 算法实现   随机森林

# In[112]:


from sklearn.ensemble import RandomForestClassifier
#导入随机森林
get_ipython().run_line_magic('pinfo', 'RandomForestClassifier')


# * RandomForestClassifier(
# * n_estimators='warn', #此处决定树的棵数，默认100棵
# * criterion='gini', #此处决定特征划分的方法，默认使用CART算法的GINI系数
# * max_depth=None,） #此处决定树的最大深度

# In[128]:


clf= RandomForestClassifier(n_estimators=200,criterion='entropy',max_depth=4)
clf


# * 训练

# In[129]:


clf.fit(train_x_set,train_y_set)


# * 预测

# In[130]:


res=clf.predict(test_x_set)
print(res)
print(test_y_set.values.T)


# * 评估

# In[131]:


accuracy = clf.score(test_x_set,test_y_set)
print("预测准确率：{:.0%}".format(accuracy))


# * 可视化

# In[132]:


#绘图
draw(clf)


# In[71]:


#结果输出
out = test_x_set.copy()
out["y"]=test_y_set
out["pre"]= res
out.head()


# In[ ]:




