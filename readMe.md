# word2vec

In this project, we will use the gensim library to demonstrate the use of word2vec. 

## What is word2vec?
The word2vec algorithm uses a neural network model to learn word associations from a large corpus of text. Once trained, such a model can detect synonymous words or suggest additional words for a partial sentence. 

#### Uses 
Auto suggest words while typing a message

## Instructions to Execute

#### Software Prequisites:
Python 3.x

When running for the first time use the following comma. to install gensim: <br>
$ pip install -U gensim

$ python test.py fake_or_real_news.csv mymodel query_words.txt


NOTE: For changing words in query_words.txt, be careful to enter words exactly in the format below:

word1
word2
word3
wordn


### Next steps for the project:

Build a flask implementation of autocomplete



