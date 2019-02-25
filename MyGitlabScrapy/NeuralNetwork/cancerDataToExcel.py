#coding:utf-8
import pandas as pd
from sklearn.tree import export_graphviz
from sklearn import tree
from sklearn.datasets import load_breast_cancer
import numpy as np

# breast数据输入excel
# data = load_breast_cancer()#从sklearn.datasets下载良/恶性肿瘤预测数据
#
# #将breast_cancer数据存入Excel表格
# outputfile = "cancerData.xls"
# column = list(data['feature_names'])
# df = pd.DataFrame(data.data,index=range(569),columns= column)
# pf = pd.DataFrame(data.target,index=range(569),columns=['outcome'])
#
# jj = df.join(pf,how='outer')#用到DataFrame的合并方法，将data.data数据与data.target数据合并
# jj.to_excel(outputfile)#将数据保存到outputfile文件中

# excel数据读入模型
dataset = pd.read_excel('cancerData.xls',dtype={'code':str},sep='\t',index_col='Unnamed: 0')
print(dataset.head())
print dataset.info()
col = dataset.columns.values.tolist()
col1 =col[2:-1]
data_x = np.array(dataset[col1])
data_y = dataset['outcome']
print data_y