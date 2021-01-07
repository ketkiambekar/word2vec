Execute the following commands:

python3 train.py fake_or_real_news.csv mymodel
python3 test.py fake_or_real_news.csv mymodel query_words.txt

NOTE: 
If you get this error: 

ModuleNotFoundError: No module named 'gensim'

then just run the below command and the program should execute fine afterwards:

pip install -U gensim

======================================================================================================

If you still get the above error then execute the program in kong environment by typing the commands below:

1) cd /afs/cad.njit.edu/courses/ccs/s20/cs/677/002/kpa9/assignment_11
2) python3 train.py fake_or_real_news.csv mymodel
3) python3 test.py fake_or_real_news.csv my_model query_words.txt


======================================================================================================

NOTE: For changing words in query_words.txt, be careful to enter words exactly in the format below:

word1
word2
word3
wordn



# word2vec
