import pandas as pd # data manupilation
from sklearn.model_selection import train_test_split # spliting data in 2 parts train and test
from sklearn.linear_model import LogisticRegression # algorithm 
import pickle
data=pd.DataFrame({
    'cgpa':[6,7,8,9,5,7.5,8.5,6.5],
    'aptitude':[60,70,80,90,75,85,65,95],
    'communication':[5,6,7,8,4,6,5,7],
    'projects':[1,2,3,4,1,2,3,1],
    'placed':[0,1,1,1,0,1,1,0]
})
x=data[['cgpa','aptitude','communication','projects']]
y=data['placed']
model=LogisticRegression()
model.fit(x,y)
pickle.dump(model,open('model.pkl','wb'))
print("model trained and saved")