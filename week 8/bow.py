import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

data = ["Urun cok guzel ve kaliteli","Urun cok kotu hic begenmedim","Kaliteli bir urun tavsiye ederim"]

count_vectorizer = CountVectorizer()
vectors=count_vectorizer.fit_transform(data)
words = count_vectorizer.get_feature_names_out()
vector_rep = vectors.toarray()
df = pd.DataFrame(vector_rep,columns=words,index=data)
print(df)