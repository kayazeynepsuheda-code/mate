import pandas as pd
import numpy as np

data={'Customer':['Ahmet','Ayse','Mehmet','Fatma','Ali'],
      'Age':[25,np.nan,30,22,np.nan],
      'Expense':[1200,850,np.nan,3000,1500]}

df=pd.DataFrame(data)
print(df.isna().sum())

print(df.describe())
df['Age']=df['Age'].fillna(df['Age'].mean())
df['Expense']=df['Expense'].fillna(df['Expense'].median())

print(df)