import pandas as pd
import sklearn.ensemble
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from tpot import TPOTRegressor
import matplotlib.pyplot as plt

df = pd.read_csv('../data/student-mat.csv')

columns_to_keep = ['sex', 'age', 'address', 'Pstatus', 'absences', 'traveltime', 'studytime', 'schoolsup', 'famsup',
                   'activities', 'paid', 'higher', 'internet', 'romantic', 'famrel', 'freetime', 'goout', 'Dalc',
                   'Walc', 'health', 'G1', 'G2', 'G3']

print(columns_to_keep)
example_to_predict = [
    [True, 16, False, True, 4, 1, 4, False, False, True, False, True, True, False, 4, 2, 2, 1, 1, 2, 19, 19]]
df = df[columns_to_keep]

print("Remaining columns:", df.columns)

df = df.dropna()

df['sex'] = df['sex'].map({'F': False, 'M': True})
df['address'] = df['address'].map({'U': False, 'R': True})
df['Pstatus'] = df['Pstatus'].map({'A': False, 'T': True})
df['schoolsup'] = df['schoolsup'].map({'no': False, 'yes': True})
df['famsup'] = df['famsup'].map({'no': False, 'yes': True})
df['paid'] = df['paid'].map({'no': False, 'yes': True})
df['activities'] = df['activities'].map({'no': False, 'yes': True})
df['higher'] = df['higher'].map({'no': False, 'yes': True})
df['internet'] = df['internet'].map({'no': False, 'yes': True})
df['romantic'] = df['romantic'].map({'no': False, 'yes': True})

y = df['G3']
X = df.drop('G3', axis=1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=69)

rf = RandomForestRegressor(max_depth=2, random_state=100)
rf.fit(X_train, y_train)

y_pred = rf.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print('predictions: ', y_pred)
print('mean squared error: ', mse)
print('R2: ', r2)

new_pred = rf.predict(example_to_predict)
print('New prediction:', int(new_pred))
