# word2vec

In this project, we will use the gensim library to demonstrate the use of word2vec. 

**TL;DR:** The program learns the text corpus and finds the top 5 most probable related words to the words we input to the algorithm. This is the underlying algorithm for text prediction.

## What is word2vec?

The word2vec algorithm uses a neural network model to learn word associations from a large corpus of text. Once trained, such a model can detect synonymous words or suggest additional words for a partial sentence. 


## Software Prequisites:
Python 3.x

## Instructions to Execute

1) Clone the Repo
2) Run the commands as below:

When running for the first time use the following command to to install gensim: <br>
$ pip install -U gensim

Command to run the consumer python program:<br>
$ python test.py fake_or_real_news.csv mymodel query_words.txt


NOTE: For changing words in query_words.txt, be careful to enter words exactly in the format below:

word1<br>
word2<br>
word3<br>
wordn<br>


### Next steps for the project:

Build a flask app implementation of autocomplete



