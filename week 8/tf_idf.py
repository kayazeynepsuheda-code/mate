import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

data = ["Urun cok guzel ve kaliteli","Urun cok kotu hic begenmedim","Kaliteli bir urun tavsiye ederim"]
tf_idf_vectorizer = TfidfVectorizer()

vectors=tf_idf_vectorizer.fit_transform(data)
words = tf_idf_vectorizer.get_feature_names_out()
vector_rep = vectors.toarray()
df = pd.DataFrame(vector_rep,columns=words,index=data)
print(df)

print(df.mean())