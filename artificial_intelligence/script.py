import pandas as pd

from datetime import datetime

from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn import svm
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split

virtues = pd.read_csv('virtues.csv', sep=',')

del virtues['Notes']
del virtues['Positive']
del virtues['Negative']

virtues['Date'] = pd.to_datetime(virtues['Date'])
virtues['Date'] = virtues['Date'].map(datetime.toordinal)

virtues.head(10)
virtues.info()
virtues.isnull().sum()

# Preprocessing Data
bins = (-7, 0, 7)
group_names = ['bad', 'good']
virtues['Balance'] = pd.cut(virtues['Balance'], bins=bins, labels=group_names)
virtues['Balance'].unique()

label_quality = LabelEncoder()
virtues['Balance'] = label_quality.fit_transform(virtues['Balance'])
virtues.head(10)
virtues['Balance'].value_counts()

# Now separate the dataset as response variable and feature variables
X = virtues.drop('Balance', axis=1)
y = virtues['Balance']

# Train and test splitting of data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# Applying Standard scaling to get optimized result
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Random Forest Classifier
rfc = RandomForestClassifier(n_estimators=200)
rfc.fit(X_train, y_train)
pred_rfc = rfc.predict(X_test)

print(classification_report(y_test, pred_rfc))
print(confusion_matrix(y_test, pred_rfc))

# SVM Classifier
clf = svm.SVC()
clf.fit(X_train, y_train)
pred_clf = clf.predict(X_test)

print(classification_report(y_test, pred_clf))
print(confusion_matrix(y_test, pred_clf))
