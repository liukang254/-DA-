#!/usr/bin/env python
# coding: utf-8

# <h1>正则表达式</h1>
# <ol>
#     <li>
#         <a href='#正则的含义'>正则的含义</a>
#     </li>
#     <li>
#         <a href='#正则表达式的应用场景'>正则表达式的应用场景</a>
#     </li>
#     <li>
#         <a href='#常用的格式校验'>常用的格式校验</a>
#     </li>
#     <li>
#         <a href='#元字符'>元字符</a>
#     </li>
#     <li>
#         <a href='#反义代码'>反义代码</a>
#     </li>
#     <li>
#         <a href='#限定符'>限定符</a>
#     </li>
#     <li>
#         <a href='#分组匹配'>分组匹配</a>
#     </li>
#     <li>
#         <a href='#贪婪与非贪婪'>贪婪与非贪婪</a>
#     </li>
#     <li>
#         <a href='#分支条件匹配'>分支条件匹配</a>
#     </li>
#     <li>
#         <a href='#零宽断言'>零宽断言</a>
#     </li>
#     <li>
#         <a href='#项目实战'>项目实战</a>
#     </li>
#     <li>
#         <a href='#作业'>作业</a>
#     </li>
# 
# </ol>
# 

# ## 正则的含义

# - 正则表达式就是用来操作字符串的逻辑公式。

# ## 正则表达式的应用场景

# - 数据分析时数据获取时文本筛选
# - 写爬虫代码的时候，网页数据的匹配
# - 写前端代码的时候，用户输入数据的验证
# - 测试人员，对请求结果的数据验证
# - 批量文本编辑，比如sublime text或nodepad++ editplus等记事本软件中全部支持

# ## 常用格式校验

# - 邮箱验证
# - IP地址验证
# - 电话号码验证
# - 身份证号码验证
# - 密码强度验证
# - 网址验证
# - 汉字验证  [\u4e00-\u9fa5]
# - ......
# - 凡是有一定规律的,批量的数据获取，都可以使用正则表达式来完成

# In[8]:


import re 


s = "我们一起来看流星雨：womenyiqilaikanliuxingyu8？"

reg = "[a-z0-9]*\？"

re.findall(reg,s)


# In[10]:


re.findall('[\u4e00-\u9fa5]',s)


# In[12]:


#正式入门
s = 'hello world'
reg ='l'

re.findall(reg,s)


# In[13]:


type(re.findall(reg,s))


# ## 元字符

# | 字符| 说明|
# |-- |--|
# |. |代表的时换行符以外的任意字符，换行符是:\n \r\n |
# |\w |匹配任意字母，数字，下划线，汉字字的一个字符|
# |\s | 匹配任意的空白符|
# |\d| 匹配数字|
# |^ |匹配字符串的开始|
# |$| 匹配字符串的结束|

# In[15]:


s = """
1,成都,泸沽湖,1145,376,成都-泸沽湖3天2晚 | 入住7天酒店丽江古城中心店 + 成都航空往返机票,7天酒店丽江古城中心店 经济型 4.0分/5分,经济房-不含早-限时特... 其他 
不含早 1间2晚,成都航空 EU2237,直飞,19:45-21:20,
成都航空 EU2738,直飞,
23:30-01:05'
"""

r = re.findall('.',s)
print(r)


# In[17]:


r = re.findall('\w',s)
print(r)


# In[18]:


print(re.findall('[0-9a-zA-Z]',s))


# ## 反义代码

# 反义代码的意思就是与元字符表示相反的代码
# 
# - \W 匹配的任意 不是 字母、数字、下划线、汉字 的字符
# - \S 匹配任意 不是 空白符的字符
# - \D 匹配任意 不是 数字的字符

# ## 限定符

# |符号|说明|
# |--|--|
# |*|代表的重复0次或者是多次|
# |+|代表的是重复1次或者是多次|
# |?|代表的是重复0次或者是1次|
# |{n}|重复n次，举例：{3}指的就是重复3次|
# |{n,}|重复n次或者更多次数|
# |{n,m}|重复n次到m次，所以这里m一般要比n大|

# In[23]:


s = '贪心学院的官网是：http://www.greedyai.com'
reg = 'http://[w]{3}\.[a-z0-9A-Z]*\.com'

print(re.findall(reg,s))
print(re.findall('http://(.+)',s))


# In[25]:


## 比如匹配qq号
s = '我的qq号是42197393'
print(re.findall('\d+',s))
print(re.findall('\d{5,12}',s))


# ## 分组匹配

# In[44]:


s = '我的qq号是42197393 ,我的邮编是10000,  我的qq号是42197393 ,我的邮编是10000'

reg = '(\d{8}).*(\d{5})'

# print(re.findall(reg,s))
# re.findall(reg,s)

re.search(reg,s)


# In[39]:



re.search(reg,s).group()


# In[40]:


re.search(reg,s).group(0)


# In[41]:


re.search(reg,s).group(1)


# In[45]:


re.search(reg,s).group(3)


# In[47]:


# match

s = 'HelloWorldHelloGreedyAI'

reg = 'Hello'

re.match(reg,s)


# In[48]:


re.match(reg,s).group()


# ### findall , search ,match 的区别
# - findall 是找到所有的
# - search 是匹配第一个 
# - match 是匹配开头的

# ## 贪婪和非贪婪

