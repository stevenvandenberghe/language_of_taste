import csv
from collections import defaultdict
from nltk.corpus.reader.plaintext import CategorizedPlaintextCorpusReader
from nltk.tokenize import RegexpTokenizer
import nltk.data

word_tokenize = RegexpTokenizer('\w+(?:-\w+)*(?:[?!.,:])*')
sent_tokenize = nltk.data.load('tokenizers/punkt/french.pickle')
translation = str.maketrans("","", ",.?!:")

def create_corpus(directory):
    corpus = CategorizedPlaintextCorpusReader(directory, r"^[^.]*$", cat_file='cats.txt', encoding="iso-8859-1", word_tokenizer=word_tokenize, sent_tokenizer=sent_tokenize)
    return corpus

catcorpus = create_corpus('catcorpus/')
print(catcorpus.categories())