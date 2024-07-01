#importing dependencies
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import train_test_split  # Corrected import

%matplotlib inline

#using pandas to read database stored in same folder
data = pd.read_csv('mnist.csv')

#viewing column head
print(data.head())

#extracting data from dataset and viewing them up close
a = data.iloc[3, 1:].values

#reshaping extracted data into reasonable size
a = a.reshape(28, 28).astype('uint8')
plt.imshow(a, cmap='gray')  # Added 'cmap' to display the image correctly
plt.show()

#preparing data
#separating labels and data values
df_x = data.iloc[:, 1:]
df_y = data.iloc[:, 0]

#creating test and train sizes
x_train, x_test, y_train, y_test = train_test_split(df_x, df_y, test_size=0.2, random_state=4)

#check data
print(y_train.head())

#call rf classifier
rf = RandomForestClassifier(n_estimators=100)

#fit the model
rf.fit(x_train, y_train)

#prediction on test data
pred = rf.predict(x_test)

#check prediction accuracy
s = y_test.values

#calculate number of correctly predicted values
count = 0
for i in range(len(pred)):
    if pred[i] == s[i]:
        count += 1

print(f'Number of correctly predicted values: {count}')

#total values that prediction code was run on
print(f'Total values: {len(pred)}')

# accuracy value
accuracy = count / len(pred)
print(f'Accuracy: {accuracy:.2f}')