# - 贪婪的意思是尽可能多的匹配
# - 非贪婪的意思就是尽可能少的匹配
# - 非贪婪操作符是问号：'符号?' 
# 
# 
# - ?号代表的是重复0次或者是1次，再加一个问号，代表的是非贪婪操作，那么最后就只匹配0次

# In[58]:


s = 'gggggggreedyaiiiiiiii'

reg = '\w+greedyai?'
re.findall(reg,s)


# ## 分支条件匹配

# -  使用 | 来分隔开不同的正则表达式，代表着 条件1 或 条件2 或条件3 ......
# 

# In[59]:


s = '电话号码有： 010-78472328      0431-9837523     0432-97462743'

# 分支条件匹配原则，前边的条件尽量匹配少的数据，后边的条件匹配多的数据
reg ='\d{3}-\d{8} | \d{4}-\d{7} |\d{4}-\d{8}'
re.findall(reg,s)


# ## 零宽断言
# - 匹配"正则表达式reg"前边的位置 (?=reg)
# - 匹配"正则表达式reg"后边的位置 (?<=reg)
# - 匹配后边跟的不是"正则表达式reg"的位置 (?!reg)
# - 匹配前边不是"正则表达式reg"的位置 (?<!reg)

# In[72]:


s = 'hellogreedyailove'

reg = '\w(?=greedyai)'

re.findall(reg,s)


# In[73]:


s = "5c714bb4397be4c5251a65c3,2,3,通州北苑,北京,朝阳,132.0,东南,2,近地铁 集中供暖,天时名苑 3室2厅 11000，https://m.lianjia.com/chuzu/bj/zufang/BJ2191007111268540416.html,153,11000,元/月,天时名苑,整租"

reg ='，(?=https)'

re.findall(reg,s)


# In[82]:


reg='(?<=11000)，'

re.findall(reg,s)


# ## 项目实战

# In[84]:


import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt


# In[85]:


data = pd.read_csv("D:/数据分析/10周学会数据分析/材料/9使用正则进行数据的复杂筛选/使用正则进行数据的复杂筛选/旅游.csv")
data.head()


# In[90]:


data['评分']=data['酒店'].str.extract('(\d\.\d)分/5分')
data.head()


# In[94]:


#data['酒店等级']=data['酒店'].str.extract('(\w\w型)')
#data['酒店等级']=data['酒店'].str.extract('(\w{2}型)')
data["酒店类型"]=data["酒店"].str.extract(' (.+) ')
data.head()


# In[96]:


data["天数"]=data["路线名"].str.extract('(\d+天\d+晚)')
data.head()


# In[97]:


zufang = pd.read_csv("D:/数据分析/10周学会数据分析/材料/9使用正则进行数据的复杂筛选/使用正则进行数据的复杂筛选/租房.csv")
zufang.head()


# In[109]:


zufang["网址"]=zufang["house_title"].str.extract('(https://.+)')


# In[110]:


def str_concat(a,b):
    return str(a)+"室"+str(b)+"厅"
# 这里有一个apply 函数， 主要作用是读取datafrom axis  作用于行，
zufang["户型"]= zufang.apply(lambda x:str_concat(x["bedroom_num"],x["hall_num"]),axis=1)


# In[112]:


zufang.head()


# In[113]:


# lambda  又叫做匿名函数

def add(x):
    return x+x

add(1)


# In[114]:


f = lambda x :x+x 

f(1)


# In[115]:


pinglun = pd.read_csv("D:/数据分析/10周学会数据分析/材料/9使用正则进行数据的复杂筛选/使用正则进行数据的复杂筛选/评论.csv")

pinglun.head()


# In[118]:


# 什么时候是用户活跃的评论时间  

time = pinglun["creationTime"].str.extract(' (\d{2}):')
time


# In[119]:


pinglun["hour"]=pinglun["creationTime"].str.extract(' (\d{2}):')
pinglun.head()


# In[122]:


a = np.sort(pinglun["hour"].unique())
a


# In[128]:


height = pinglun.groupby("hour").count()['content']
height


# In[130]:


# font={
# "family":"SimHei",
# "size":15
# }

# plt.rc('font',**font)

plt.figure(figsize=(20,5))

plt.bar(a,height=height)

plt.title('用户评论活跃时间段')

ax =plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')


# In[134]:


## 词云图的绘制

# 把句子变成词

"""
No module *****
pip install *****

"""


import jieba
data='我爱北京天安门，天安门上太阳升'

# cut_all = True 全模式切割

s = jieba.cut(data,cut_all=True)
r = '-'.join(s)

print(r)


# In[136]:


# 精准模式

s = jieba.cut(data,cut_all=False)

r = '-'.join(s)
print(r)


# In[137]:


# 搜索模式

s = jieba.cut_for_search(data)
r = '-'.join(s)
print(r)


# In[138]:


### cut 返回的结果是一个生成器  

### lcut   list_cut 返回结果是一个列表


# In[139]:


s = jieba.lcut(data)
s


# In[142]:


import jieba

recomment = pinglun['content']

text=''

for r in recomment:
    if r ==' ':
        continue
    text+=r
data_cut = " ".join(jieba.lcut(text))

from wordcloud import WordCloud

font = 'C:\Windows\Fonts\simkai.ttf'

w = WordCloud(font_path=font)
w.generate(data_cut)

image = w.to_file("评论词云图.png")


from PIL import Image
display(Image.open("评论词云图.png"))


# In[ ]:




