import pandas as pd

data = {'Worker':['Ali','Veli','Ayse','Fatma','Ahmet','Mehmet','Can'],
        'Salary':[25000,27000,24000,26000,28000,250000,23000]}

df = pd.DataFrame(data)
print(f"Mean : {df['Salary'].mean()}")
print(f"Median : {df['Salary'].median()} \n")

Q1 = df['Salary'].quantile(0.25)
Q3 = df['Salary'].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5*IQR
upper =Q3 + 1.5*IQR

outliers = df[(df['Salary'] < lower) | (df['Salary'] > upper)]

print(f"Outliers : \n{outliers}\n")

new_df = df.drop(outliers.index)

outliers = outliers.reset_index(drop=True)
new_df = new_df.reset_index(drop=True)

print(f"Outliers : \n{outliers}\n")
print(f"New DataFrame : \n{new_df}")

print(f"New DataFrame Mean : {new_df['Salary'].mean()}\nNew DataFrame Median : {new_df['Salary'].median()}\n")

print(f"Mean Difference : {df['Salary'].mean()-new_df['Salary'].mean()}")
print(f"Median Difference :{df['Salary'].median()-new_df['Salary'].median()}")


