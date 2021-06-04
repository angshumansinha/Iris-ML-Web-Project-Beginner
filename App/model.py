import pandas as pd
import numpy as np
from sklearn.svm import SVC

df=pd.read_csv(r"App\Iris.csv")


from sklearn.preprocessing import LabelEncoder 
lb=LabelEncoder()
df.Species=lb.fit_transform(df.Species)

Feature=df.drop(columns=['Id','Species'],axis=1)
Target=df.Species

from sklearn.model_selection import train_test_split
X_train, X_test,y_train,y_test=train_test_split(Feature,Target,test_size=0.3,random_state=42)

model=SVC()
model.fit(X_train, y_train)

import pickle
#pickle.dump(model,open('App/model.pkl','wb'))
print(model.predict([[2,2,2,2]]))


