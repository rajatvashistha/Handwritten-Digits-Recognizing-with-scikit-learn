# Training the instance

svc.fit(digits.data[1:1790], digits.target[1:1790])
svc.fit(digits.data[321:800], digits.target[321:800])
svc.fit(digits.data[1:260], digits.target[1:260])

# Train-test split
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(digits.data,digits.target,test_size=0.25,random_state=0)
svc.fit(x_train, y_train)
y_pred = svc.predict(x_test)
y_pred
svc.predict(digits.data[1791:1797])
digits.target[1791:1797]

# Accuracy
from sklearn.metrics import accuracy_score
accuracy=accuracy_score(y_test,y_pred)*100
print(accuracy)
