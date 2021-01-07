import pandas as pd
import numpy as np
import sys
import gensim as gn
from gensim.parsing.preprocessing import remove_stopwords
  


print("###### train.py execution started ######")  

#Comman Line Args
data_filename = sys.argv[1]
model_filename= sys.argv[2]

#read the CSV file
data = pd.read_csv(data_filename) 

df_real = data.loc[data["label"] == "REAL"]
df_fake = data.loc[data["label"] == "FAKE"]

real_news= list(df_real['text'])
fake_news= list(df_fake['text'])

real_list=[]
fake_list=[]

for text in real_news:
  real_list.append( list(gn.utils.simple_preprocess(remove_stopwords(text),deacc=True)))

for text in fake_news:
  fake_list.append( list(gn.utils.simple_preprocess(remove_stopwords(text),deacc=True)))

#Train and save Real News model
model_real = gn.models.Word2Vec(real_list, size = 100, window = 4, min_count = 2, iter = 20)
model_real.init_sims(replace=True)
model_real.save("real_"+model_filename)

#Train and save Fake News model
model_fake = gn.models.Word2Vec(fake_list, size = 100, window = 4, min_count = 2, iter = 20)
model_fake.init_sims(replace=True)
model_fake.save("fake_"+model_filename)

print("###### train.py execution complete. ######")  

