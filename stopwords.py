from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
text="the cat on the wall"
a=word_tokenize(text)
b=set(stopwords.words('english'))
c=[]
for i in a:
   if i.lower() not in b:
      c.append(i)
print(c)