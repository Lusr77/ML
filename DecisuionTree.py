import pandas as pd
from sklearn import tree
from sklearn.externals import joblib
df=pd.read_csv('Testing..csv')
x=df.drop(columns='labels')
y=df['labels']
#features =[[weight,texture]] 0 represent rough,1 represent smooth

#labels-1 represent orange 2-represent berry 0-represent apple
classifier=tree.DecisionTreeClassifier()
classifier=classifier.fit(x,y)
# # joblib.dump(classifier,'fruitpredict.joblib')
# # # classifier = joblib.load('fruitpredict.joblib')
# print(classifier.predict([[67.5,1]]))
classify=classifier.predict([[67.5,1]])
if classify==0:
    print('SteveJobs apple')
elif classify==1:
    print('Pavan Orange')
elif classify==2:
    print('Berrie')
tree.export_graphviz(classifier,out_file="fruitPredictorr.dot",feature_names=['weight','texture'],class_names=sorted(y.unique()),label='all',rounded=True,filled=True)
