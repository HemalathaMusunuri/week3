from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
sentences=["I Like friedrice","I Like noodles"]
a=TfidfVectorizer ()
b=a.fit_transform(sentences)
op=cosine_similarity(b[0],b[1])
print("similarity score:",op)
