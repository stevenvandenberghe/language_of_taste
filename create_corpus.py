import os
from nltk import RegexpTokenizer
from nltk.corpus.reader.plaintext import PlaintextCorpusReader

corpusdir = 'testcorpus/'
newcorpus = PlaintextCorpusReader(corpusdir, '.*', encoding="latin-1")
print(newcorpus.fileids())
for sen in newcorpus.sents('6070/Bruxelles_Gourmand_1976_Au_Cheval_Marin_32_33.txt'):
    print(sen)
