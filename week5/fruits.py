import pandas as pd

data = {'Fruits': ['Apple', 'Banana', 'Melon', 'Grape'],
        'Price': [23, 56, 92, 17],
        'Stock' : [85,12,7,0]}


df= pd.DataFrame(data)

df.drop(df[df['Stock'] == 0].index, inplace=True)
print(df)


result=df[df['Price']>40]

print(result['Fruits'])

