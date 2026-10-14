import numpy as np
import pandas as pd

steps=np.array([8000,1200,6500,10000,15000,4000,9000])
days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

data={'Steps':steps,
      'Days':days}

df=pd.DataFrame(data)

healty_days=df[df['Steps']>=10000]

print(healty_days)