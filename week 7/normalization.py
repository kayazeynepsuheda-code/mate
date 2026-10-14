import pandas as pd

data = {'Age':[2,5,10,1,8],
        'km':[20000,75000,150000,12000,110000]}

df = pd.DataFrame(data)

df_minmax=(df-df.min())/(df.max()-df.min())
df_z_score=(df-df.mean())/df.std()

print("Original")
print(df)
print(f"Original mean: \n{df.mean()}")

print("Min-Max Scaling")
print(df_minmax)
print(f"Min-Max mean: \n{df_minmax.mean()}")

print("Z-score")
print(df_z_score)
print(f"Z-score mean: \n{df_z_score.mean().round(10)}")