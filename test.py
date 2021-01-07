import gensim
from gensim.models import Word2Vec
from gensim.test.utils import datapath
from gensim.models import KeyedVectors
import numpy as np
from numpy.linalg import norm 
import sys

data_filename = sys.argv[1]
model_filename= sys.argv[2]
query_filename = sys.argv[3]

# data_filename = "fake_or_real_news.csv"
# model_filename= "my_model2"
# query_filename = "query_words.txt"


def get_query_words(filename):
  my_file = open(filename, "r")
  content_list=[]
  for line in my_file.readlines():
    content_list.append(line.replace('\n','').lower())
  #print(content_list)
  return content_list

def cosine_sim(model, word, topn):
  cos_sim = {}
  vocab = list(model.wv.vocab)
  a = model[word]
  norma = norm(a)
 
  for n in vocab:
    if n != word:
      b = model[n]
      similarity = np.dot(a,b)/(norma*norm(b))
      cos_sim[n] = similarity
  cos_sim = sorted(cos_sim.items(), key = lambda dist: dist[1], reverse = True)
  most_sim = []
  i = 0;
  for item in cos_sim:
    if not item[0] in ["he", "she", "him", "her", "his", "himself", "herself","mr.","mrs.","mr","mrs"]:    
      most_sim.append((item[0], item[1]))
      i += 1
    if i == topn:
      break
  return most_sim

if __name__ == "__main__":

  query_words=[]
  query_words=get_query_words(query_filename)

  #Load Real news Model
  my_model_real = Word2Vec.load("real_"+model_filename)

  #Load Fake News Model
  my_model_fake = Word2Vec.load("fake_"+model_filename)

  print("\n####### Real News: Top 5 similar words to query words ##########")

  #print Real News Similar Words
  for word in query_words:
    temp=cosine_sim(my_model_real,word,5)
    print("\n"+word)
    for n in temp:
      print("\t"+ str(n))

  print("\n####### Fake News: Top 5 similar words to query words ##########")

  #print Fake News Similar Words
  for word in query_words:
    temp=cosine_sim(my_model_fake,word,5)
    print("\n"+word)
    for n in temp:
      print("\t"+ str(n))
